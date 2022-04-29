"""
Utility functions to format text
"""
import re
import photoshop.api as ps
import proxyshop.helpers as psd
from proxyshop.constants import con
from proxyshop.gui import console_handler as console
app = ps.Application()

# Symbol colors
rgb_c = ps.SolidColor()
rgb_c.rgb.red = con.rgb_c['r']
rgb_c.rgb.green = con.rgb_c['g']
rgb_c.rgb.blue = con.rgb_c['b']

rgb_w = ps.SolidColor()
rgb_w.rgb.red = con.rgb_w['r']
rgb_w.rgb.green = con.rgb_w['g']
rgb_w.rgb.blue = con.rgb_w['b']

rgb_u = ps.SolidColor()
rgb_u.rgb.red = con.rgb_u['r']
rgb_u.rgb.green = con.rgb_u['g']
rgb_u.rgb.blue = con.rgb_u['b']

rgb_b = ps.SolidColor()
rgb_b.rgb.red = con.rgb_b['r']
rgb_b.rgb.green = con.rgb_b['g']
rgb_b.rgb.blue = con.rgb_b['b']

rgb_r = ps.SolidColor()
rgb_r.rgb.red = con.rgb_r['r']
rgb_r.rgb.green = con.rgb_r['g']
rgb_r.rgb.blue = con.rgb_r['b']

rgb_g = ps.SolidColor()
rgb_g.rgb.red = con.rgb_g['r']
rgb_g.rgb.green = con.rgb_g['g']
rgb_g.rgb.blue = con.rgb_g['b']


def locate_symbols(input_string):
    """
    Locate symbols in the input string, replace them with the characters we use to represent them in NDPMTG,
    and determine the colors those characters need to be. Returns an object with the modified input string and
    a list of symbol indices.
    """
    symbol = ""
    symbol_re = r"(\{.*?\})"
    symbol_indices = []
    try:
        while True:
            match = re.search(symbol_re, input_string)
            if match:
                symbol = match[1]
                symbol_index = match.span()[0]
                symbol_char = con.symbols[symbol]
                input_string = input_string.replace(symbol, symbol_char, 1)
                symbol_indices.extend([{
                    'index': symbol_index,
                    'colors': determine_symbol_colors(symbol, len(symbol_char))
                }])
            else: break
    except Exception as e:
        console.update(
            f"Encountered a formatted character in braces that doesn't map to characters: {symbol}", e
        )
    return {
        'input_string': input_string,
        'symbol_indices': symbol_indices
    }


def locate_italics(input_string, italics_strings):
    """
    Locate all instances of italic strings in the input string and record their start and end indices.
    Returns a list of italic string indices (start and end).
    """
    italics_indices = []

    for italics in italics_strings:

        # replace symbols with their character representations in the italic string
        if italics.find("}") >= 0:
            for key, symbol in con.symbols.items():
                try: italics = italics.replace(key, symbol)
                except Exception as e: console.log_exception(e)

        # Locate Italicized text
        end_index = 0
        while True:
            start_index = input_string.find(italics, end_index)
            end_index = start_index + len(italics)
            if start_index < 0: break

            italics_indices.extend([{
                'start_index': start_index,
                'end_index': end_index,
            }])

    return italics_indices


def determine_symbol_colors(symbol, symbol_length):
    """
    Determines the colors of a symbol (represented as Scryfall string) and returns an array of SolidColor objects.
    """
    symbol_color_map = {
        "W": rgb_w,
        "U": rgb_u,
        "B": rgb_c,
        "R": rgb_r,
        "G": rgb_g,
        "2": rgb_c,
    }

    # For hybrid symbols with generic mana, use the black symbol color rather than colorless for B
    hybrid_symbol_color_map = {
        "W": rgb_w,
        "U": rgb_u,
        "B": rgb_b,
        "R": rgb_r,
        "G": rgb_g,
        "2": rgb_c,
    }

    # SPECIAL SYMBOLS
    if symbol in ("{E}", "{CHAOS}"):
        # Energy or chaos symbols
        return [psd.rgb_black()]
    elif symbol == "{S}":
        # Snow symbol
        return [rgb_c, psd.rgb_black(), psd.rgb_white()]
    elif symbol == "{Q}":
        # Untap symbol
        return [psd.rgb_black(), psd.rgb_white()]

    # Phyrexian
    phyrexian_regex = r"\{([W,U,B,R,G])\/P\}"
    phyrexian_match = re.match(phyrexian_regex, symbol)
    if phyrexian_match: return [hybrid_symbol_color_map[phyrexian_match[1]], psd.rgb_black()]

    # Phyrexian hybrid
    phyrexian_hybrid_regex = r"\{([W,U,B,R,G])\/([W,U,B,R,G])\/P\}"
    phyrexian_hybrid_match = re.match(phyrexian_hybrid_regex, symbol)
    if phyrexian_hybrid_match:
        return [
            symbol_color_map[phyrexian_hybrid_match[2]],
            symbol_color_map[phyrexian_hybrid_match[1]],
            psd.rgb_black()
        ]

    # Hybrid
    hybrid_regex = r"\{([2,W,U,B,R,G])\/([W,U,B,R,G])\}"
    hybrid_match = re.match(hybrid_regex, symbol)
    if hybrid_match:
        color_map = symbol_color_map
        if hybrid_match[1] == "2":
            # Use the darker color for black's symbols for 2/B hybrid symbols
            color_map = hybrid_symbol_color_map
        return [
            color_map[hybrid_match[2]],
            color_map[hybrid_match[1]],
            psd.rgb_black(),
            psd.rgb_black()
        ]

    normal_symbol_regex = r"\{([W,U,B,R,G])\}"
    normal_symbol_match = re.match(normal_symbol_regex, symbol)
    if normal_symbol_match: return [symbol_color_map[normal_symbol_match[1]], psd.rgb_black()]

    if symbol_length == 2: return [rgb_c, psd.rgb_black()]
    print(f"Encountered a symbol that I don't know how to color: {symbol}")
    return None


def format_symbol(primary_action_list, starting_layer_ref, symbol_index, symbol_colors, layer_font_size):
    """
     * Formats an n-character symbol at the specified index (symbol length determined from symbol_colors).
    """
    current_ref = starting_layer_ref
    for i, color in enumerate(symbol_colors):
        desc1 = ps.ActionDescriptor()
        desc2 = ps.ActionDescriptor()
        desc3 = ps.ActionDescriptor()
        idTxtS = app.charIDToTypeID("TxtS")
        primary_action_list.putObject(app.charIDToTypeID("Txtt"), current_ref)
        desc1.putInteger(app.charIDToTypeID("From"), symbol_index + i)
        desc1.putInteger(app.charIDToTypeID("T   "), symbol_index + i + 1)
        desc2.putString(
            app.stringIDToTypeID("fontPostScriptName"),
            con.font_mana) # NDPMTG default
        desc2.putString(
            app.charIDToTypeID("FntN"),
            con.font_mana) # NDPMTG default
        desc2.putUnitDouble(
            app.charIDToTypeID("Sz  "),
            app.charIDToTypeID("#Pnt"),
            layer_font_size)
        desc2.putBoolean(app.stringIDToTypeID("autoLeading"), False)
        desc2.putUnitDouble(
            app.charIDToTypeID("Ldng"),
            app.charIDToTypeID("#Pnt"),
            layer_font_size)
        desc3.putDouble(
            app.charIDToTypeID("Rd  "),
            color.rgb.red) # rgb value.red
        desc3.putDouble(
            app.charIDToTypeID("Grn "),
            color.rgb.green) # rgb value.green
        desc3.putDouble(
            app.charIDToTypeID("Bl  "),
            color.rgb.blue) # rgb value.blue
        desc2.putObject(
            app.charIDToTypeID("Clr "),
            app.charIDToTypeID("RGBC"),
            desc3)
        desc1.putObject(idTxtS, idTxtS, desc2)
        current_ref = desc1
    return current_ref


def format_text(input_string, italics_strings, flavor_index, is_centered):
    """
     * Inserts the given string into the active layer and formats it according to defined parameters with symbols
     * from the NDPMTG font.
     * @param {str} input_string The string to insert into the active layer
     * @param {Array[str]} italic_strings An array containing strings that are present in the main input string
     and should be italicised
     * @param {int} flavor_index The index at which linebreak spacing should be increased and any subsequent
     chars should be italicised (where the card's flavor text begins)
     * @param {boolean} is_centered Whether or not the input text should be centre-justified
    """

    # record the layer's justification before modifying the layer in case it's reset along the way
    layer_justification = app.activeDocument.activeLayer.textItem.justification

    # TODO: check that the active layer is a text layer, and raise an issue if not
    if flavor_index > 0: quote_index = input_string.find("\r", flavor_index + 3)
    else: quote_index = 0

    # Locate symbols and update the input string
    ret = locate_symbols(input_string)
    input_string = ret['input_string']
    symbol_indices = ret['symbol_indices']

    # Locate italics text indices
    italics_indices = locate_italics(input_string, italics_strings)

    # Prepare action descriptor and reference variables
    layer_font_size = app.activeDocument.activeLayer.textItem.size
    layer_text_color = app.activeDocument.activeLayer.textItem.color
    # layer_text_color = rgb_grey()
    primary_action_descriptor = ps.ActionDescriptor()
    primary_action_list = ps.ActionList()
    desc119 = ps.ActionDescriptor()
    desc27 = ps.ActionDescriptor()
    desc26 = ps.ActionDescriptor()
    desc25 = ps.ActionDescriptor()
    ref101 = ps.ActionReference()
    desc141 = ps.ActionDescriptor()
    desc142 = ps.ActionDescriptor()
    desc143 = ps.ActionDescriptor()
    list13 = ps.ActionList()
    list14 = ps.ActionList()
    idparagraphStyleRange = app.stringIDToTypeID("paragraphStyleRange")
    idfontPostScriptName = app.stringIDToTypeID("fontPostScriptName")
    idfirstLineIndent = app.stringIDToTypeID("firstLineIndent")
    idparagraphStyle = app.stringIDToTypeID("paragraphStyle")
    idkerningRange = app.stringIDToTypeID("kerningRange")
    idautoLeading = app.stringIDToTypeID("autoLeading")
    idstartIndent = app.stringIDToTypeID("startIndent")
    idspaceBefore = app.stringIDToTypeID("spaceBefore")
    idleadingType = app.stringIDToTypeID("leadingType")
    idspaceAfter = app.stringIDToTypeID("spaceAfter")
    idendIndent = app.stringIDToTypeID("endIndent")
    idsetd = app.charIDToTypeID("setd")
    idTxLr = app.charIDToTypeID("TxLr")
    idT = app.charIDToTypeID("T   ")
    idFntN = app.charIDToTypeID("FntN")
    idSz = app.charIDToTypeID("Sz  ")
    idPnt = app.charIDToTypeID("#Pnt")
    idClr = app.charIDToTypeID("Clr ")
    idRd = app.charIDToTypeID("Rd  ")
    idGrn = app.charIDToTypeID("Grn ")
    idBl = app.charIDToTypeID("Bl  ")
    idRGBC = app.charIDToTypeID("RGBC")
    idLdng = app.charIDToTypeID("Ldng")
    idTxtt = app.charIDToTypeID("Txtt")
    idFrom = app.charIDToTypeID("From")
    ref101.putEnumerated(
        idTxLr,
        app.charIDToTypeID("Ordn"),
        app.charIDToTypeID("Trgt"))
    desc119.putReference(app.charIDToTypeID("null"), ref101)
    primary_action_descriptor.putString(app.charIDToTypeID("Txt "), input_string)
    desc25.putInteger(idFrom, 0)
    desc25.putInteger(idT, len(input_string))
    desc26.putString(idfontPostScriptName, con.font_rules_text)  # MPlantin default
    desc26.putString(idFntN, con.font_rules_text)  # MPlantin default
    desc26.putUnitDouble(idSz, idPnt, layer_font_size)
    desc27.putDouble(idRd, layer_text_color.rgb.red)  # text color.red
    desc27.putDouble(idGrn, layer_text_color.rgb.green)  # text color.green
    desc27.putDouble(idBl, layer_text_color.rgb.blue)  # text color.blue
    desc26.putObject(idClr, idRGBC, desc27)
    desc26.putBoolean(idautoLeading, False)
    desc26.putUnitDouble(idLdng, idPnt, layer_font_size)
    idTxtS = app.charIDToTypeID("TxtS")
    desc25.putObject(idTxtS, idTxtS, desc26)
    current_layer_ref = desc25

    for italics_indice in italics_indices:
        # Italics text
        primary_action_list.putObject(idTxtt, current_layer_ref)
        desc125 = ps.ActionDescriptor()
        desc125.putInteger(idFrom, italics_indice['start_index'])  # italics start index
        desc125.putInteger(idT, italics_indice['end_index'])  # italics end index
        desc126 = ps.ActionDescriptor()
        desc126.putString(idfontPostScriptName, con.font_rules_text_italic)  # MPlantin italic default
        desc126.putString(idFntN, con.font_rules_text_italic)  # MPlantin italic default
        desc126.putUnitDouble(idSz, idPnt, layer_font_size)
        desc126.putBoolean(idautoLeading, False)
        desc126.putUnitDouble(idLdng, idPnt, layer_font_size)
        # Added
        descTemp = ps.ActionDescriptor()
        """
        # GREY
        descTemp.putDouble(idRd, 170)  // text color.red
        idGrn = app.charIDToTypeID("Grn ")
        descTemp.putDouble(idGrn, 170)  // text color.green
        idBl = app.charIDToTypeID("Bl  ")
        descTemp.putDouble(idBl, 170)  // text color.blue
        """
        # Default text box
        descTemp.putDouble(idRd, layer_text_color.rgb.red)  # text color.red
        descTemp.putDouble(idGrn, layer_text_color.rgb.green)  # text color.green
        descTemp.putDouble(idBl, layer_text_color.rgb.blue)  # text color.blue
        desc126.putObject(idClr, idRGBC, descTemp)
        # End
        desc125.putObject(idTxtS, idTxtS, desc126)
        current_layer_ref = desc125

    # Format each symbol correctly
    for symbol_indice in symbol_indices:
        current_layer_ref = format_symbol(
            primary_action_list = primary_action_list,
            starting_layer_ref = current_layer_ref,
            symbol_index = symbol_indice['index'],
            symbol_colors = symbol_indice['colors'],
            layer_font_size = layer_font_size,
        )

    primary_action_list.putObject(idTxtt, current_layer_ref)
    primary_action_descriptor.putList(idTxtt, primary_action_list)

    # paragraph formatting
    desc141.putInteger(idFrom, 0)
    desc141.putInteger(idT, len(input_string))  # input string length
    desc142.putUnitDouble(idfirstLineIndent, idPnt, 0)
    desc142.putUnitDouble(idstartIndent, idPnt, 0)
    desc142.putUnitDouble(idendIndent, idPnt, 0)
    if is_centered:  # line break lead
        desc142.putUnitDouble(idspaceBefore, idPnt, 0)
    else:
        desc142.putUnitDouble(idspaceBefore, idPnt, con.line_break_lead)
    desc142.putUnitDouble(idspaceAfter, idPnt, 0)
    desc142.putInteger(app.stringIDToTypeID("dropCapMultiplier"), 1)
    desc142.putEnumerated(idleadingType, idleadingType, app.stringIDToTypeID("leadingBelow"))
    desc143.putString(idfontPostScriptName, con.font_mana)  # NDPMTG default
    desc143.putString(idFntN, con.font_rules_text)  # MPlantin default
    desc143.putBoolean(idautoLeading, False)
    primary_action_descriptor.putList(idparagraphStyleRange, list13)
    primary_action_descriptor.putList(idkerningRange, list14)
    list13 = ps.ActionList()

    if input_string.find("\u2022") >= 0:
        # Modal card with bullet points - adjust the formatting slightly
        startIndexBullet = input_string.find("\u2022")
        endIndexBullet = input_string.rindex("\u2022")
        list13 = ps.ActionList()
        desc141 = ps.ActionDescriptor()
        desc141.putInteger(idFrom, startIndexBullet)
        desc141.putInteger(idT, endIndexBullet + 1)
        desc142.putUnitDouble(idfirstLineIndent, idPnt, -con.modal_indent) # negative modal indent
        desc142.putUnitDouble(idstartIndent, idPnt, con.modal_indent) # modal indent
        desc142.putUnitDouble(idspaceBefore, idPnt, 1)
        desc142.putUnitDouble(idspaceAfter, idPnt, 0)
        desc143 = ps.ActionDescriptor()
        desc143.putString(idfontPostScriptName, con.font_mana)  # NDPMTG default
        desc143.putString(idFntN, con.font_rules_text) # MPlantin default
        desc143.putUnitDouble(idSz, idPnt, 11.998500)  # TODO: what's this?
        desc143.putBoolean(idautoLeading, False)
        desc142.putObject(app.stringIDToTypeID("defaultStyle"), idTxtS, desc143)
        desc141.putObject(idparagraphStyle, idparagraphStyle, desc142)
        list13.putObject(idparagraphStyleRange, desc141)
        primary_action_descriptor.putList(idparagraphStyleRange, list13)
        list14 = ps.ActionList()
        primary_action_descriptor.putList(idkerningRange, list14)

    if flavor_index > 0:
        # Adjust line break spacing if there's a line break in the flavor text
        desc141 = ps.ActionDescriptor()
        desc141.putInteger(idFrom, flavor_index + 3)
        idT = app.charIDToTypeID("T   ")
        desc141.putInteger(idT, flavor_index + 4)
        desc142.putUnitDouble(idfirstLineIndent, idPnt, 0)
        idimpliedFirstLineIndent = app.stringIDToTypeID("impliedFirstLineIndent")
        desc142.putUnitDouble(idimpliedFirstLineIndent, idPnt, 0)
        desc142.putUnitDouble(idstartIndent, idPnt, 0)
        idimpliedStartIndent = app.stringIDToTypeID("impliedStartIndent")
        desc142.putUnitDouble(idimpliedStartIndent, idPnt, 0)
        desc142.putUnitDouble(idspaceBefore, idPnt, con.flavor_text_lead) # lead size between rules text and flavor text
        desc141.putObject(idparagraphStyle, idparagraphStyle, desc142)
        list13.putObject(idparagraphStyleRange, desc141)
        primary_action_descriptor.putList(idparagraphStyleRange, list13)
        list14 = ps.ActionList()
        primary_action_descriptor.putList(idkerningRange, list14)

    if quote_index > 0:
        # Adjust line break spacing if there's a line break in the flavor text
        desc141 = ps.ActionDescriptor()
        desc141.putInteger(idFrom, quote_index + 3)
        idT = app.charIDToTypeID("T   ")
        desc141.putInteger(idT, len(input_string))
        desc142.putUnitDouble(idspaceBefore, idPnt, 0)
        desc141.putObject(idparagraphStyle, idparagraphStyle, desc142)
        list13.putObject(idparagraphStyleRange, desc141)
        primary_action_descriptor.putList(idparagraphStyleRange, list13)
        list14 = ps.ActionList()
        primary_action_descriptor.putList(idkerningRange, list14)

    # Push changes to document
    desc119.putObject(idT, idTxLr, primary_action_descriptor)
    app.executeAction(idsetd, desc119, ps.DialogModes.DisplayNoDialogs)

    # Reset layer's justification and disable hypenation
    app.activeDocument.activeLayer.textItem.justification = layer_justification
    app.activeDocument.activeLayer.textItem.hyphenation = False


def generate_italics(card_text):
    """
     * Generates italics text array from card text to italicise all text within (parentheses) and all ability words.
    """
    reminder_text = True
    italic_text = []
    end_index = 0
    while reminder_text:
        start_index = card_text.find("(", end_index)
        if start_index >= 0:
            end_index = card_text.find(")", start_index + 1)
            end_index += 1
            italic_text.extend([card_text[start_index:end_index]])
        else: reminder_text = False

    # Attach all ability words to the italics array
    for ability_word in con.ability_words:
        italic_text.extend([ability_word + " \u2014"])  # Include em dash

    # italic_text.color = psd.rgb_grey()
    return italic_text


def format_text_wrapper():
    """
     Wrapper for format_text which runs the function with the active layer's current text contents
     and auto-generated italics array. Flavor text index and centered text not supported.
     Super useful to add as a script action in Photoshop for making cards manually!
    """
    card_text = app.activeDocument.activeLayer.textItem.contents
    italic_text = generate_italics(card_text)
    italic_text.color = psd.rgb_grey()
    format_text(card_text, italic_text, -1, False)


def strip_reminder_text(oracle_text):
    """
    Strip out any reminder text that a card's oracle text has (reminder text in parentheses).
    If this would empty the string, instead return the original string.
    """
    oracle_text_stripped = re.sub(r"\([^()]*\)", "", oracle_text)

    # ensure we didn't add any double whitespace by doing that
    oracle_text_stripped = re.sub(r"  +", "", oracle_text_stripped)
    if oracle_text_stripped != "":
        return oracle_text_stripped
    return oracle_text

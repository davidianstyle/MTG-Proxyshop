﻿"""
GLOBAL CONSTANTS
Keep all global variables here.
"""
import json
import os
from pathlib import Path
cwd = os.getcwd()
version = "v1.1.0"

# Ensure mandatory folders are created
Path(os.path.join(cwd, "out")).mkdir(mode=511, parents=True, exist_ok=True)
Path(os.path.join(cwd, "tmp")).mkdir(mode=511, parents=True, exist_ok=True)

# PATHS
json_custom_path = os.path.join(cwd, "tmp\\custom.json")
scryfall_scan_path = os.path.join(cwd, "tmp\\card.jpg")

# Card classes - finer grained than Scryfall layouts
normal_class = "normal"
transform_front_class = "transform_front"
transform_back_class = "transform_back"
ixalan_class = "ixalan"
mdfc_front_class = "mdfc_front"
mdfc_back_class = "mdfc_back"
mutate_class = "mutate"
adventure_class = "adventure"
leveler_class = "leveler"
saga_class = "saga"
miracle_class = "miracle"
planeswalker_class = "planeswalker"
pw_tf_front_class = "pw_tf_front"
pw_tf_back_class = "pw_tf_back"
pw_mdfc_front_class = "pw_mdfc_front"
pw_mdfc_back_class = "pw_mdfc_back"
snow_class = "snow"
basic_class = "basic"
planar_class = "planar"

# LAYER NAMES
layers = {
    "WHITE": "W",
    "BLUE": "U",
    "BLACK": "B",
    "RED": "R",
    "GREEN": "G",
    "WU": "WU",
    "UB": "UB",
    "BR": "BR",
    "RG": "RG",
    "GW": "GW",
    "WB": "WB",
    "BG": "BG",
    "GU": "GU",
    "UR": "UR",
    "RW": "RW",
    "ARTIFACT": "Artifact",
    "COLORLESS": "Colorless",
    "NONLAND": "Nonland",
    "LAND": "Land",
    "GOLD": "Gold",
    "VEHICLE": "Vehicle",

    # frame layer group names
    "PT_BOX": "PT Box",
    "PT_AND_LEVEL_BOXES": "PT and Level Boxes",
    "TWINS": "Name & Title Boxes",
    "LEGENDARY_CROWN": "Legendary Crown",
    "PINLINES_TEXTBOX": "Pinlines & Textbox",
    "PINLINES_AND_SAGA_STRIPE": "Pinlines & Saga Stripe",
    "PINLINES": "Pinlines",
    "LAND_PINLINES_TEXTBOX": "Land Pinlines & Textbox",
    "COMPANION": "Companion",
    "BACKGROUND": "Background",
    "NYX": "Nyx",

    # borders
    "BORDER": "Border",
    "NORMAL_BORDER": "Normal Border",
    "LEGENDARY_BORDER": "Legendary Border",

    # shadows
    "SHADOWS": "Shadows",
    "HOLLOW_CROWN_SHADOW": "Hollow Crown Shadow",

    # legal
    "LEGAL": "Legal",
    "ARTIST": "Artist",
    "SET": "Set",
    "COLLECTOR": "Collector",
    "TOP_LINE": "Top",
    "BOTTOM_LINE": "Bottom",

    # text and icons
    "TEXT_AND_ICONS": "Text and Icons",
    "NAME": "Card Name",
    "NAME_SHIFT": "Card Name Shift",
    "NAME_ADVENTURE": "Card Name - Adventure",
    "TYPE_LINE": "Typeline",
    "TYPE_LINE_SHIFT": "Typeline Shift",
    "TYPE_LINE_ADVENTURE": "Typeline - Adventure",
    "MANA_COST": "Mana Cost",
    "MANA_COST_ADVENTURE": "Mana Cost - Adventure",
    "EXPANSION_SYMBOL": "Expansion Symbol",
    "EXPANSION_REFERENCE": "Expansion Reference",
    "COLOR_INDICATOR": "Color Indicator",
    "POWER_TOUGHNESS": "Power / Toughness",
    "FLIPSIDE_POWER_TOUGHNESS": "Flipside Power / Toughness",
    "RULES_TEXT": "Rules Text",
    "RULES_TEXT_NONCREATURE": "Rules Text - Noncreature",
    "RULES_TEXT_NONCREATURE_FLIP": "Rules Text - Noncreature Flip",
    "RULES_TEXT_CREATURE": "Rules Text - Creature",
    "RULES_TEXT_CREATURE_FLIP": "Rules Text - Creature Flip",
    "RULES_TEXT_ADVENTURE": "Rules Text - Adventure",
    "MUTATE": "Mutate",

    # planar text and icons
    "STATIC_ABILITY": "Static Ability",
    "CHAOS_ABILITY": "Chaos Ability",
    "CHAOS_SYMBOL": "Chaos Symbol",
    "PHENOMENON": "Phenomenon",
    "TEXTBOX": "Textbox",

    # textbox references
    "TEXTBOX_REFERENCE": "Textbox Reference",
    "TEXTBOX_REFERENCE_LAND": "Textbox Reference Land",
    "TEXTBOX_REFERENCE_ADVENTURE": "Textbox Reference - Adventure",
    "MUTATE_REFERENCE": "Mutate Reference",
    "PT_REFERENCE": "PT Adjustment Reference",
    "PT_TOP_REFERENCE": "PT Top Reference",

    # planeswalker
    "FIRST_ABILITY": "First Ability",
    "SECOND_ABILITY": "Second Ability",
    "THIRD_ABILITY": "Third Ability",
    "FOURTH_ABILITY": "Fourth Ability",
    "STARTING_LOYALTY": "Starting Loyalty",
    "LOYALTY_GRAPHICS": "Loyalty Graphics",
    "STATIC_TEXT": "Static Text",
    "ABILITY_TEXT": "Ability Text",
    "TEXT": "Text",
    "COST": "Cost",

    # art frames
    "ART_FRAME": "Art Frame",
    "FULL_ART_FRAME": "Full Art Frame",
    "BASIC_ART_FRAME": "Basic Art Frame",
    "PLANESWALKER_ART_FRAME": "Planeswalker Art Frame",
    "SCRYFALL_SCAN_FRAME": "Scryfall Scan Frame",

    # transform
    "TF_FRONT": "tf-front",
    "TF_BACK": "tf-back",
    "MDFC_FRONT": "mdfc-front",
    "MDFC_BACK": "mdfc-back",
    "MOON_ELDRAZI_DFC": "mooneldrazidfc",

    # mdfc
    "TOP": "Top",
    "BOTTOM": "Bottom",
    "LEFT": "Left",
    "RIGHT": "Right",
}

default_layer = "Layer 1"

basic_land_names = [
    "Plains",
    "Island",
    "Swamp",
    "Mountain",
    "Forest",
    "Wastes",
    "Snow-Covered Plains",
    "Snow-Covered Island",
    "Snow-Covered Swamp",
    "Snow-Covered Mountain",
    "Snow-Covered Forest"
]

# Card faces
Faces = {
    "FRONT": 0,
    "BACK": 1,
}

# font_name_mplantin = "MPlantin"
# font_name_mplantin_italic = "MPlantin-Italic"
# font_name_ndpmtg = "NDPMTG"
# font_name_beleren_smallcaps = "Beleren Small Caps Bold"
# font_name_relay_medium = "Relay-Medium"

# Font names
font_rules_text = "MPlantin"
font_rules_text_italic = "MPlantin-Italic"
font_mana = "NDPMTG"
font_subtext = "Beleren Small Caps Bold"
font_collector = "Relay-Medium"

# Font spacing
modal_indent = 5.7
line_break_lead = 2.4
flavor_text_lead = 4.4

# NDPMTG font dictionary to translate Scryfall symbols to font character sequences
symbols = {
    "{W/P}": "Qp",
    "{U/P}": "Qp",
    "{B/P}": "Qp",
    "{R/P}": "Qp",
    "{G/P}": "Qp",
    "{W/U/P}": "Qqp",
    "{U/B/P}": "Qqp",
    "{B/R/P}": "Qqp",
    "{R/G/P}": "Qqp",
    "{G/W/P}": "Qqp",
    "{W/B/P}": "Qqp",
    "{B/G/P}": "Qqp",
    "{G/U/P}": "Qqp",
    "{U/R/P}": "Qqp",
    "{R/W/P}": "Qqp",
    "{E}": "e",
    "{T}": "ot",
    "{X}": "ox",
    "{0}": "o0",
    "{1}": "o1",
    "{2}": "o2",
    "{3}": "o3",
    "{4}": "o4",
    "{5}": "o5",
    "{6}": "o6",
    "{7}": "o7",
    "{8}": "o8",
    "{9}": "o9",
    "{10}": "oA",
    "{11}": "oB",
    "{12}": "oC",
    "{13}": "oD",
    "{14}": "oE",
    "{15}": "oF",
    "{16}": "oG",
    "{20}": "oK",
    "{W}": "ow",
    "{U}": "ou",
    "{B}": "ob",
    "{R}": "or",
    "{G}": "og",
    "{C}": "oc",
    "{W/U}": "QqLS",
    "{U/B}": "QqMT",
    "{B/R}": "QqNU",
    "{R/G}": "QqOV",
    "{G/W}": "QqPR",
    "{W/B}": "QqLT",
    "{B/G}": "QqNV",
    "{G/U}": "QqPS",
    "{U/R}": "QqMU",
    "{R/W}": "QqOR",
    "{2/W}": "QqWR",
    "{2/U}": "QqWS",
    "{2/B}": "QqWT",
    "{2/R}": "QqWU",
    "{2/G}": "QqWV",
    "{S}": "omn",
    "{Q}": "ol",
    "{CHAOS}": "?"
}

# Ability words which should be italicised in formatted text
ability_words = [
    "Adamant",
    "Addendum",
    "Battalion",
    "Bloodrush",
    "Channel",
    "Chroma",
    "Cohort",
    "Converge",
    "Council's dilemma",
    "Delirium",
    "Domain",
    "Eminence",
    "Enrage",
    "Fateful hour",
    "Ferocious",
    "Formidable",
    "Grandeur",
    "Hellbent",
    "Heroic",
    "Imprint",
    "Inspired",
    "Join forces",
    "Kinship",
    "Landfall",
    "Lieutenant",
    "Metalcraft",
    "Morbid",
    "Parley",
    "Radiance",
    "Raid",
    "Rally",
    "Revolt",
    "Spell mastery",
    "Strive",
    "Sweep",
    "Tempting offer",
    "Threshold",
    "Undergrowth",
    "Will of the council",
    "Magecraft",

    # AFR ability words
    "Antimagic Cone",
    "Fear Ray",
    "Pack tactics",
    "Acid Breath",
    "Teleport",
    "Lightning Breath",
    "Wild Magic Surge",
    "Two-Weapon Fighting",
    "Archery",
    "Bear Form",
    "Mage Hand",
    "Cure Wounds",
    "Dispel Magic",
    "Gentle Reprise",
    "Beacon of Hope",
    "Displacement",
    "Drag Below",
    "Siege Monster",
    "Dark One's Own Luck",
    "Climb Over",
    "Tie Up",
    "Rappel Down",
    "Rejuvenation",
    "Engulf",
    "Dissolve",
    "Poison Breath",
    "Tragic Backstory",
    "Cunning Action",
    "Stunning Strike",
    "Circle of Death",
    "Bardic Inspiration",
    "Song of Rest",
    "Sneak Attack",
    "Tail Spikes",
    "Dominate Monster",
    "Flurry of Blows",
    "Divine Intervention",
    "Split",
    "Magical Tinkering",
    "Keen Senses",
    "Grant an Advantage",
    "Smash the Chest",
    "Pry It Open",
    "Fire Breath",
    "Cone of Cold",
    "Brave the Stench",
    "Search the Body",
    "Search the Room",
    "Bewitching Whispers",
    "Whispers of the Grave",
    "Animate Walking Statue",
    "Trapped!",
    "Invoke Duplicity",
    "Combat Inspiration",
    "Cold Breath",
    "Life Drain",
    "Fight the Current",
    "Find a Crossing",
    "Intimidate Them",
    "Fend Them Off",
    "Smash It",
    "Lift the Curse",
    "Steal Its Eyes",
    "Break Their Chains",
    "Interrogate Them",
    "Foil Their Scheme",
    "Learn Their Secrets",
    "Journey On",
    "Make Camp",
    "Rouse the Party",
    "Set Off Traps",
    "Form a Party",
    "Start a Brawl",
    "Make a Retreat",
    "Stand and Fight",
    "Distract the Guards",
    "Hide",
    "Charge Them",
    "Befriend Them",
    "Negative Energy Cone",

    # Midnight Hunt words
    "Coven",
]

# Card rarities
rarity_common = "common"
rarity_uncommon = "uncommon"
rarity_rare = "rare"
rarity_mythic = "mythic"
rarity_special = "special"
rarity_bonus = "bonus"

# Symbol colors
rgb_c = {'r': 204, 'g': 194, 'b': 193}
rgb_w = {'r': 255, 'g': 251, 'b': 214}
rgb_u = {'r': 170, 'g': 224, 'b': 250}
rgb_b = {'r': 159, 'g': 146, 'b': 143}
rgb_r = {'r': 249, 'g': 169, 'b': 143}
rgb_g = {'r': 154, 'g': 211, 'b': 175}

# Import symbol library
with open(os.path.join(cwd, "proxyshop/symbols.json"), encoding="utf-8-sig") as js:
    set_symbols = json.load(js)


class Con:
    def __init__(self):
        # PATHS
        self.cwd = cwd
        self.json_custom_path = json_custom_path
        self.scryfall_scan_path = scryfall_scan_path

        # Card classes - finer grained than Scryfall layouts
        self.normal_class = normal_class
        self.transform_front_class = transform_front_class
        self.transform_back_class = transform_back_class
        self.ixalan_class = ixalan_class
        self.mdfc_front_class = mdfc_front_class
        self.mdfc_back_class = mdfc_back_class
        self.mutate_class = mutate_class
        self.adventure_class = adventure_class
        self.leveler_class = leveler_class
        self.saga_class = saga_class
        self.miracle_class = miracle_class
        self.planeswalker_class = planeswalker_class
        self.pw_tf_front_class = pw_tf_front_class
        self.pw_tf_back_class = pw_tf_back_class
        self.pw_mdfc_front_class = pw_mdfc_front_class
        self.pw_mdfc_back_class = pw_mdfc_back_class
        self.snow_class = snow_class
        self.basic_class = basic_class
        self.planar_class = planar_class

        # Layer names
        self.layers = layers
        self.default_layer = default_layer

        # Cards
        self.symbols = symbols
        self.ability_words = ability_words
        self.basic_land_names = basic_land_names
        self.set_symbols = set_symbols
        self.Faces = Faces

        # Font names
        self.font_rules_text = font_rules_text
        self.font_rules_text_italic = font_rules_text_italic
        self.font_mana = font_mana
        self.font_subtext = font_subtext
        self.font_collector = font_collector

        # Font spacing
        self.modal_indent = modal_indent
        self.line_break_lead = line_break_lead
        self.flavor_text_lead = flavor_text_lead

        # Card rarities
        self.rarity_common = rarity_common
        self.rarity_uncommon = rarity_uncommon
        self.rarity_rare = rarity_rare
        self.rarity_mythic = rarity_mythic
        self.rarity_special = rarity_special
        self.rarity_bonus = rarity_bonus

        # Symbol colors
        self.rgb_c = rgb_c
        self.rgb_w = rgb_w
        self.rgb_u = rgb_u
        self.rgb_b = rgb_b
        self.rgb_r = rgb_r
        self.rgb_g = rgb_g

    def reload(self):
        self.__init__()

# Global instance
con = Con()

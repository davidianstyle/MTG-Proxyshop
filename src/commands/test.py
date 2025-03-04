"""
* CLI Commands: Testing
"""
# Third Party
import click

# Local Imports
from src import CONSOLE as logr, PATH
from src.tests import frame_logic, text_logic

"""
* TEST COMMANDS
"""


@click.group()
def test_cli():
    """Cli interface for test funcs."""
    pass


@test_cli.command()
@click.option('-T', '--target', is_flag=True, default=False, help="Evaluate a specific test case.")
def test_frame_logic(target: bool = False):
    """Run Frame Logic test on all cases."""
    logr.info(f"Test Utility: Frame Logic ({PATH.CWD})")
    cases = frame_logic.get_frame_logic_cases()

    # Was this a targeted case?
    if not target:
        return frame_logic.test_all_cases()

    # Choose test case
    options = {str(i): title for i, title in enumerate(cases.keys())}
    while True:
        choice = input("Enter the number for a test case to evaluate:\n" +
                       "\n".join([f"[{i}] {n}" for i, n in options.items()]))
        if choice not in options:
            print("Choice provided was invalid.")
        break

    # Run the test
    case = options[choice]
    logr.info(f"CASE: {case}")
    frame_logic.test_target_case(cases[case])


@test_cli.command()
def test_text_logic():
    """Run Text Logic test on all cases."""
    text_logic.test_all_cases()


# Export CLI
__all__ = ['test_cli']

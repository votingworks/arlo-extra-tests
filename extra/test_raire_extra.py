# This file runs extra RAIRE tests if they are present.
from pathlib import Path
from  server.tests.audit_math.test_raire import run_test
import pytest


RAIRE_INPUT_DIR = "server/tests/audit_math/ExtraRaireData/Input/"
RAIRE_OUTPUT_DIR = "server/tests/audit_math/ExtraRaireData/Output/"

def pytest_generate_tests(metafunc):
    input_files = Path(RAIRE_INPUT_DIR).glob("*.raire")
    metafunc.parametrize("input_file", input_files)
    output_files = Path(RAIRE_OUTPUT_DIR).glob("*.raire.out")
    metafunc.parametrize("output_file", output_files)

#@pytest.mark.parametrize("input_file,output_file",input_files, output_files)
def test_files(input_file, output_file):
    # TODO: find a better value for agap...
    agap = 0
    run_test(input_file, output_file, agap)

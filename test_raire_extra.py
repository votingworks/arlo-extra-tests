# This file runs extra RAIRE tests if they are present.
from pathlib import Path
from  server.tests.audit_math.test_raire import run_test
import pytest


RAIRE_INPUT_DIR = "server/tests/arlo-extra-tests/ExtraRaireData/Input/"
RAIRE_OUTPUT_DIR = "server/tests/arlo-extra-tests/ExtraRaireData/Output/"

def idfn(file_name):
    if isinstance(file_name, tuple):
        return file_name[0].parts[-1]
    return repr(file_name)

def pytest_generate_tests(metafunc):
    input_files = Path(RAIRE_INPUT_DIR).rglob("*.raire")
    file_tuples = []
    for input_file in input_files:
        output_file = str(input_file).replace("Input", "Output") + ".out"
        file_tuples.append((input_file, output_file))

    metafunc.parametrize("file_pair", file_tuples, ids=idfn)

def test_files(file_pair):
    # TODO: find a better value for agap?
    agap = 0
    run_test(file_pair[0],file_pair[1], agap)

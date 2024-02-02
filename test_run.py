import json
import subprocess

# path to executable
EXEC_PATH = "YOUR_EXECUTABLE_PATH"
# path to test spec
TEST_SPEC = "PATH TO student_tests.json file (name doesn't matter)"


def convert_windows_crlf_to_linux(b: bytes):
    return b"\n".join(b.split(b"\r\n"))


def pytest_generate_tests(metafunc):
    # read test spec
    with open(TEST_SPEC, 'r') as spec_file:
        json_data = json.loads(spec_file.read())

    # parametrize tests with the data from the json file
    # also make sure names are indicative based on json file
    metafunc.parametrize("json_data", json_data['tests'],
                         ids=[i['name'] for i in json_data['tests']])


def test_json_case(json_data):
    proc = subprocess.Popen([EXEC_PATH], stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    # pass input to file and get output back
    out = proc.communicate(input=bytes(json_data['input'], 'utf-8'), timeout=4)

    # windows hacks
    actual_output = convert_windows_crlf_to_linux(out[0])
    # truncate last newline, for some reason gradescope ignores it
    actual_output = actual_output[:len(actual_output) - 1]

    assert actual_output == bytes(json_data['output'], 'utf-8')

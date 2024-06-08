import warnings
from binary_class import Binary, InvalidBinaryOperationException

warnings.filterwarnings("ignore")

test_results = []

def run_test(test_lambda, test_description, expected_exception=None):
    try:
        result = test_lambda()
        test_results.append(result)
        if result:
            print(f"Passed: {test_description}")
        else:
            print(f"\033[91mFailed: {test_description}\033[0m")  # Red color for failed tests
    except Exception as e:
        passed = isinstance(e, expected_exception) if expected_exception else False
        test_results.append(passed)
        if passed:
            print(f"Passed: {test_description}")
        else:
            print(f"\033[91mFailed: {test_description}\033[0m") 

# 1. Test Initialization
run_test(lambda: Binary('1010', 'unsigned').value == '1010' and Binary('1010', 'unsigned').type == 'unsigned', "Test Initialization with valid binary and type")
run_test(lambda: Binary('1010', 'invalid'), "Test Initialization with invalid type", ValueError)
run_test(lambda: Binary(1010, 'unsigned'), "Test Initialization with non-string binary", ValueError)

# 2. Test `to_dec` Method
run_test(lambda: Binary('1010', 'unsigned').to_dec() == 10, "Test `to_dec` with unsigned binary")
run_test(lambda: Binary('11010', 'signed').to_dec() == -10, "Test `to_dec` with signed binary")
run_test(lambda: Binary('11110110', 'twos-complement').to_dec() == -10, "Test `to_dec` with two's complement binary")

# 3. Test `add` Method
run_test(lambda: Binary('1010', 'unsigned').add(Binary('0101', 'unsigned')).value == '1111', "Test `add` with two unsigned binaries")
run_test(lambda: Binary('1010', 'signed').add(Binary('0101', 'signed')), "Test `add` with two signed binaries", InvalidBinaryOperationException)
run_test(lambda: Binary('1010', 'unsigned').add(Binary('0101', 'signed')), "Test `add` with mixed types", InvalidBinaryOperationException)
run_test(lambda: Binary('1010', 'unsigned').add("0101"), "Test `add` with invalid type", InvalidBinaryOperationException)

# 4. Count and Display Test Results
passed_tests = test_results.count(True)
failed_tests = len(test_results) - passed_tests
print(f"Passed: {passed_tests}, Failed: {failed_tests}")
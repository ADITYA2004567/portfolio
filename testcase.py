class TestCase:
    def __init__(self, test_case_id, screen, functionality, precondition, test_condition, test_case_steps, expected_result):
        self.test_case_id = test_case_id
        self.screen = screen
        self.functionality = functionality
        self.precondition = precondition
        self.test_condition = test_condition
        self.test_case_steps = test_case_steps
        self.expected_result = expected_result
 
    def display_info(self):
        print(f"Test Case ID: {self.test_case_id}")
        print(f"Screen: {self.screen}")
        print(f"Functionality: {self.functionality}")
        print(f"Precondition: {self.precondition}")
        print(f"Test Condition: {self.test_condition}")
        print(f"Test Case Steps: {self.test_case_steps}")
        print(f"Expected Result: {self.expected_result}")
 
example_test_case = TestCase(
test_case_id="Tc_001",
screen="Login",
functionality="Authentication",
precondition="",
test_condition="",
test_case_steps="",
expected_result=""
)
example_test_case.display_info()
 
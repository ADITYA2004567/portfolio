class TestCase:
    def __init__(self, test_case_id, functionality, role):
        self.test_case_id = test_case_id
        self.functionality = functionality
        self.role = role

class FunctionalTestCase(TestCase):
    def __init__(self, *args, priority='Medium', **kwargs):
        super().__init__(*args, **kwargs)
        self.priority = priority
test = FunctionalTestCase(101, 'Login Feature', 'Tester', priority='High')

print(test.test_case_id)     
print(test.functionality)     
print(test.role)              
print(test.priority)  
print(test.priority)      
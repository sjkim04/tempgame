import main

class TestClass:

    def test_function_1(self):
        # Override the Python built-in input method 
        main.input = lambda: ''
        # Call the function you would like to test (which uses input)
        output = module.function()  
        assert output == 'または始めるを入力'

    def test_function_2(self):
        main.input = lambda: 'y'
        output = module.function()  
        assert output == 'GAME OVER'        

    def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
        main.input = input  

from  config.config_reader import ConfigReader

class Calculator:
    def add(self, a, b):
        return a + b

    def test1(self):
        config_file= ConfigReader()
        # Example static values (you can modify this with actual dynamic values)
        username = config_file.get_required("username")
        password = config_file.get_required("password")
        print(f"Username: {username} \tPass: {password}")

# Main block to run the Calculator class methods
if __name__ == "__main__":
    calc = Calculator()
    result = calc.add(4, 6)
    print(f"Addition Result: {result}")
    calc.test1()
    #rightclick inside this and run!!!
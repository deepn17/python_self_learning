class Calculator:

    def show_menu(self):
        print("\n Calculator Menu")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def add(self,a, b):
        """Add two values using the '+' operator"""
        return a + b

    def subtract(self,a, b):
        """Subtract two values using the '-' operator"""
        return a - b

    def multiply(self,a, b):
        """Multiply two values using the '*' operator"""
        return a * b

    def divide(self, a, b):
        """Divide two values using the '/' operator"""
        if b == 0:
            return "Cannot divide by Zero"
        return a / b

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-5): ")

            if choice == '5':
                print("Goodbye!")
                break

            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if choice == '1':
                print("Result:", self.add(a, b))
            elif choice == '2':
                print("Result:", self.subtract(a, b))
            elif choice == '3':
                print("Result:", self.multiply(a, b))
            elif choice == '4':
                print("Result:", self.divide(a, b))
            else:
                print("Invalid choice")


calc = Calculator()
calc.run()
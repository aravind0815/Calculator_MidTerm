from app.commands import Command

class AddCommand(Command):
    def execute(self):
        try:
            input1 = float(input("Enter the first number: "))
            input2 = float(input("Enter the second number: "))
            print(input1 + input2)
        except:
            print("Please enter the correct numbers!")
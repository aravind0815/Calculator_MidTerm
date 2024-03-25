from app.commands import Command

class AddCommand(Command):
    def execute(self):
        input1 = float(input("Enter the first number: "))
        input2 = float(input("Enter the second number: "))
        print(input1 - input2)

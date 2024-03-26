import logging
from app.commands import Command
from app.history import History

class MultiplyCommand(Command):
    def execute(self):
        try:
            hist_inst = History()
            input1 = float(input("Enter the first number: "))
            input2 = float(input("Enter the second number: "))
            result = input1 * input2
            print('The result of the operation is', result)
            logging.info(f'Multiplication of {input1} and {input2} = {input1 * input2}')
            logging.info('The Multiplication operation was performed successfully')
            data = ['multiply', input1, input2]
            existing_data = hist_inst.get_as_list()
            existing_data.append(data)
            hist_inst.writing_the_data(existing_data)

        except ValueError:
                print("Please enter a valid number!")
                logging.info('The Multiplication operation failed')

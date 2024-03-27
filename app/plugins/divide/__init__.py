import logging
from app.commands import Command
from app.history import History

class DivideCommand(Command):
    def execute(self):

        try:

            hist_inst = History()
            input1 = float(input("Enter the first number: "))
            input2 = float(input("Enter the second number: "))
            if input2 == 0:
                raise ZeroDivisionError
            
            result = input1 / input2
            print('The result of the operation is', result)
            logging.info(f'division of {input1} and {input2} = {input1 / input2}')
            logging.info('The Division operation was performed successfully')
            print(input1 / input2)
            data = ['divide', input1, input2]
            existing_data = hist_inst.get_as_list()
            existing_data.append(data)
            hist_inst.writing_the_data(existing_data)

        except ZeroDivisionError:
            print('This action results in Divide by zero error')
            logging.error("The number cannot be divided by zero.")

        except ValueError:
            print('Please enter a Valid number')
            logging.info('Divison operation was unsuccessful')


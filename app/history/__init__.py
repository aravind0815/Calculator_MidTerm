import os
import logging
import pandas as pd

class History:
    def __init__(self):
        path= os.environ.get('calc_file_path')
        self.path = path
        self.counter = 1
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
            logging.info(f"The directory '{os.path.dirname(path)}' is created.")

        elif not os.access(os.path.dirname(path), os.W_OK):
            logging.error(f"The directory '{os.path.dirname(path)}' is not writable.")

    def writing_the_data(self, data):
        data_without_id = [record[1:] if len(record) == 4 else record for record in data]
        data_with_id = [[self.counter + i] + record for i, record in enumerate(data_without_id)]
        self.counter += len(data)
        cal_data = pd.DataFrame(data_with_id, columns=['ID','action', 'arg1', 'arg2'])
        cal_data.to_csv(self.path, index=False)
    
    def get_as_list(self):
        existing_data = pd.read_csv(self.path)
        return existing_data.values.tolist()
    
    def get_as_data_frame(self):
        return pd.read_csv(self.path)
    
    def clear(self):
        cal_data = pd.DataFrame([], columns=['ID','action', 'arg1', 'arg2'])
        cal_data.to_csv(self.path, index=False)
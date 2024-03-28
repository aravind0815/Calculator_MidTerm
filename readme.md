# Advanced Calculator Optimization: A Comprehensive Overview of Design Patterns, Logging, and Error Handling
This report outlines the design and implementation of a Python module for managing a history of calculations within a calculator application. The system utilizes various design patterns, logging strategies, and error handling techniques to provide a robust and user-friendly experience.

## Setup Guide

### Step 1: Clone the Repository
    #To get started, clone the repository by executing the following command in your terminal:

    git clone repository_link

### Step 2: Install Dependencies
    #Next, navigate to the cloned repository directory and install the required dependencies using the following command:

    pip install -r requirements.txt

### Step 3: Configure Environment Variables
    #Create a `.env` file in the root directory and add the following key-value pair to specify the file path for the calculator history:

    CALC_HISTORY_FILE_PATH='./data/calculator_history.csv'


### Step 4: Run the Application
    #Execute the main application file `main.py` using the following command:

    python3 main.py


## Examples of Usage
Once the application is running, utilize the 'menu' command to view a list of available functionalities.
[Click here](https://github.com/aravind0815/Calculator_MidTerm/tree/main/app/plugins) to access the source code for additional insights.

This setup ensures a seamless experience for managing and executing the calculator application.

### Performing Division
To execute the division operation:
1. Enter the command 'divide' within the REPL command interface.
2. Input the dividend and divisor when prompted.
3. The system will compute the quotient and display the result.

Please note: If you attempt to divide any number by zero, a ZeroDivisionError will occur.

For detailed implementation, refer to the following link: [Division Operation](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/divide/__init__.py)

### Other Arithmetic Operations
To perform arithmetic operations other than division, you can use the following commands within the REPL command interface:

1. **add** - for addition
2. **subtract** - for subtraction
3. **multiply** - for multiplication

Simply input the desired command and follow the prompts to enter the necessary numbers. The system will execute the corresponding operation and display the result.

For detailed implementation, refer to the following links:
- [Addition Operation](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/add/__init__.py)
- [Subtraction Operation](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/subtract/__init__.py)
- [Multiplication Operation](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/multiply/__init__.py)


## Implementation Overview

### Design Patterns

1. **Command Pattern**:
   The `execute` method within the command handling code exemplifies the Command pattern. Each command, such as `add`, `subtract`, etc., is represented as an object that encapsulates the operation to be executed. This design promotes decoupling between the invoker (e.g., user input) and the executor (e.g., calculation logic), enhancing modularity and extensibility.
   [Explore the implementation](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/commands/__init__.py) 

2. **Facade Pattern**:
    The `History` class acts as a gateway, offering a streamlined approach to manage CSV files with the power of pandas. It provides an intuitive interface with methods like `writing_the_data`, `get_as_list`, `get_as_dataframe`, and `clear`, shielding users from the intricacies of file management and pandas intricacies. This abstraction empowers users to manipulate CSV data effortlessly, abstracting away the complexities of data handling.
    [Explore the implementation](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/history/__init__.py)

3. **Factory Method Pattern**:
   The `load_plugin` method in the app's `__init__.py` file of the application dynamically loads new plugins without requiring explicit configuration. This demonstrates the Factory Method pattern, allowing for the creation of objects without specifying their exact class types. This promotes flexibility and scalability in the application's architecture.
   [See how it's implemented](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/__init__.py)

4. **Singleton Pattern**:
   The `MenuCommand` class serves as a singleton instance, ensuring that only one instance is created throughout the application's lifecycle. The singleton pattern is observed in the implementation of the 'MenuCommand' class within the 
   "app.plugins.menu" module. This promotes resource efficiency and ensures consistent behavior across the application.
   [Review the singleton implementation](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/__init__.py)


### Managing Calculation History
Here are the commands available for managing the calculation history within the calculator application:

#### 1. TO Load the data and View History (load)
To retrieve all data from the CSV file, use the command:
```
>>> load
```
This command will display the complete history of calculations performed, including the action performed and the values used.
Implementation of load [click here](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/load/__init__.py)
    example:
        >>> load
            Calculator history data:
                ID   action     arg1  arg2
                1      add      3.0   2.0
                2    subtract   5.0   3.0
                3   multiply    5.0   4.0
                4    divide     4.0   2.0


#### 2. Delete Specific Record (delete)
To remove a specific record from the history by its ID field, follow these steps:
1. Enter the command:
```
>>> delete
```
2. Input the ID of the record you wish to delete when prompted.
3. The system will update and display the history after the deletion.
Implementtion of delete [click here](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/delete/__init__.py)
    example:
        >>> delete
            Enter the ID of the record to delete: 4
            2024-03-27 22:33:15,422 - root - INFO - History of the record with ID 4 has been deleted.
            Data history of calculator after deletion:
            ID   action     arg1   arg2
            1     add       3.0    2.0
            2   subtract    5.0    3.0
            3   multiply    5.0    4.0

#### 3. Clear History (clear)
To delete all stored history, utilize the command:
```
>>> clear
```
Executing this command will clear the entire history, providing a clean slate for new calculations.
Implementation of clear [click here](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/clear/__init__.py)


### Logging Approach

The application implements a robust logging mechanism leveraging Python's logging library to ensure comprehensive monitoring and effective troubleshooting:

1. **Initialization and Configuration**:
   Logging setup is orchestrated at the onset of the application, usually within the main module or entry point. This setup encompasses configuring parameters like logging level, format, and output destination (e.g., console, file). A dedicated logging configuration file (`logging.conf`) is utilized to centralize and streamline configuration settings, enhancing maintainability and flexibility.
   [Explore the logging configuration](https://github.com/aravind0815/Calculator_MidTerm/blob/main/logging.conf)

2. **Usage and Message Categorization**:
   Throughout the application's codebase, logging is strategically integrated to capture a wide spectrum of messages, including informational, warning, and error messages. Each log message is carefully categorized based on its severity and relevance, facilitating efficient triaging and prioritization during troubleshooting endeavors.
   ### some of the log messages for reference:
        2024-03-27 01:03:44,156 - root - INFO - Multiplication of 7.0 and 8.0 = 56.0
        2024-03-27 01:03:44,156 - root - INFO - The Multiplication operation was performed successfully
        2024-03-27 01:03:50,748 - root - INFO - division of 90.0 and 5.0 = 18.0
        2024-03-27 01:03:50,748 - root - INFO - The Division operation was performed successfully
        2024-03-27 01:03:56,652 - root - INFO - Calculator history has been fetched and loaded:  
        ID   action    arg1  arg2
        1      add     3.0   2.0
        2   subtract   4.0   2.0
        3   multiply   7.0   8.0
        4    divide    90.0  5.0

3. **Exception Handling and Error Reporting**:
    Robust error handling mechanisms, demonstrated through try/except blocks, are strategically implemented across key sections of the codebase, including file operations and computational tasks. These mechanisms are consistently utilized in modules such as subtract, add, multiply, and divide, ensuring comprehensive error coverage. In case of exceptions, detailed error messages are logged to provide developers with contextual insights into the root cause and context of the error, facilitating prompt diagnosis and resolution of issues.
[Dive into the error handling strategy](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/subtract/__init__.py)

By adopting this logging approach, the application ensures transparency, traceability, and resilience in its operational lifecycle, thereby fortifying its reliability and maintainability in diverse operational scenarios.


### EAFP (Easier to Ask for Forgiveness than Permission)

The Pythonic EAFP (Easier to Ask for Forgiveness than Permission) paradigm is elegantly showcased in the application's error handling strategy:

1. **Implementation**:
   Delve into the `divide` plugin's implementation, where the try/except mechanism gracefully manages potential 'ZeroDivisionError' exceptions. This approach embodies Pythonic ideals, fostering code clarity and readability while ensuring robust error management.
   [Discover the EAFP implementation](https://github.com/aravind0815/Calculator_MidTerm/blob/main/app/plugins/divide/__init__.py)

This distinctive approach to design patterns, logging strategies, and error handling techniques not only enhances the application's reliability but also elevates the overall user experience to new heights.


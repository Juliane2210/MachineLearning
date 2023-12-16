# sys is a module used to manipulate
# ##different parts of the Python Runtime Environment.
import sys
from src.logger import logging

# This function will take an exception object (error) and error_detail (instance of sys).


def error_message_detail(error, error_detail: sys):
    # Using exc_info() it will retrieve a tuple containing info about the exception(type, value, traceback)
    # and only assign the traceback to exc_tb.
    _, _, exc_tb = error_detail.exc_info()

# extracts the filename from the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename

    # constructing an error message using the extracted information
    # (file name, line number, and string representation of original error)
    error_message = "Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message


# CustomException class that inherits from the built-in Exception class
# constructor takes two parameters(error_message, error_detail) and calls Exception base constructor
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

# overrides the base __str__ method and returns the stored error message
    def __str__(self):
        return self.error_message


# This code will not be executed automatically  if exception.py is imported,
if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)

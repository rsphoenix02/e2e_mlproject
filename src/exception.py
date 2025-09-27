import sys
from src.logger import logging

class CustomException(Exception):
    def __init__(self, error_message:str, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
def error_message_detail(error:str, error_detail:sys)->str:
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script name {filename}, line no {line_number}.\nError message: {str(error)}"

    return error_message
import sys
import os
from Heart.exception import CustomException
from Heart.logger import logging

def test_exception():
    try:
        logging.info("error occured here")
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)

if __name__=="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)


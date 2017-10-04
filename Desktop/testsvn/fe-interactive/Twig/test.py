"""
a function which returns the contents of the array divided into positive integer N equally sized arrays.
If the size of the original array cannot be divided equally by N, the final part should have length equal to the
reminder.
To test the function, please only run the following command:
==> python unit_test.py
You can import "mySplit" from the "test" and use the function in your own program.
There is a log file which is saved all the log of running this script.
"""
# version 0.0.1
from math import ceil
import logging
logger = logging.getLogger('myLog')
hdlr = logging.FileHandler('Twig.log')
formatter = logging.Formatter('%(asctime)s--%(module)s--%(levelname)s--%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

def mySplit(inputList,size):
    """
        Calls the methods that create first of all check the types and constraints and then split the list.
    """
    if size <= 0:
        logger.error("the argument of size is not a positive integer")
        return inputList
    if type(inputList) is not list:
        logger.error("the input is a " + str(type(inputList)) + ". It must be a list. ")
        return inputList
    step = int(ceil(len(inputList)/float(size)))
    logger.debug("The number of input in each cell is: " + str(step))
    output = []
    for index in range(size):
        if (len(inputList[:step]) != 0):
            output.append(inputList[:step])
            inputList = inputList[step:]
    logger.debug("The output is: " + str(output))
    return output
'''
Contains class for setting up logging
'''
import logging

class AddLogging:
    '''
    Class for setting up logging
    '''
    def create_logger(self, test_name, loglevel):
        '''
        Creates logger with specific log file format
        '''
        logger = logging.getLogger(test_name)
        file_handler = logging.FileHandler('logfile.log')

        # pass the Formatter class information to the logger object
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.setLevel(loglevel)
        return logger

import inspect
import logging

class Log_class:

    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        file = logging.FileHandler(".\\Logs\\ Bankapp.log")
        log_formate = logging.Formatter(" %(asctime)s : %(levelname)s : %(funcName)s : %(message)s ")
        file.setFormatter(log_formate)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
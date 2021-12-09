# 2021 Dec 4 - customLogger.py
#
# Logger class that outputs test case results into a log file.
# Expected log output: "2021:Dec:4_13:47:01_INFO_***Test Passed***"....
########################################################################
import logging

class LogGen:
    @staticmethod # Rewrote 4Dec2021- J-WoW
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s_%(levelname)s_%(message)s',
                    datefmt='%Y:%b:%d_%H:%M:%S',
                    filename= '.\\Logs\\automation.log')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
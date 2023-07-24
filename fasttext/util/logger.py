import logging
from pytz import timezone
from datetime import datetime

class Logger:
    def __init__(self, name):
        self._domain = name.replace("__","")
        self._logger = logging.getLogger(self._domain)
        self._file_path = "/tmp/log/" + self._domain + ".log"
        self._file_handler = logging.FileHandler(self._file_path)
        self._formatter = logging.Formatter('%(asctime)s (%(name)s) [%(levelname)s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        # FIXME:timezoneをJSTに設定したい
        #self._formatter.converter = datetime.now(timezone('Asia/Tokyo')).timetuple()
        self._file_handler.setFormatter(self._formatter)
        self._file_handler.setLevel(logging.INFO)
        self._logger.setLevel(logging.INFO)
        self._logger.addHandler(self._file_handler)

    def get_logger(self):
        return self._logger

import logging
from common.yaml_handler import yaml_data


class LoggerHandler(logging.Logger):
    def __init__(self, name='root', level='DEBUG', file=None, log_format=None):
        super().__init__(self)
        self.name = name
        self.setLevel(level)
        fmt = logging.Formatter(log_format)
        # if import the file, output the file log
        if file:
            file_handler = logging.FileHandler(file, encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        # output console log
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


logger = LoggerHandler(name=yaml_data['logger_1']['name'], level=yaml_data['logger_1']['level'],
                       file='../logs/my_log.txt',
                       log_format=yaml_data['logger_1']['format'])

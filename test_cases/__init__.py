from common.yaml_handler import YamlHandler
from common.logger_handler import LoggerHandler

yaml_data = YamlHandler.read_yaml('../configs/config.yaml')
logger = LoggerHandler(name='test-chen', level=yaml_data['logger_1']['level'], file='../logs/my_log.txt',
                       log_format=yaml_data['logger_1']['format'])

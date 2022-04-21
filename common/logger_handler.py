import logging

logger = logging.getLogger('This is the name')

logger.setLevel('DEBUG')

fmt = logging.Formatter('%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s')

file_handler = logging.FileHandler('../logs/mylog.txt')

file_handler.setLevel('DEBUG')

file_handler.setFormatter(fmt)

ch = logging.StreamHandler()

ch.setLevel("DEBUG")

ch.setFormatter(fmt)

logger.addHandler(file_handler)

logger.addHandler(ch)

if __name__ == "__main__":
    logger.debug('自定义的debug日志')
    logger.info('自定义的info日志')
    logger.warning('自定义的warning日志')
    logger.error('自定义的error日志')
    logger.critical('自定义的critical日志')

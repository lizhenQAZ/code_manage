import logging
import logging.config

# 配置日志文件，控制台打印
logging.config.fileConfig('E1_logging.conf')
# create logger
logger = logging.getLogger('E1_logging')
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


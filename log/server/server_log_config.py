import logging
from logging import handlers

logger = logging.getLogger('server_log_app')

formatter = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

# file_handler = logging.FileHandler('server.log', encoding='utf-8')
file_handler = handlers.TimedRotatingFileHandler('server.log', encoding='utf-8', interval=1, when='D')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


# if __name__ == '__main__':
#     console = logging.StreamHandler()
#     console.setLevel(logging.DEBUG)
#     console.setFormatter(formatter)
#     logger.addHandler(console)
#     logger.info('some test')

import logging


logger = logging.getLogger('client_log_app')

formatter = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

file_handler = logging.FileHandler('client.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


# if __name__ == '__main__':
#     console = log.StreamHandler()
#     console.setLevel(log.DEBUG)
#     console.setFormatter(formatter)
#     logger.addHandler(console)
#     logger.info('some test')


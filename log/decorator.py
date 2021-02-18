import logging
import inspect


class Log:

    def __init__(self):
        pass

    def __call__(self, func):
        def decorator(*args, **kwargs):
            log_message = f"call function '{func.__name__}' from file " \
                          f"{list(str(inspect.stack()[1][0]).split())[4].split(',')[0]}"
            if list(str(inspect.stack()[1][0]).split())[4].split(',')[0] == "'client.py'":
                logger = logging.getLogger('client_log_app')
                logger.info(log_message)
            if list(str(inspect.stack()[1][0]).split())[4].split(',')[0] == "'server.py'":
                logger = logging.getLogger('server_log_app')
                logger.info(log_message)
            return func(*args, **kwargs)

        return decorator

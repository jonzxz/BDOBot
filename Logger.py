import logging, Constants

# Logger
logger = logging.getLogger(__name__)
# Root debug level
logger.setLevel(level=logging.DEBUG)
# CLI Debug Handler config - set to DEBUG and above.
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_formatter = logging.Formatter(Constants.LOGGING_STREAM_FORMAT)
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)

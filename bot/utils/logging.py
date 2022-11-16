import sys
import logging
from logging.handlers import TimedRotatingFileHandler


LOG_NAME = "logs/bot.log"

logger = logging.getLogger('bot')
logger.setLevel(level=logging.DEBUG)

formatter = logging.Formatter(u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s')

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

time_rotating_handler = TimedRotatingFileHandler(LOG_NAME, when="midnight", interval=1, encoding="utf-8")
time_rotating_handler.suffix = "%Y%m%d"
time_rotating_handler.setFormatter(formatter)
time_rotating_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(time_rotating_handler)
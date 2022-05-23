import os
import logging
import jsonpickle

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def print(event, context):
    logger.info(
        f'\n## ENVIRONMENT VARIABLES\n{jsonpickle.encode(dict(**os.environ))}\n')
    logger.info(f'\n## EVENT\n{jsonpickle.encode(event)}\n')
    logger.info(f'\n## CONTEXT\n{jsonpickle.encode(context)}\n')
    return

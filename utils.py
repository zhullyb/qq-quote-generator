import os

class Config(object):
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT') or 5000
    RETURN_PNG = os.environ.get('RETURN_PNG') or False
    GECKODRIVER_PATH = os.environ.get('GECKODRIVER_PATH') or None
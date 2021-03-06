"""
Set environmental variables for local testing.
"""

import os, sys
sout = sys.stdout.write
serr = sys.stderr.write

# 
filePath = os.path.abspath(__file__)
TEST_DIR, fn = os.path.split(filePath)
HOME_DIR = os.path.split(TEST_DIR)[0]
DATA_DIR = os.path.join(HOME_DIR, 'data')

#####################################################
# Define environmental variables
vals = [
    ('DATA_DIR', os.path.join(HOME_DIR, 'data')),
    ('REPO_DIR', HOME_DIR),
    ('WWW_DIR', os.path.join(HOME_DIR, 'www')),
    #('MONGODB_USERNAME', "LMM"),
    #('MONGODB_PASSWORD', "123456"),
    ('MONGODB_HOST', 'localhost'),
    ('MONGODB_PORT', '27017'),
    ('INTERNAL_SERVE_IP', '127.0.0.1'),
    ('INTERNAL_SERVE_PORT', '8000'),
    ('PYTHON_DIR', ''),
]

dir_keys = ['DATA_DIR', 'REPO_DIR']
######################################################

def setupEnv():
    print 'Setting up testing environmental variables.'

    # Update the environmental variables
    os.environ.update(vals)

    # Create any of these directories if they do not already exist
    for dk in dir_keys:
        d = os.environ[dk]
        if not os.path.exists(d):
            os.mkdir(d)

def fixSysPath():
    print 'Setting sys.path to include the dcmetrometrics package at: %s'%HOME_DIR
    sys.path = [HOME_DIR] + sys.path


# def setupDB():
#     """
#     Setup the MongoDB with the User/Password
#     """
#     import pymongo

#     print 'Adding user to the MetroEscalators MongoDB'

#     host = os.environ["MONGODB_HOST"]
#     port = int(os.environ["MONGODB_PORT"])

#     user = os.environ["MONGODB_USERNAME"]
#     password = os.environ["MONGODB_PASSWORD"]

#     client = pymongo.MongoClient(host, port)
#     db = client.MetroEscalators
#     db.add_user(user, password)

print '*'*50
print 'Creating testing environment\n\n'

setupEnv()
fixSysPath()
#setupDB()
print 'DONE'
print '*'*50 + '\n\n'


from dcmetrometrics.common import dbGlobals

def connect():
    dbGlobals.connect()


def setup_logging():

    print "Setting up logging"
    ###############################################################
    # Log the ELES App to a file.
    import logging

    LOG_FILE_NAME = os.path.join(DATA_DIR, 'ELESApp.log')
    fh = logging.FileHandler(LOG_FILE_NAME)
    sh = logging.StreamHandler(sys.stderr)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    logger = logging.getLogger('ELESApp')
    logger.addHandler(fh)
    logger.addHandler(sh)

    # Set up logging for HotCar App.
    hot_car_logger = logging.getLogger("HotCarApp")
    hot_car_file = os.path.join(DATA_DIR, 'HotCarApp.log')
    fh = logging.FileHandler(hot_car_file)
    sh = logging.StreamHandler(sys.stderr)
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    hot_car_logger.addHandler(fh)
    hot_car_logger.addHandler(sh)
    print "Done setting up logging"

#################################################################

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
FILES_FOLDER = os.path.join(BASEDIR, 'files')

DATABASE_NAME = "mongo_knuddy"

DATASET_NAMES = ["cell_data", "internet_users", "sugar_data"]
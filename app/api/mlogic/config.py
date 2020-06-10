import os

N = 200
RANDOM_STATE = 42
TEST_SIZE = 0.1
MAX_DEPTH = 8

DROP_NA_COLUMN_LIST = ['Tax Liens', 'Bankruptcies', 'Maximum Open Credit', 'Years in current job']
FEATURES_LABEL_ENCODER_COLUMN_LIST = ['Term', 'Home Ownership', 'Purpose']
FEATURES_CATEGORICAL_LIST = ['Number of Open Accounts', 'Number of Credit Problems', 'Bankruptcies', 'Tax Liens']
NUMERIC_COLUMN_IMPUTE_LIST = ['Credit Score', 'Annual Income']


DEPLOY_DROP_COLUMN_LIST = ["id", "first_name", "last_name", "age", "gender"]
DEPLOY_FEATURES_LABEL_ENCODER_COLUMN_LIST = ['term', 'home_ownership', 'purpose']


PROJECT_DIR = os.path.dirname(__file__)
OBJECTS_SAVE_PATH = os.path.join(PROJECT_DIR, 'Pickle_Objects')

LABEL_ENCODER_LOAN_STATUS = os.path.join(OBJECTS_SAVE_PATH, 'le_loan_status.pickle')
LABEL_ENCODER_TERM = os.path.join(OBJECTS_SAVE_PATH, 'le_term.pickle')
LABEL_ENCODER_HOME_OWNERSHIP = os.path.join(OBJECTS_SAVE_PATH, 'le_home_ownership.pickle')
LABEL_ENCODER_PURPOSE = os.path.join(OBJECTS_SAVE_PATH, 'le_purpose.pickle')

ORDINAL_ENCODER_YOJ = os.path.join(OBJECTS_SAVE_PATH, 'oe_years_job.pickle')

LOAN_STATUS_MAPPER = {0: 'Reject', 1: 'Approve'}

SELECTED_COLUMNS = os.path.join(OBJECTS_SAVE_PATH, 'selected_columns.pickle')

MODEL = os.path.join(OBJECTS_SAVE_PATH, 'model_randomforestclassifier.pickle')

# import pickle

# # open a file, where you stored the pickled data
# file = open(SELECTED_COLUMNS, 'rb')

# # dump information to that file
# data = pickle.load(file)

# # close the file
# file.close()

# print(data)
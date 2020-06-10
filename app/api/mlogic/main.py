from pipeline import Pipeline
from config import *
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = pd.read_csv("/media/gagandeep/2E92405C92402AA3/Work/Codes/PythonCodes/Bank-Loan-App/BankLoanApp/Analysis/credit_train.csv")

pipeline = Pipeline(data=data, target='Loan Status', test_size=TEST_SIZE, 
                    model=RandomForestClassifier(n_estimators=N, random_state=RANDOM_STATE, max_depth=MAX_DEPTH))
pipeline.fit(predict_flag=True, eval_flag=True)

#pipeline.predict()
#pipeline.evaluation()
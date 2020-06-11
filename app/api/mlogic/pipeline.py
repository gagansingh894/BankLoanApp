from config import *
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import Lasso
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
# from imblearn.under_sampling import RepeatedEditedNearestNeighbours
import pickle
from tqdm import tqdm

class Pipeline(object):

    def __init__(self, data, target, test_size, model, random_state=RANDOM_STATE):
        self.data = data
        self.target = target
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.colist = None
        self.random_state = random_state
        self.test_size = test_size
        self.dropna_col_list= DROP_NA_COLUMN_LIST
        self.features_le_col_list= FEATURES_LABEL_ENCODER_COLUMN_LIST
        self.features_cat_list = FEATURES_CATEGORICAL_LIST
        self.numeric_impute_list = NUMERIC_COLUMN_IMPUTE_LIST
        self.le_loan_status = LabelEncoder()
        self.le_term = LabelEncoder()
        self.le_home_ownership = LabelEncoder()
        self.le_purpose = LabelEncoder()
        self.le_list = [self.le_term, self.le_home_ownership, self.le_purpose]
        self.oe_years_job = OrdinalEncoder()
        self.selected_columns = None
        self.model = model
        self.undersampler = RepeatedEditedNearestNeighbours()
        self.predictions = None
        self.obj_savepath = OBJECTS_SAVE_PATH

    def drop_data(self):
        print("Drop NA values")
        for col in self.dropna_col_list:
            self.data = self.data[self.data[col].isna() == False]        

        self.data.drop(['Loan ID', 'Customer ID', 'Months since last delinquent'], axis=1, inplace=True)
        return self
    
    def split_data(self):
        print("Train Test Split")
        self.y = self.data[self.target]
        self.data = self.data.drop('Loan Status', axis=1)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data, self.y, test_size=self.test_size, random_state=self.random_state, stratify=self.y)
        self.X_train = self.X_train.reset_index().drop('index', axis=1)
        self.X_test = self.X_test.reset_index().drop('index', axis=1)
        self.colist = self.X_train.columns
        return self

    def prepare_train_data(self):
        print('Transforming Train Data')
        self.y_train = self.le_loan_status.fit_transform(self.y_train)
        
        for le,col in zip(self.le_list,self.features_le_col_list):
            self.X_train[col] = le.fit_transform(self.X_train[col]).astype(int).astype(str)
        
        self.X_train['Years in current job'] = self.oe_years_job.fit_transform(self.X_train['Years in current job'].values.reshape(-1,1)).astype(int).astype(str)
        
        for col in self.features_cat_list:
            self.X_train[col] = self.X_train[col].astype(int).astype(str)
        
        for col in self.numeric_impute_list:
            self.X_train[col] = self.X_train[col].fillna(self.X_train[col].median())
    
    def feature_selection(self):
        print('Feature Selection')
        self.sel_ = SelectFromModel(Lasso(alpha=0.005, random_state=self.random_state))
        self.sel_.fit(self.X_train, self.y_train)
        self.selected_columns = self.colist[self.sel_.get_support()]
        self.X_train = self.X_train[self.selected_columns]
        return self
    
    def prepare_test_data(self):
        print('Transforming Test Data')
        self.y_test = self.le_loan_status.transform(self.y_test)
        
        self.X_test = self.X_test[self.selected_columns]

        for le,col in zip(self.le_list,self.features_le_col_list):
            self.X_test[col] = le.transform(self.X_test[col]).astype(int).astype(str)        

        self.X_test['Years in current job'] = self.oe_years_job.transform(self.X_test['Years in current job'].values.reshape(-1,1)).astype(int).astype(str)
        
        self.X_test['Number of Open Accounts'] = self.X_test['Number of Open Accounts'].astype(int).astype(str)
        
        self.X_test['Credit Score'] = self.X_test[col].fillna(self.X_test['Credit Score'].median())
        return self
    
    # def undersample_data(self):
    #     print('Applying undersampling')
    #     self.X_train, self.y_train = self.undersampler.fit_resample(self.X_train, self.y_train)

    def fit(self, predict_flag=False, eval_flag=False):
        self.drop_data()
        self.split_data()
        self.prepare_train_data()
        self.feature_selection()
        self.prepare_test_data()
        # self.undersample_data()
        self.model.fit(self.X_train, self.y_train)
        self.save_objects()

        if predict_flag:
            self.predict()
        
        if eval_flag:
            self.evaluation()
        return self
    
    def save_objects(self):
        print("Pickle and Save")
        self.objs = [self.le_loan_status, self.le_term, self.le_home_ownership, self.le_purpose,
                     self.oe_years_job, self.selected_columns, self.model]
        self.objs_name = ["le_loan_status.pickle", "le_term.pickle", "le_home_ownership.pickle", "le_purpose.pickle",
                        "oe_years_job.pickle", "selected_columns.pickle", "model_randomforestclassifier.pickle"]

        for i in tqdm(range(len(self.objs))):
            self.pickle_out = open(os.path.join(self.obj_savepath, self.objs_name[i]), 'wb')
            pickle.dump(self.objs[i], self.pickle_out)
            self.pickle_out.close()


    def predict(self):
        print('Making Predictions')        
        self.predictions = self.model.predict(self.X_test)
        print()
    
    def evaluation(self):
        print('******************** EVALUATION REPORT *****************************************')
        print("Accuracy Score: {}".format(accuracy_score(self.y_test, self.predictions)))
        print("Precision Score: {}".format(precision_score(self.y_test, self.predictions)))
        print("Recall Score: {}".format(recall_score(self.y_test, self.predictions)))
        print("F1 Score: {}".format(f1_score(self.y_test, self.predictions)))
        print()
        print(confusion_matrix(self.y_test, self.predictions))

if __name__ == '__main__':
    pass
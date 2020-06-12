import pickle
import pandas as pd
from config import *

class MLAPP:
    def __init__(self):
        self.obj_list = []

        for obj in [LABEL_ENCODER_TERM, LABEL_ENCODER_HOME_OWNERSHIP, LABEL_ENCODER_PURPOSE, ORDINAL_ENCODER_YOJ,  
                    SELECTED_COLUMNS, MODEL]:
            
            self.file = open(obj, 'rb')
            self.obj_list.append(pickle.load(self.file))
            self.file.close()
        
        del self.file
        
        #Set the objects        
        self.le_list = [self.obj_list[0], self.obj_list[1], self.obj_list[2]]
        self.oe_years_job = self.obj_list[3]
        self.selected_columns = self.obj_list[4]
        self.model = self.obj_list[5]
        self.drop_column_list = DEPLOY_DROP_COLUMN_LIST
        self.features_le_col_list = DEPLOY_FEATURES_LABEL_ENCODER_COLUMN_LIST
        self.loan_status_mapper = LOAN_STATUS_MAPPER   

    def predict(self,data):
        self.X_test = pd.DataFrame(data)
        self.X_test.drop(self.drop_column_list, axis=1, inplace=True)

        for le,col in zip(self.le_list,self.features_le_col_list):
            self.X_test[col] = le.transform(self.X_test[col]).astype(int).astype(str)        

        self.X_test['year_in_current_job'] = self.oe_years_job.transform(self.X_test['year_in_current_job'].values.reshape(-1,1)).astype(int).astype(str)
        
        self.X_test['num_open_acc'] = self.X_test['num_open_acc'].astype(int).astype(str)

        self.X_test['credit_score'] = self.X_test['credit_score'].fillna(self.X_test[col].median())
        self.prediction = pd.Series(self.model.predict(self.X_test)).map(self.loan_status_mapper)[0]
        # self.res = {'result':self.predictions.map(self.loan_status_mapper)[0]}
        return self.prediction





# import pickle
# import pandas as pd
# from pipeline import Pipeline
# from config import *

# class MLAPP(Pipeline):
#     def __init__(self):
#         self.obj_list = []

#         for obj in [LABEL_ENCODER_TERM, LABEL_ENCODER_HOME_OWNERSHIP, LABEL_ENCODER_PURPOSE, ORDINAL_ENCODER_YOJ,  
#                     SELECTED_COLUMNS, MODEL]:
            
#             self.file = open(obj, 'rb')
#             self.obj_list.append(pickle.load(self.file))
#             self.file.close()
        
#         del self.file
        
#         #Set the objects        
#         Pipeline.le_list = [self.obj_list[0], self.obj_list[1], self.obj_list[2]]
#         Pipeline.oe_years_job = self.obj_list[3]
#         Pipeline.selected_columns = self.obj_list[4]
#         Pipeline.model = self.obj_list[5]
#         self.drop_column_list = DEPLOY_DROP_COLUMN_LIST
#         Pipeline.features_le_col_list = DEPLOY_FEATURES_LABEL_ENCODER_COLUMN_LIST
#         self.loan_status_mapper = LOAN_STATUS_MAPPER   

#     def predict(self,data):
#         Pipeline.X_test = pd.DataFrame(data)
#         Pipeline.X_test.drop(self.drop_column_list, axis=1, inplace=True)

#         for le,col in zip(Pipeline.le_list,Pipeline.features_le_col_list):
#             Pipeline.X_test[col] = le.transform(Pipeline.X_test[col]).astype(int).astype(str)        

#         Pipeline.X_test['year_in_current_job'] = Pipeline.oe_years_job.transform(Pipeline.X_test['year_in_current_job'].values.reshape(-1,1)).astype(int).astype(str)
        
#         Pipeline.X_test['num_open_acc'] = Pipeline.X_test['num_open_acc'].astype(int).astype(str)

#         Pipeline.X_test['credit_score'] = Pipeline.X_test['credit_score'].fillna(Pipeline.X_test[col].median())
#         self.prediction = pd.Series(Pipeline.model.predict(Pipeline.X_test)).map(self.loan_status_mapper)[0]
#         # self.res = {'result':self.predictions.map(self.loan_status_mapper)[0]}
#         return self.prediction

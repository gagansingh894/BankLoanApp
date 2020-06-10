import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'mlogic'))
import deploy

print('Loading in the model...')
ml = deploy.MLAPP()
print('Success')

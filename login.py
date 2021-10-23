import pandas as pd
import os
from Resource.resourcePath import getResourcePath

df=pd.read_csv(os.path.join(getResourcePath(),"Resource/cred.csv"))
def checkUsername(un):
    for x in df['Username']:
        if un==x:
            return True
        else:
            return False
    return

def checkPassword(p):
    for x in df['Password']:
        if p==x:
            return True
        else:
            return False
    return
    

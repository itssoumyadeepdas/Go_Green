import pandas as pd
import os
from Resource.resourcePath import getResourcePath

df=pd.read_csv("os.path.join(getResourcePath(),"Resource/cred.csv"))
def checkUsername(un):
    for x in df['Username']:
        if un==x:
            con=True
            break
        else:
            con=False
    return con

def checkPassword(p):
    for x in df['Password']:
        if p==x:
            con=True
            break
        else:
            con=False
    return con
    

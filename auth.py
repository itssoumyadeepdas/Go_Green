import pandas as pd

df=pd.read_csv("Resource/cred.csv")
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
    

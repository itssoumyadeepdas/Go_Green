import pandas as pd
import os
from Resource.resourcePath import getResourcePath
t=pd.read_csv(os.path.join(getResourcePath(),"Resource/tips.csv"))
v=pd.read_csv(os.path.join(getResourcePath(),"Resource/link.csv"))
def getLink(item):
    d=v.loc[v['Item']==item]
    return (d.iloc[0,1])

def getTips(cat):
    tip=t.loc[t['Category']==cat]
    tip=tip['Remarks']
    tip=tip.str.split("-")
    tip=list(tip)
    tip=sum(tip,[])
    tipStr=('<br>'.join(tip))
    return (tipStr)

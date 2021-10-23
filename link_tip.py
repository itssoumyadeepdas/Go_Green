import pandas as pd
from pathlib import path
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Resource'))
import Resource.link
t=pd.read_csv("tfile")
v=pd.read_csv("https://github.com/sagarkumar3105/Go_Green/blob/907dd8eefaf8e46eb4c5b830fda5b807cdf6154c/Resource/link.csv")
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

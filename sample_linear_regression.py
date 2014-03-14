#!/usr/bin/python

import string
import warnings
import numpy as np  
from sklearn.pls import PLSRegression as pls 

alphas = string.ascii_lowercase

def converttoones (data, alphas,training=False):
        indexed = [0] * 26
        for i in list(data):
                if training:
                        indexed[list(alphas).index(i)] = list(alphas).index(i)+1
                else:
                        indexed[list(alphas).index(i)] = 1 
        return indexed

linguistics=converttoones('linguistics', alphas,True)
linguistic=converttoones('linguistic', alphas)
lgstx=converttoones('lgstx', alphas,True)
lgstk=converttoones('lgstk', alphas)
hardwood=converttoones('hardwood', alphas,True)
hdwd=converttoones('hdwd', alphas)
will=converttoones('will', alphas,True)
vil=converttoones('vil', alphas)
love=converttoones('love', alphas,True)
lv=converttoones('lv', alphas)
kiss=converttoones('kiss', alphas,True)
ks=converttoones('ks', alphas)
hard=converttoones('hard', alphas,True)
hd=converttoones('hd', alphas)
road=converttoones('road', alphas,True)
rd=converttoones('rd', alphas)
computer=converttoones('computer', alphas,True)
cmptr=converttoones('cmptr', alphas)
diehard=converttoones('diehard', alphas,True)
dihd=converttoones('dihd', alphas)
school=converttoones('school', alphas,True)
schl=converttoones('schl', alphas)
peacock = converttoones('peacock', alphas,True)
pck = converttoones('pck', alphas)
football = converttoones('football', alphas,True)
ftbl = converttoones('ftbl', alphas)
jungle = converttoones('jungle', alphas,True)
jngl = converttoones('jngl', alphas)
master = converttoones('master', alphas,True)
mstr = converttoones('mstr', alphas)
quiz = converttoones('quiz', alphas,True)
qz = converttoones('qz', alphas)
you  = converttoones('you', alphas,True)
u  = converttoones('u', alphas)
catestropphy  = converttoones('catestropphy', alphas,True)
ktstrphy  = converttoones('ktstrphy', alphas)
a = converttoones('a', alphas,True)
aa= converttoones('a', alphas)
o = converttoones('o', alphas,True)
oo = converttoones('o', alphas)

e = converttoones('e', alphas,True)
ee = converttoones('e', alphas)

X=np.array((linguistics,linguistic,hardwood,will,love,kiss,hard,road,computer,diehard,school,peacock,football,jungle,master,quiz,you,catestropphy,a,o,e))
Y=np.array((lgstx,lgstk,hdwd,vil,lv,ks,hd,rd,cmptr,dihd,schl,pck,ftbl,jngl,mstr,qz,u,ktstrphy,aa,oo,ee))

mypls = pls(n_components=3).fit(X=X, Y=Y)

testWord = converttoones('we',alphas)
print zip(alphas,np.round(np.array(testWord) * np.array(mypls.predict(catestropphy)),1))

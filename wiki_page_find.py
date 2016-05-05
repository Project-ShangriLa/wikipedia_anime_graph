#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
与えた声優の名前でwikipediaのページがあるか確認する。
井上和彦 (声優)のように(声優)が必要な人を抽出。
"""

import numpy as np
import requests
import urllib
import sys
from wiki_relevance_module import wiki_rel_mod
from wiki_relevance_module import gethtml
#-------------------------------------------------------#
def set_vc(argv):
    fname="cv_list.dat"
    fname=argv
    try :
        #句読点で区切られた名前をlistに格納
        for line in open(fname, 'r'):
            namelist = line[:-1].split(',')
        print(namelist)
    except :
        print("cannot be opend")
        exit(-1)
    return namelist
#-------------------------------------------------------#
if __name__ == '__main__' :
    if len(sys.argv) != 2 :
        print("argument error")
        exit(1)

    name=[]
    name=set_vc(sys.argv[1])
    matlen=len(name)
    rel=np.zeros([matlen,matlen], dtype=float)

    for i in range(matlen):
        tmp_rel=gethtml(name[i])
        if tmp_rel == -1 : #エラーがあれば表示
            print("error name:",name[i])
        else:
            print("ok:",name[i])

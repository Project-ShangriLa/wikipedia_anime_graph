#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
多次元尺度構成法(MDS)に渡す行列を生成する
"""

def set_vc():
    name=["悠木碧","斎藤千和","喜多村英梨","水橋かおり","野中藍","加藤英美里"]
    return name


def make_matrix():
    import numpy as np
    from wiki_relevance_module import wiki_rel_mod

    name=[]
    name=set_vc()
    matlen=len(name)
    rel=np.zeros([matlen,matlen])

    for i in range(matlen-1):
        for j in range(i,matlen-1):
            rel[i][j+1]=wiki_rel_mod(name[i],name[j+1])
            rel[j+1][i]=rel[i][j+1] #対象行列にする
    print("matrix:")
    print(rel)
    return rel


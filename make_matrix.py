#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
多次元尺度構成法(MDS)に渡す行列を生成する
"""

def set_vc():
    fname="cv_list.dat"
    try :
        #句読点で区切られた名前をlistに格納
        for line in open(fname, 'r'):
            namelist = line[:-1].split(',')
        print(namelist)
    except :
        print("cannot be opend")
        exit(-1)
    #name=["悠木碧","斎藤千和","喜多村英梨","水橋かおり","野中藍","加藤英美里"]
    #name=["神谷浩史","斎藤千和","堀江由衣","櫻井孝宏","坂本真綾","沢城みゆき","花澤香菜","喜多村英梨","井口裕香"]
    return namelist


def make_matrix():
    import numpy as np
    from wiki_relevance_module import wiki_rel_mod

    name=[]
    name=set_vc()
    matlen=len(name)
    rel=np.zeros([matlen,matlen], dtype=float)

    for i in range(matlen-1):
        for j in range(i,matlen-1):
            tmp_rel=wiki_rel_mod(name[i],name[j+1])
            if tmp_rel == -1 : #エラーが帰ってきたらスキップ
                print("error name:",name[i],name[j+1])
            else :
                rel[i][j+1] = tmp_rel
                rel[j+1][i] = rel[i][j+1] #対象行列にする
    print("matrix:")
    print(rel)
    return rel


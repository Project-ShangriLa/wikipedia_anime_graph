# -*- coding: utf-8 -*-
"""
wiki_relevance.pyをモジュール化
2つのwikipedia のページの関連度度を求める
一致リンクが多いほど関連度が高くなる
"""

import sys
import requests
import urllib
import math
# 本文取得
def gethtml(argv):
    title = urllib.parse.quote_plus(argv)
    url='http://ja.wikipedia.org/w/api.php?format=xml&action=query&prop=revisions&titles='+title+'&rvprop=content'
    r = requests.get(url)
    return r.text

# linesに本文htmlを1行毎にリストに格納
def linesget(get):
    lines=[]
    tmp=""
    st=""
    for tmp in get:
        st=st+tmp
        if tmp == "\n" :
            lines.append(st)
            st=""
    return lines

#リンクをリストに格納
def getlink(page):
    flag=0
    tmp = ""
    words=[]
    for line in page :
        if line == "[" : flag = 1
        if flag == 1 and line != "[" : flag = 2
        if line == "]" : flag = 3
        if flag == 3 and line != "]" : flag = 4

        if flag == 2 :
            tmp = tmp + line
        if flag == 3 :
            words.append(tmp)
            tmp=""
    return words

#リンク一致度計算
def cal_relevance(link1,link2):
    list_set1 = set(link1)
    list_set2 = set(link2)

    # #Jaccard係数
    upper = len(list_set1 & list_set2)
    bottom = len(list_set1 | list_set2)
    #重複ワード単語は無視する

    # #Dice係数
    # upper = 2*len(list_set1 & list_set2)
    # bottom = len(list_set1) + len( list_set2)

    # #Simpson係数
    # upper = len(list_set1 & list_set2)
    # bottom = min (len(list_set1) , len( list_set2))

    # rel = len(matched_list) /(len(link1) + len(link2))
    # print(len(link1),len(link2))

    if bottom != 0 :
        return float(upper) / bottom
    else :
        return 0
    
#対数変換
def cal_log(rel):
    if rel != 0 :
        return math.log10(1/rel)
    else:
        return 0

#-------main--------------------
def wiki_rel_mod(name1,name2):
    lines=[]
    infolines=[]
    
    #本文html取得
    page1=gethtml(name1)
    page2=gethtml(name2)

    #リンク取得
    linklist1=getlink(page1)
    linklist2=getlink(page2)

    #リンク一致度計算(類似度)
    rel=cal_relevance(linklist1,linklist2)
    
    #リンク一致度計算(距離)
    logrel=cal_log(rel)
    # print(logrel)
    return logrel

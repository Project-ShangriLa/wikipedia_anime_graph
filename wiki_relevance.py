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

#リンクの数の最小値
LimLink=200

#-------------------------------------------------------#
# 本文取得
def gethtml(argv):
    title = urllib.parse.quote_plus(argv)
    url='http://ja.wikipedia.org/w/api.php?format=xml&action=query&prop=revisions&titles='+title+'&rvprop=content'
    r = requests.get(url)
    #wikipediaのページが取ってこれなければエラーを返す
    if "missing" in r.text :
        return -1
    else:
        return r.text
#-------------------------------------------------------#
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
#-------------------------------------------------------#
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
#-------------------------------------------------------#
#出演作品のページ以前を切り取る
def cut_lines(lines):
    applines=""
    flag=0
    for line in lines :
        if '== 出演作品 ==' in line : flag=1
        if flag==1 :
            applines += line
        if "=== OVA ===" in line : break

    return applines
#-------------------------------------------------------#
#リンクの数が少なすぎるとエラー
def linkerror(linklist):
    if len(linklist) < LimLink :
        return -1
    else :
        return 0
#-------------------------------------------------------#
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
#-------------------------------------------------------#

#-------main--------------------
def wiki_rel_mod(name1,name2,flag):
    #引数処理
    # if len(sys.argv) != 3 :
    #     print("arguments error")
    #     exit(0)

    #本文html取得
    page1=gethtml(name1)
    if page1 == -1 : return -1
    page2=gethtml(name2)
    if page2 == -1 : return -1

    if flag == "a":
        #リンク取得を出演アニメに絞る
        lines1=linesget(page1)
        lines2=linesget(page2)
        applines1=cut_lines(lines1)
        applines2=cut_lines(lines2)
    else:
        applines1=page1
        applines2=page2

    #リンク取得
    linklist1=getlink(applines1)
    linklist2=getlink(applines2)

    #リンクの数が少なすぎるとエラー
    errorflag=linkerror(linklist1)
    errorflag=linkerror(linklist2)

    if errorflag == -1 :
        print("link num small")
        return -1

    #リンク一致度計算(類似度)
    rel=cal_relevance(linklist1,linklist2)

    #リンク一致度計算(距離)
    logrel=cal_log(rel)

    return logrel
#-------main--------------------
if __name__ == '__main__' :
    flag="a"
    logrel=wiki_rel_mod(sys.argv[-2],sys.argv[-1],flag)
    print(logrel)

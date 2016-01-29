#2つのwikipedia のページの関連度度を求める
#一致リンクが多いほど関連度が高くなる
#抽出するリンクを出演アニメから取ってくるパターン
# -*- coding: utf-8 -*-
import sys
import requests
import urllib
import numpy as np

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


#リンク類似度計算
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

    if bottom != 0 :
        rel= float(upper) / bottom
    else :
        rel=0
    return rel
#-------main--------------------
if __name__ == '__main__' :
    #引数処理
    if len(sys.argv) != 3 :
        print("arguments error")
        exit(0)
    #本文html取得
    page1=gethtml(sys.argv[1])
    page2=gethtml(sys.argv[2])
    lines1=[]
    lines2=[]
    lines1=linesget(page1)
    lines2=linesget(page2)

    #出演作品のページ以前を切り取る
    applines1=[]
    applines1=cut_lines(lines1)
    applines2=[]
    applines2=cut_lines(lines2)

    #リンク取得
    linklist1=getlink(applines1)
    linklist2=getlink(applines2)

    #リンク一致度計算
    rel=cal_relevance(linklist1,linklist2)
    print(rel)
    # print(1.0 - rel)

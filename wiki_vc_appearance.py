# -*- coding: utf-8 -*-
"""
入力声優の出演作品一覧を出力
"""

import sys
import requests
import urllib
import numpy as np
import re

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
    applines=[]
    flag=0
    for line in lines :
        if '== 出演作品 ==' in line : flag=1
        if flag==1 :
            applines.append(line)
    return applines

#初出演年代を特定
def get_debut(lines):
    line=""
    flag=0
    num=1990
    tmp=""

    for line in lines :
        if '=== テレビアニメ ===' in line : flag=1
        if (flag == 1) and ('年' in line):
            tmp=line
            break
    while True:
        stryear = str("'''"+str(num)+"年'''")
        if stryear in tmp :
            year = num
            break
        num+=1
    return year

#-------main--------------------
if __name__ == '__main__' :
    #引数処理
    if len(sys.argv) != 2 :
        print("arguments error")
        exit(0)
    #本文html取得
    page=gethtml(sys.argv[1])
    lines=[]
    lines=linesget(page)

    for line in lines :
        print(line )
    #出演作品のページ以前を切り取る
    applines=[]
    applines=cut_lines(lines)

    apps=[]
    for line in applines :
        if '*' in line:
            apps+=re.findall('\[+(.*?.)\]+',line)
            # apps.append(match)
        if "=== OVA ===" in line: break
        if "===" in line: break

    #表示
    for app in apps :
        print(app)

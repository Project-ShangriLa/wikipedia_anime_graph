#wikipedia の声優ページから活躍年代を推定
# -*- coding: utf-8 -*-
import sys
import requests
import urllib
import numpy as np
import re
#-------------------------------------------------------#
# 本文取得
def gethtml(argv):
    title = urllib.parse.quote_plus(argv)
    url='http://ja.wikipedia.org/w/api.php?format=xml&action=query&prop=revisions&titles='+title+'&rvprop=content'
    r = requests.get(url)
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
#出演作品のページ以前を切り取る
def cut_lines(lines):
    applines=[]
    flag=0
    for line in lines :
        if '== 出演作品 ==' in line : flag=1
        if flag==1 :
            applines.append(line)
    return applines

#-------------------------------------------------------#
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
#-------------------------------------------------------#
def main():
    #引数処理
    if len(sys.argv) != 2 :
        print("arguments error")
        exit(0)

  #本文html取得
    page=gethtml(sys.argv[1])
    lines=linesget(page)
    #出演作品のページ以前を切り取る
    applines=cut_lines(lines)

    cnt=np.zeros(50)
    year_cnt=np.zeros(50)
    i=-1
    for line in applines :
        if '*' in line:
            if "'''" in line: #メインキャラクターであれば3ポイント
                cnt[i]+=3
            else: #そうでなければ1ポイント
                cnt[i]+=1
        else:
            if "年" in line:
                i+=1
                match = re.findall(r'[0-9]+', line)
                year_cnt[i]=match[0]
        if "=== OVA ===" in line: break

    #表示
    for value in range(i):
        print(year_cnt[value],cnt[value])

#-------main--------------------#
if __name__ == '__main__' :
    main()  


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
多次元尺度構成法
Multidimensional Scaling; MDS
"""
import numpy as np
import matplotlib.pyplot as plt
from make_matrix import make_matrix
import sys


#-------------------------------------------------------#
def make_mtrx(fname):
    # データ読み込み
    #行列D
    D=make_matrix(fname)
    N = len(D)

    # 距離の2乗の行列 (arrayだと要素同士の掛け算になる)
    S = D * D

    # 中心化行列
    one = np.eye(N) - np.ones((N,N))/N

    # ヤング・ハウスホルダー変換
    P = - 1.0/2 * one * S * one

    # スペクトル分解
    w,v = np.linalg.eig(P)
    ind = np.argsort(w)
    x1 = ind[-1] # 1番
    x2 = ind[-2] # 2番

    # 標準されたデータの固有値が求められているので標準偏差を掛けて可視化
    s = P.std(axis=0)
    w1 = s[x1]
    w2 = s[x2]
    return w1,w2,x1,x2,v,N
#-------------------------------------------------------#

#-------------------------------------------------------#
def print_coordinates(w1,w2,x1,x2,v,N):
    #各点の表示
    for i in range(N):
        print(i,w1*v[i,x1],w2*v[i,x2])
#-------------------------------------------------------#


#-------------------------------------------------------#
def make_graph(w1,w2,x1,x2,v,N):
    #グラフ描写
    for i in range(N):
        plt.plot(w1*v[i,x1],w2*v[i,x2],'b.')
        #ラベル付け 
        plt.text(w1*v[i,x1],w2*v[i,x2],str(i))

    #描写
    # plt.draw()
    # plt.show()
    print("save glaph")
    #グラフ保存
    filename = "figure/mds_fig.png"
    plt.savefig(filename)
#-------------------------------------------------------#


#-------------------------------------------------------#
#プロット点保存
def save_data(w1,w2,x1,x2,v,N,wfname):
    print("save ",wfname)

    f = open(wfname,'w')
    for i in range(N):
        f.writelines([str(w1*v[i,x1]),",",str(w2*v[i,x2]),"\n"])
    f.close()
#-------------------------------------------------------#p


#-------------------------------------------------------#
def cal_mds(param):
    rfname = "./data/cv_list.dat"
    wfname = "./data/mds_plot.dat"
    w1,w2,x1,x2,v,N = make_mtrx(rfname)
    print_coordinates(w1,w2,x1,x2,v,N)
    if "-m" in param :
        make_graph(w1,w2,x1,x2,v,N)
    if "-s" in param :
        save_data(w1,w2,x1,x2,v,N,wfname)

#-------------------------------------------------------#
if __name__ == '__main__' :
    cal_mds(sys.argv)

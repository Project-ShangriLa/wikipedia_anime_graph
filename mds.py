#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
多次元尺度構成法
Multidimensional Scaling; MDS
"""
import numpy as np
import matplotlib.pyplot as plt
from make_matrix import make_matrix

# データ読み込み
#行列D
D=make_matrix()
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

#各点の表示
for i in range(N):
    print(i,w1*v[i,x1],w2*v[i,x2])

#グラフ描写
for i in range(N):
    plt.plot(w1*v[i,x1],w2*v[i,x2],'b.')
    #ラベル付け 
    plt.text(w1*v[i,x1],w2*v[i,x2],str(i))
#描写
# plt.draw()
# plt.show()
#保存  
filename = "figure/output.png"
plt.savefig(filename)

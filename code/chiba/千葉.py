# coding: utf-8

# SC_sim_最適化.py

# data1=(data1[:,0]) #町丁目のFID
# data1=(data1[:,1]) #町丁目のcode
# data1=(data1[:,2]) #町丁目の人口数
# data1=(data1[:,3]) #町丁目中心点のX_utm座標
# data1=(data1[:,4]) #町丁目中心点のY_utm座標

# store1=(store1[:,0]) #店舗のFID
# store1=(store1[:,1]) #店舗のX_utm座標
# store1=(store1[:,2]) #店舗のY_utm座標
# store1=(store1[:,3]) #店舗の面積（㎡）
# store1=(store1[:,4]) #店舗のテナント得点

path = r'F:\サイゼリヤ2019\0129\pyworks\kazo\千葉'
import sys
import numpy as np
import math
np.set_printoptions(suppress=True) #指数表示にしない


#-------------------------------------
data1=np.loadtxt('data11.csv',comments='OBJECTID',delimiter=',',dtype='float')
store1=np.loadtxt('store11.csv',comments='OBJECTID',delimiter=',',dtype='float')


print(data1)
print(store1)
# print(data2)

n1=3541 # 町丁目数
m1=34 # 店舗数

print u'町丁目数=',
print(n1)
print u"店舗数=",
print(m1)
print("") 

from numpy import *

dist1=np.zeros((n1,m1))
memb1=np.zeros((n1,m1))
memb2=np.zeros((n1,m1))
memb3=np.zeros((n1,m1))
smem=np.zeros(n1)
ssmem=np.zeros((m1,2))
differ=np.zeros(m1)
attract=np.zeros(m1)
#ctattract=np.zeros(n2)
#popu=np.zeros(n2)
stpopu=np.zeros(m1)
   

#------------直線距離の計算-------------------------

for j in range(0, m1, 1):
    for i in range(0, n1, 1):
        dist1[i,j]=np.sqrt((data1[i,3]-store1[j,2])**2+(data1[i,4]-store1[j,3])**2)

#-------------------------------------------------
import codecs
fin=codecs.open('text1.csv', 'r', 'shift_jis')
fout=codecs.open('result88.csv', 'w', 'shift_jis')
for line in fin:
    fout.write(line)


#---------結果出力-----------------------

np.savetxt('result81.csv', dist1, fmt='%.01f', delimiter=',')
















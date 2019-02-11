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

path = r'F:\サイゼリヤ2019\0129\pyworks\kazo'
import sys
import numpy as np
import math
np.set_printoptions(suppress=True) #指数表示にしない


#-------------------------------------
data1=np.loadtxt('data11.csv',comments='OBJECTID',delimiter=',',dtype='float')
store1=np.loadtxt('store11.csv',comments='OBJECTID',delimiter=',',dtype='float')


# print(data1)
# print(store1)
# print(data2)

n1=436 # 町丁目数
m1=58 # 店舗数＝9

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

#------------総人口の算出---------------------------

total_population=0 #研究地域の総人口
for i in range(0, n1, 1):
    total_population=total_population+data1[i,2]

# print(int(total_population))    

#------------直線距離の計算-------------------------

for j in range(0, m1, 1):
    for i in range(0, n1, 1):
        dist1[i,j]=np.sqrt((data1[i,3]-store1[j,1])**2+(data1[i,4]-store1[j,2])**2)

# print(data1[0,3])
#print(store1[0,4])
# print(data1[0,4])
# print(store1[0,2])

#print(dist1[0,0])

#----------------魅力度計算-------------------------

for j in range(0, m1, 1):
#    attract[j]=sqrt(store1[j,3]/1000)
#    attract[j]=(store1[j,3]/1000)
    attract[j]=(store1[j,4])

print u'店舗魅力度='
print(attract)
print("")



#----------------拡張指数モデル----------------------

#--------パラメータα、β------------
a1=1  # FG参加率
b1=0.05 # FG参加率の距離逓減率
c=1 # 店舗魅力度の乗数

print u'パラメータ（参加率、距離逓減率、魅力度の乗数）='
print(a1,b1,c)
print("")


#--------------分子と分母の計算-------------------

for j in range(0, m1, 1):
    for i in range(0, n1, 1):        
#        memb1[i,j]=a1*data1[i,2]*np.exp(-b1*dist1[i,j]/100)*attract[j]**c*np.exp(-b1*dist1[i,j]/100) #拡張SIM 
        memb1[i,j]=a1*data1[i,2]*attract[j]**c*np.exp(-b1*dist1[i,j]/100) #SIM
        memb2[i,j]=attract[j]**c*np.exp(-b1*dist1[i,j]/100) #Para1
# print(memb1)

#----------------分母の合計-------------------------------

for i in range(0, n1, 1):    
    sum1=0
    for j in range(0, m1, 1):
        sum1=sum1+memb2[i,j]

    if sum1<=0:
        smem[i]=0.0001
    else:
        smem[i]=sum1

# print(smem)

#-----------------分子/分母の合計（買物流動_memb3）-----------------------

for i in range(0, n1, 1):
    for j in range(0, m1, 1):
        memb3[i,j]=memb1[i,j]/smem[i]
        
#-----------------SCの商圏人口ssmem[j,0]--------------------------------------
    
for j in range(0, m1, 1):
    sum2=0
    for i in range(0, n1, 1):       
        sum2=sum2+(memb1[i,j]/smem[i])
    ssmem[j,0]=int(sum2)
    
for j in range(0, m1, 1):
#    print(data2[j,0],data2[j,2])
    ssmem[j,1]=int(attract[j])

print u'予測結果='    
print(ssmem)
print("")

#-----------------商圏総人口totalTAP--------------------------------------

totalTAP=0 #商圏総人口
for j in range(0, m1, 1):
    totalTAP=totalTAP+ssmem[j,0]

print u'SCの商圏総人口=',
print(int(totalTAP))

print u'研究地域総人口=',
print(int(total_population))

print u'SCの獲得率=',
print(round(totalTAP/total_population,2))


#-------------------------------------------------
import codecs
fin=codecs.open('text1.csv', 'r', 'shift_jis')
fout=codecs.open('result88.csv', 'w', 'shift_jis')
for line in fin:
    fout.write(line)


#---------結果出力-----------------------

np.savetxt('result81.csv', memb3, fmt='%.01f', delimiter=',')
np.savetxt('result82.csv', ssmem, fmt='%.01f', delimiter=',')

#-----------会員数_14店舗-------------------------------------------
fin=codecs.open('result82.csv', 'r', 'utf-8')
out=codecs.open('result88.csv', 'a', 'utf-8')
#out=codecs.open('result9.csv', 'w', 'utf-8')
for line in fin:
    fout.write(line)

#-----------会員数_125mメッシュ中心-------------------------------------------
fin=codecs.open('result81.csv', 'r', 'utf-8')
out=codecs.open('result88.csv', 'a', 'utf-8')
#out=codecs.open('result9.csv', 'w', 'utf-8')
for line in fin:
    fout.write(line)














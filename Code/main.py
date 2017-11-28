# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 21:54:01 2017
call holdem_calc as library
@author: shuyang
"""
import pandas as pd
from pandas import DataFrame
import numpy as np
import holdem_calc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter  

#define file path
file_path = 'C:\\Users\\moliu\\Desktop\\Texas Holdem\\ProbabilityofWinning\\holdem_calc-master\\'
offsuitedpath = file_path + 'off_suited_hands.txt'
suitedpath = file_path + 'suited_hands.txt'

#calculate winning probability of different off suit hands
ohandsList = []
for l in open(offsuitedpath):
    row = [x for x in l.split()]
    if len(row) > 0:
        ohandsList.append(row)

probabilityList = []
for eachHand in shandsList:
    print(eachHand)
    sprobabilityList.append(holdem_calc.calculate(None, False, 200, None, eachHand, False))

#calculate winning probability of different suited hands
shandsList = []
for l in open(suitedpath):
    row = [x for x in l.split()]
    if len(row) > 0:
        shandsList.append(row)
        
sprobabilityList = []
for eachHand in shandsList:
    print(eachHand)
    sprobabilityList.append(holdem_calc.calculate(None, False, 200, None, eachHand, False))

#sort data
ohandsFrame = DataFrame(ohandsList).rename(index=str,columns={0:'hand1',1:'hand2',2:'uhand1',3:'uhand2'})
shandsFrame = DataFrame(shandsList).rename(index=str,columns={0:'hand1',1:'hand2',2:'uhand1',3:'uhand2'})

oprobabilityFrame = DataFrame(probabilityList).rename(index=str,columns={0:'tie',1:'WinningProbability',2:'Opponent'})
sprobabilityFrame = DataFrame(sprobabilityList).rename(index=str,columns={0:'tie',1:'WinningProbability',2:'Opponent'})

oresultFrame = pd.concat([ohandsFrame[['hand1','hand2']],oprobabilityFrame],axis=1)
sresultFrame = pd.concat([shandsFrame[['hand1','hand2']],sprobabilityFrame],axis=1)

result = sresultFrame
handstype = 's'
resultFrame = DataFrame()
for i in range(0,len(result)):
    result['hand1'][i] = result['hand1'][i][0]
    result['hand2'][i] = result['hand2'][i][0]
    result['type'] = handstype
    result['hand'] = result['hand1'] + result['hand2'] + handstype

resultFrame = pd.concat([resultFrame,result])
resultFrame.to_csv(file_path + 'resultFrame.csv')

#analysis
resultFrame = pd.read_csv(file_path + 'resultFrame.csv',index_col=0)

#draw picture 1
plt.figure(figsize=(20,20))
plt.grid(linestyle='--')

plt.xlim(0,180)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylim(0.2,0.9)

plt.plot(pd.Series(sortedresultFrame.index),sortedresultFrame['WinningProbability'],'ro--')

annotateSet1 = {'AAo','KKo','QQo','JJo','TTo','99o','88o','77o','66o','55o','44o','33o','22o'}
annotateSet2 = {'AKs','KJs','QTs','98s','32s'}
annotateSet3 = {'AKo','KJo','QTo','98o','32o'}
for annotateHand in annotateSet1:  #annotation
    annotateHandXY = sortedresultFrame[sortedresultFrame['hand'] == annotateHand]['WinningProbability']
    annotateHandX = (annotateHandXY.index)[0]
    annotateHandY = (annotateHandXY.values)[0]
    plt.annotate(annotateHand,xytext=(annotateHandX+3,annotateHandY+0.005),xy=(annotateHandX,annotateHandY),fontsize=15,arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))     
for annotateHand in annotateSet2:  #annotation
    annotateHandXY = sortedresultFrame[sortedresultFrame['hand'] == annotateHand]['WinningProbability']
    annotateHandX = (annotateHandXY.index)[0]
    annotateHandY = (annotateHandXY.values)[0]
    plt.annotate(annotateHand,xytext=(annotateHandX-7,annotateHandY-0.015),xy=(annotateHandX,annotateHandY),fontsize=15,arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))
for annotateHand in annotateSet3:  #annotation
    annotateHandXY = sortedresultFrame[sortedresultFrame['hand'] == annotateHand]['WinningProbability']
    annotateHandX = (annotateHandXY.index)[0]
    annotateHandY = (annotateHandXY.values)[0]
    plt.annotate(annotateHand,xytext=(annotateHandX-7,annotateHandY-0.015),xy=(annotateHandX,annotateHandY),fontsize=15,arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))

plt.text(10,0.38,'Notes:',fontsize=17)
plt.text(10,0.365,'1. The probability is approximated by running a Monte Carlo method.',fontsize=15)
plt.text(13,0.35,'The number of simulations is 200.',fontsize=15)
plt.text(10,0.335,'2. Number 10 in poker is noted \'T\' in this graph.',fontsize=15)
plt.text(10,0.32,'3. \'s\' means suited, and \'o\' means off suit.',fontsize=15)
plt.text(10,0.305,'4. author Shuxin Yang  2017-11-25',fontsize=15)
plt.xlabel('Different Hands',fontsize=20)
plt.ylabel('Winning Probability',fontsize=20)
plt.title('Winning Probability of Different Hands (1 opponent)',fontsize=25)
plt.savefig(file_path + 'ProbabilityGraph1.png',dpi=200)
plt.show()

#draw picture 2
sortedresultFrame['hand1num'] = sortedresultFrame['hand1']
sortedresultFrame['hand2num'] = sortedresultFrame['hand2']
for j in range(0,len(sortedresultFrame)):
    if sortedresultFrame['hand1'][j][0] == 'T':
        sortedresultFrame['hand1num'][j] = 'a'
    elif sortedresultFrame['hand1'][j][0] == 'J':
        sortedresultFrame['hand1num'][j] = 'b'
    elif sortedresultFrame['hand1'][j][0] == 'Q':
        sortedresultFrame['hand1num'][j] = 'c'
    elif sortedresultFrame['hand1'][j][0] == 'K':
        sortedresultFrame['hand1num'][j] = 'd'
    elif sortedresultFrame['hand1'][j][0] == 'A':
        sortedresultFrame['hand1num'][j] = 'e'
    if sortedresultFrame['hand2'][j][0] == 'T':
        sortedresultFrame['hand2num'][j] = 'a'
    elif sortedresultFrame['hand2'][j][0] == 'J':
        sortedresultFrame['hand2num'][j] = 'b'
    elif sortedresultFrame['hand2'][j][0] == 'Q':
        sortedresultFrame['hand2num'][j] = 'c'
    elif sortedresultFrame['hand2'][j][0] == 'K':
        sortedresultFrame['hand2num'][j] = 'd'
    elif sortedresultFrame['hand2'][j][0] == 'A':
        sortedresultFrame['hand2num'][j] = 'e'
        
oMatrix = sortedresultFrame[sortedresultFrame['type']=='o'].pivot(index='hand1num',columns='hand2num',values='WinningProbability')
oMatrix = oMatrix.rename(index={'a':'T','b':'J','c':'Q','d':'K','e':'A'},columns={'a':'T','b':'J','c':'Q','d':'K','e':'A'})

sMatrix = sortedresultFrame[sortedresultFrame['type']=='s'].pivot(index='hand1num',columns='hand2num',values='WinningProbability')
sMatrix = sMatrix.rename(index={'a':'T','b':'J','c':'Q','d':'K','e':'A'},columns={'a':'T','b':'J','c':'Q','d':'K','e':'A'})
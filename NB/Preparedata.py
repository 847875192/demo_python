import os
import random
import sys


OutFileName = '../test/nb_data'
trainOutFile = open(OutFileName+".train","w",encoding='utf-8')
testOutFile =open(OutFileName+".test","w",encoding='utf-8')

WordDir ={}
WordList =[]

i=0
tag =0
input = '../data'
for filename in os.listdir(input):
    if filename.find("business") != -1:
        tag =1
    elif filename.find("auto")!=-1:
        tag = 2
    elif filename.find("sport") != -1:
        tag = 3
    i+=1

    #留出法，80%为训练集，20%为测试集
    rd = random.random()
    outfile = testOutFile
    if rd<0.8:
        outfile = trainOutFile

    if i%1000 ==0:
        print (i,"files processed!\r")

        #读取每一个原始样本
    infile = open(input+'/'+filename,'r',encoding='utf-8')
    outfile.write(str(tag)+" ")
    content = infile.read().strip()
    words = content.replace('\n',' ').split(" ")
    for word in words:
        if  len(word.strip())<1:
            continue
        if word not in WordDir:
            WordList.append(word)
            WordDir[word]=len(WordList)
        outfile.write(str( WordDir[word] ) + " ")
    outfile.write("#"+filename+"\n")
    infile.close()

print ("一共有"+str(len(WordList)) +"个词语读取成功")

trainOutFile.close()
testOutFile.close()
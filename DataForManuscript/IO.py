# -*- coding: utf-8 -*-

import random
import re

class IO(object):
    #读入LIST
    def readtolist(self,readfilename,list):
        #readfilename = 'C:/Users/administor/Desktop/42.txt'
        with open(readfilename, 'r', encoding='utf-8') as in_file:
            lines = in_file.readlines()
            for line in lines:
                line = line.strip()
                list.append(line)
            return list

    #读入dict
    def readtodict(self,readfilename,dict):
        #readfilename = 'C:/Users/administor/Desktop/42.txt'
        with open(readfilename, 'r', encoding='utf-8') as in_file:
            lines = in_file.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(',')
                key = line[0]
                value = line[1]
                dict.setdefault(key, []).append(value)     # 可以写入多值字典,value的 形式是list
                #listdict =list(dict.keys())     #得到字典的KDY值的列表
                # for i in listdict:
                #     listvalue= dict[i]     #得到字典的KDY值i的value列表
            return dict



    #写入TXT
    def write(self,writefilename,list):
        #writefilename = 'C:/Users/administor/Desktop/42.txt'
        with open(writefilename, 'w', encoding='utf-8') as write_file:
            for line in list:
                write_file.write(str(line)+'\n')

    #追写入TXT
    def writetoadd(self,writefilename,list):
        #writefilename = 'C:/Users/administor/Desktop/42.txt'
        with open(writefilename, 'a', encoding='utf-8') as write_file:
            for line in list:
                write_file.write(str(line)+'\n')



    #随机抽取selectnum个数
    def randomselectnum(self,list1,selectnum,list2):
        number = range(0,len(list1))
        randnumber= random.sample(number,selectnum)
        randnumber.sort()
        for i in randnumber:
            list2.append(list1[i])
        return list2

    #随机抽取同分布的2个数据selectnum个数
    def randomselect(self,selectnum,list1,list2,list3,list4):
        number = range(0,len(list1))
        randnumber= random.sample(number,selectnum)
        randnumber.sort()
        for i in randnumber:
            list2.append(list1[i])
            list4.append(list3[i])
        return list2 ,list4


    #随机抽取selectnum个数,抛出被抽取到的以后，继续抽取(无放回)

    def remove_num(original_list,n,k):    #K次抽取，每次抽取n个数拿走
        global list1
        count =0
        while count < k:
            count += 1
            random_num = random.sample(origin_list, n)
            list1 = origin_list = list(set(origin_list)- set(random_num))
            yield random_num

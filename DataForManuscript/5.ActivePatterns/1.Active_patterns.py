# -*- coding: utf-8 -*-

from Dateformat import datechange
from IO import  IO
import time
import math

#This program is used to calculate the active patterns of the two groups.The result can be showed after running the program.
#The two groups:PSI, and  other users in the community.
#The 10 different time periods were:
#“2012.3.19-2012.9.18”, “2012.3.19-2013.3.18”, “2012.3.19-2013.9.18”, “2012.3.19-2014.3.18”, “2012.3.19-2014.9.18”, “2012.3.19-2015.3.18”, “2012.3.19-2015.9.18”, “2012.3.19-2016.3.18”, “2012.3.19-2016.9.18”, and “2012.3.19-2017.2.18”.
#To calculate the communication between users and PSI in different time periods, we should change the filenames in this program:
#“2012.3.19-2012.9.18”: endyearth=2012，part =2， file1='Data5/....date2012918.txt',file2='Data5/....date2012918.txt',and writefile1='Data5/....date2012918.txt'
#“2012.3.19-2013.3.18”: endyearth=2013，part =1， file1='Data5/....date2013318.txt',file2='Data5/....date2013318.txt',and writefile1='Data5/....date2013318.txt'
#“2012.3.19-2013.9.18”: endyearth=2013，part =2， file1='Data5/....date2013918.txt',file2='Data5/....date2013918.txt',and writefile1='Data5/....date2013918.txt'
#“2012.3.19-2014.3.18”: endyearth=2014，part =1， file1='Data5/....date2014318.txt',file2='Data5/....date2014318.txt',and writefile1='Data5/....date2014318.txt'
#“2012.3.19-2014.9.18”: endyearth=2014，part =2， file1='Data5/....date2014918.txt',file2='Data5/....date2014918.txt',and writefile1='Data5/....date2014918.txt'
#“2012.3.19-2015.3.18”: endyearth=2015，part =1， file1='Data5/....date2015318.txt',file2='Data5/....date2015318.txt',and writefile1='Data5/....date2015318.txt'
#“2012.3.19-2015.9.18”: endyearth=2015，part =2， file1='Data5/....date2015918.txt',file2='Data5/....date2015918.txt',and writefile1='Data5/....date2015918.txt'
#“2012.3.19-2016.3.18”: endyearth=2016，part =1， file1='Data5/....date2016318.txt',file2='Data5/....date2016318.txt',and writefile1='Data5/....date2016318.txt'
#“2012.3.19-2016.9.18”: endyearth=2016，part =2， file1='Data5/....date2016918.txt',file2='Data5/....date2016918.txt',and writefile1='Data5/....date2016918.txt'
#“2012.3.19-2017.2.18”: endyearth=2017，part =1， file1='Data5/....date2017218.txt',file2='Data5/....date2017218.txt',and writefile1='Data5/....date2017218.txt'


@datechange.warps(0.001)
def myfunc(*args, **kwargs):
    uidlist1 = []
    uidlist2 = []
    uidlist3 = []
    splitlist = []
    uiddict1= {}
    uiddict2= {}
    deallist2 =[]
    deallist3 =[]
    deallist6= []
    deallist7 = []
    iooperation= IO()
    endyearth =2016# deadline:year
    part =2# 2:the date of the deadline is 918,91: the date of the deadline is 318
    file1 = 'Data5/OriginalData.txt'
    file2 = 'Data5/Uid_of_PSI/Uid_of_PSI_to_the_date2016918.txt'
    file3 = 'Data5/Uid_of_TotalUsers/Uid_of_TotalUsers_to_the_date2016918.txt'
    iooperation.readtolist(file1,uidlist1)
    iooperation.readtolist(file2,uidlist2)
    iooperation.readtolist(file3,uidlist3)

    def get_list_time_change(strtime):  #  trans to  stamp
        for i in uiddict1[strtime]:
            deallist2.append(datechange().formattime(i))
            deallist2.sort()
        if len(deallist2)>2:
            for i in range(1, len(deallist2)):
                deallist3.append((deallist2[i] - deallist2[i - 1]) / 86400)
            deallist4 = [math.ceil(i) for i in deallist3]  # take only integer part of the number.
            for i in range(len(deallist4)-1, -1, -1):
                if deallist4[i] == deallist4[i - 1]:
                    del (deallist4[i])
            for i in deallist4:
                if i == 0:
                    deallist4.remove(i)
            for ii in deallist4:
                key = strtime
                value = ii
                uiddict2.setdefault(key, []).append(value)  # put Time interval write into dictionary
            deallist3.clear()
            deallist4.clear()
        deallist2.clear()


    def get_time_eliminate_subsequent(time_in,endyearth,part):    # Cutting time
        start_year_format = str('2012-3-19 00:00')
        if part ==1 :
            end_year_format = str(str(endyearth)+'-3-19 00:00')
        if part == 2:
            end_year_format = str(str(endyearth) + '-9-19 00:00')
        time_str = str(time_in)
        if ' ' in time_str:
            try:
                time_exchange = time.strptime(time_str, "%Y-%m-%d %H:%M")
                timestamp_time_str = time.mktime(time_exchange)
            except Exception as e:
                time_exchange = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                timestamp_time_str = time.mktime(time_exchange)
            end_year_exchange = time.strptime(end_year_format, "%Y-%m-%d %H:%M")
            timestamp_endtime =time.mktime(end_year_exchange)
            time_value = int(timestamp_time_str)-int(timestamp_endtime)
            if time_value < 0:
                return 1
            else:
                return 0
        else:
            return 0

    def count_frequence(interval_list):
        if len(interval_list) < 2:
            return 0
        else:
            for i in range(1, len(interval_list)):
                if int(interval_list[i - 1]) + int(interval_list[i]) < 5:
                    return 1
                else:
                    return 0


    if __name__ == '__main__':
        for i in uidlist1[1::]:
            total_str = i.split('     ')
            time_string = total_str[0]
            if get_time_eliminate_subsequent(time_string,endyearth,part) == 1:
                splitlist.append(i)

        for i in splitlist:  # id is KEY，time isVALUE
            ii = i.split('     ')
            key = ii[1]
            value = ii[0]
            uiddict1.setdefault(key, []).append(value)

        for i in uiddict1:
            get_list_time_change(i)

        for i in uiddict2:
            if i in uidlist2[1::]:   #suicidal users
                number = count_frequence(uiddict2[i]) #0或1
                deallist6.append(str(number))
            else:  # not suicidal users
                number = count_frequence(uiddict2[i])  # 0或1
                deallist7.append(str(number))

        number1= int(deallist6.count('1'))
        number2= int(len(uidlist2[1::]))
        print('deadline to', str(endyearth) + str(part) +  '\n' + "the active number of PSI：" + str(number1) + '\n' + "the total number of PSI：" + str(number2) + '\n' + 'the percentage is:',str(number1 / number2))

        number3= int(deallist7.count('1'))
        number4= int(len(uidlist3[1::])-len(uidlist2[1::]))
        print('deadline to', str(endyearth)+str(part)+ '\n'+ "the active number of other users in the community："+str(number3)+'\n'+"the total number of other users in the community："+str(number4)+'\n','the percentage is:'+str(number3/number4))


myfunc()

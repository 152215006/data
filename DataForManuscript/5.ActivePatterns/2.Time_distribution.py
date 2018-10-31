# -*- coding: utf-8 -*-

from Dateformat import datechange
from IO import  IO
import time
import datetime
#This program is used to calculate the Time distribution of the two groups.The result can be showed after running the program.
#The two groups:PSI, and  other users in the community.
#The first column: time periods in a day (e.g. '00' represents the time period of '12 AM' to '1AM')
#The second column: the proportion of the postings posted during this period.
@datechange.warps(0.001)
def myfunc(*args, **kwargs):
    uidlist1 = []
    uidlist2 = []
    deallist2 = []
    deallist3 = []
    id_hour_dict = {}
    iooperation = IO()
    file1 = 'Data5/OriginalData.txt'
    file2 = 'Data5/Uid_of_PSI/Uid_of_PSI_to_the_date2017218.txt'
    iooperation.readtolist(file1, uidlist1)
    iooperation.readtolist(file2, uidlist2)




    if __name__ == '__main__':
        for i in uidlist1[1::]:
            i_str = i.split('     ')
            key = i_str[1]   #id
            posting_time =i_str[0]
            time_str = posting_time.split(' ')
            hour_minute = time_str[1]
            hour_time_str =hour_minute.split(':')
            value = hour_time_str[0]
            id_hour_dict.setdefault(key, []).append(value)


        for i in id_hour_dict:
            if i in uidlist2[1::]:
                for ii in id_hour_dict[i]:
                    deallist2.append(ii)  #the hours of the postings posted by PSI
            else:
                for ii in id_hour_dict[i]:
                    deallist3.append(ii)  # the hours of the postings posted by other users in the community

        dealset2 = set(deallist2)
        print('Time distribution of postings posted by PSI:')
        for i in sorted(list(dealset2)):
            print(i +':',(int(deallist2.count(i)) / int(len(deallist2))))
        print('-------------------------------------------------')
        print('Time distribution of postings posted by other users in the community:')
        dealset3 = set(deallist3)
        for i in sorted(list(dealset3)):
            print(i + ':' , (int(deallist3.count(i)) / int(len(deallist3))))


myfunc()


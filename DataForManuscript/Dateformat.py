# -*- coding: utf-8 -*-



import time
import datetime

class datechange(object):
    #localtime='2017-01-12 11:33:00'
    def formattime(self,localtime):
        self.localtime= localtime
        try:  # 有的精确到分
            stamp1 = datetime.datetime.strptime(self.localtime, "%Y-%m-%d %H:%M:%S")
            time_local = stamp1.timetuple()
        except Exception as e:  # 有的精确到秒
            stamp1 = datetime.datetime.strptime(self.localtime, "%Y-%m-%d %H:%M")
            time_local = stamp1.timetuple()
        timestamp = time.mktime(time_local)#是时间戳了
        date1= stamp1.strftime('%y.%m.%d')
        #return stamp1.year,stamp1.month,date1,stamp1.hour,stamp1.weekday()
        return timestamp


    def warps(No):
        def deco(func):
            def _deco(*args,**kwargs):
                print(No)
                start = time.clock()
                func(*args, **kwargs)
                end = time.clock()
                print(end-start)
                print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+'---'\
                      + datetime.datetime.now().strftime('%A'))
                #print(str(datetime.datetime.now().strftime('%c')))
            return _deco
        return deco



    # def warps(t):
    #     def deco(func):
    #         def _deco(*args,**kwargs):
    #             print(1)
    #             start = time.clock()
    #             func(*args, **kwargs)
    #             print(4)
    #             end = time.clock()
    #             if end - start > t:
    #                 print('bad')
    #             else:
    #                 print ('goods')
    #         return _deco
    #     return deco











# localtime='2017-04-24 11:33:00'
# stamp1=datetime.datetime.strptime(localtime, "%Y-%m-%d %H:%M:%S")
# print(stamp1.date())
# print(stamp1.weekday())
#
#
# #今天星期几
# today=int(time.strftime("%w"))
# print (today)
# #某个日期星期几
# anyday=datetime.datetime(2012,4,23).strftime("%w")
# print (anyday)
#
# dt = datetime.datetime.strptime("2012-09-12 21:08:12", "%Y-%m-%d %H:%M:%S")
# print (dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.minute)
# print(dt.second)
# print(dt.microsecond)
# print(dt.tzinfo)
# print('3333333333')
# print (dt.date())
# print (dt.time())
# print (dt.replace(year = 2013))
# print (dt.timetuple())
# print('-----')
# print (time.mktime(dt.timetuple()))
# print (dt.utctimetuple())
# print (dt.toordinal())
# print (dt.weekday())
# print (dt.isocalendar())
# print (dt.strftime('%y-%m-%d %I:%M:%S %p'))
# print (dt.strftime('(%y,%m,%d)'))
#
# # datetime. strftime (format)
# # %a 星期的简写。如 星期三为Web
# # %A 星期的全写。如 星期三为Wednesday
# # %b 月份的简写。如4月份为Apr
# # %B月份的全写。如4月份为April
# # %c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
# # %d:  日在这个月中的天数（是这个月的第几天）
# # %f:  微秒（范围[0,999999]）
# # %H:  小时（24小时制，[0, 23]）
# # %I:  小时（12小时制，[0, 11]）
# # %j:  日在年中的天数 [001,366]（是当年的第几天）
# # %m:  月份（[01,12]）
# # %M:  分钟（[00,59]）
# # %p:  AM或者PM
# # %S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
# # %U:  周在当年的周数当年的第几周），星期天作为周的第一天
# # %w:  今天在这周的天数，范围为[0, 6]，6表示星期天
# # %W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
# # %x:  日期字符串（如：04/07/10）
# # %X:  时间字符串（如：10:43:39）
# # %y:  2个数字表示的年份
# # %Y:  4个数字表示的年份
# # %z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
# # %Z:  时区名称（如果是本地时间，返回空字符串）
# # %%:  %% => %
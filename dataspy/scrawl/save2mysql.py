# -*- coding: gbk -*-
# Copyright (c) 2015-2016 Steven Lee, zetta info. co. Ltd This module is
# part of dataspy project

import sys
import xlrd
import MySQLdb
import re
from point import Point
value_from_cell201011 = [
    Point("全国发电量_本月值_亿千瓦时",3,2),
    Point("全国发电量_本月值_同比_%"  ,3,3),
    Point("全国发电量_本年累计值_亿千瓦时",3,4),
    Point("全国发电量_本年累计值_同比_%",3,5),

    Point("全国发电量_水电_本月值_亿千瓦时",4,2),
    Point("全国发电量_水电_本月值_同比_%"  ,4,3),
    Point("全国发电量_水电_本年累计值_亿千瓦时",4,4),
    Point("全国发电量_水电_本年累计值_同比_%",4,5),


    Point("全国发电量_火电_本月值_亿千瓦时",5,2),
    Point("全国发电量_火电_本月值_同比_%"  ,5,3),
    Point("全国发电量_火电_本年累计值_亿千瓦时",5,4),
    Point("全国发电量_火电_本年累计值_同比_%",5,5),
    

    Point("全国发电量_核电_本月值_亿千瓦时",6,2),
    Point("全国发电量_核电_本月值_同比_%"  ,6,3),
    Point("全国发电量_核电_本年累计值_亿千瓦时",6,4),
    Point("全国发电量_核电_本年累计值_同比_%",6,5),

    Point("全社会用电量_本月值_亿千瓦时",7,2),
    Point("全社会用电量_本月值_同比_%"  ,7,3),
    Point("全社会用电量_本年累计值_亿千瓦时",7,4),
    Point("全社会用电量_本年累计值_同比_%",7,5),

    Point("全社会用电量_第一产业用电量_本月值_亿千瓦时",8,2),
    Point("全社会用电量_第一产业用电量_本月值_同比_%"  ,8,3),
    Point("全社会用电量_第一产业用电量_本年累计值_亿千瓦时",8,4),
    Point("全社会用电量_第一产业用电量_本年累计值_同比_%",8,5),

    Point("全社会用电量_第二产业用电量_本月值_亿千瓦时",9,2),
    Point("全社会用电量_第二产业用电量_本月值_同比_%"  ,9,3),
    Point("全社会用电量_第二产业用电量_本年累计值_亿千瓦时",9,4),
    Point("全社会用电量_第二产业用电量_本年累计值_同比_%",9,5),

    Point("全社会用电量_第二产业用电量_工业用电_本月值_亿千瓦时",10,2),
    Point("全社会用电量_第二产业用电量_工业用电_本月值_同比_%"  ,10,3),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_亿千瓦时",10,4),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_同比_%",10,5),

    Point("全社会用电量_第二产业用电量_轻工业_本月值_亿千瓦时",11,2),
    Point("全社会用电量_第二产业用电量_轻工业_本月值_同比_%"  ,11,3),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_亿千瓦时",11,4),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_同比_%",11,5),

    Point("全社会用电量_第二产业用电量_重工业_本月值_亿千瓦时",12,2),
    Point("全社会用电量_第二产业用电量_重工业_本月值_同比_%"  ,12,3),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_亿千瓦时",12,4),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_同比_%",12,5),

    Point("全社会用电量_第三产业用电量_本月值_亿千瓦时",13,2),
    Point("全社会用电量_第三产业用电量_本月值_同比_%"  ,13,3),
    Point("全社会用电量_第三产业用电量_本年累计值_亿千瓦时",13,4),
    Point("全社会用电量_第三产业用电量_本年累计值_同比_%",13,5),

    Point("全社会用电量_城乡居民生活用电量_本月值_亿千瓦时",14,2),
    Point("全社会用电量_城乡居民生活用电量_本月值_同比_%"  ,14,3),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_亿千瓦时",14,4),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_同比_%",14,5),

    Point("6000千瓦及以上电厂发电设备容量_本年累计值_万千瓦",15,4),
    Point("6000千瓦及以上电厂发电设备容量_本年累计值_同比_%",15,5),

    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_万千瓦",16,4),
    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_同比_%",16,5),

    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_万千瓦",17,4),
    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_同比_%",17,5),

    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_万千瓦",18,4),
    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_同比_%",18,5),

    Point("全国供电煤耗率_本年累计值_克/千瓦时",19,4),
    Point("全国供电煤耗率_本年累计值_克/千瓦时_同比_%",19,5),

    Point("全国线路损失率_本年累计值_%",20,4),
    Point("全国线路损失率_本年累计值_同比增减_%",20,5),

    Point("全国供热量_本年累计值_万百万焦",21,4),
    Point("全国供热量_本年累计值_同比_%",21,5),

    Point("全国供热耗用原煤_本年累计值_万吨",22,4),
    Point("全国供热耗用原煤_本年累计值_同比_%",22,5),

    Point("全国供电量_本年累计值_亿千瓦时",23,4),
    Point("全国供电量_本年累计值_同比_%",23,5),

    Point("全国售电量_本年累计值_亿千瓦时",24,4),
    Point("全国售电量_本年累计值_同比_%",24,5),

    Point("全国线损电量_本年累计值_亿千瓦时",25,4),
    Point("全国线损电量_本年累计值_同比_%",25,5),

    Point("全国发电设备累计平均利用小时_本年累计值_小时",26,4),
    Point("全国发电设备累计平均利用小时_本年累计值_同比_%",26,5),

    Point("全国发电设备累计平均利用小时_水电_本年累计值_小时",27,4),
    Point("全国发电设备累计平均利用小时_水电_本年累计值_同比_%",27,5),
    
    Point("全国发电设备累计平均利用小时_火电_本年累计值_小时",28,4),
    Point("全国发电设备累计平均利用小时_火电_本年累计值_同比_%",28,5),

    Point("全国发电累计厂用电率_本年累计值_%",29,4),
    Point("全国发电累计厂用电率_本年累计值_同比_%",29,5),

    Point("全国发电累计厂用电率_水电_本年累计值_%",30,4),
    Point("全国发电累计厂用电率_水电_本年累计值_同比_%",30,5),

    Point("全国发电累计厂用电率_火电_本年累计值_%",31,4),
    Point("全国发电累计厂用电率_火电_本年累计值_同比_%",31,5),
    
    Point("电源基本建设投资完成额_本年累计值_亿元",32,4),
    Point("电源基本建设投资完成额_本年累计值_同比_%",32,5),

    Point("电源基本建设投资完成额_水电_本年累计值_亿元",33,4),
    Point("电源基本建设投资完成额_水电_本年累计值_同比_%",33,5),

    Point("电源基本建设投资完成额_火电_本年累计值_亿元",34,4),
    Point("电源基本建设投资完成额_火电_本年累计值_同比_%",34,5),

    Point("电源基本建设投资完成额_核电_本年累计值_亿元",35,4),

    Point("电网基本建设投资完成额_本年累计值_亿元",36,4),

    Point("发电新增设备容量_本年累计值_万千瓦",37,4),

    Point("发电新增设备容量_水电_本年累计值_万千瓦",38,4),

    Point("发电新增设备容量_火电_本年累计值_万千瓦",39,4),

    Point("新增220千伏及以上变电设备容量_本年累计值_万千伏安",40,4),

    Point("新增220千伏及以上线路长度_本年累计值_千米",41,4)
    ]

value_from_cell201102 = [
    Point("全国发电量_本月值_亿千瓦时",3,2),
    Point("全国发电量_本月值_同比_%"  ,3,3),
    Point("全国发电量_本年累计值_亿千瓦时",3,4),
    Point("全国发电量_本年累计值_同比_%",3,5),

    Point("全国发电量_水电_本月值_亿千瓦时",4,2),
    Point("全国发电量_水电_本月值_同比_%"  ,4,3),
    Point("全国发电量_水电_本年累计值_亿千瓦时",4,4),
    Point("全国发电量_水电_本年累计值_同比_%",4,5),


    Point("全国发电量_火电_本月值_亿千瓦时",5,2),
    Point("全国发电量_火电_本月值_同比_%"  ,5,3),
    Point("全国发电量_火电_本年累计值_亿千瓦时",5,4),
    Point("全国发电量_火电_本年累计值_同比_%",5,5),
    

    Point("全国发电量_核电_本月值_亿千瓦时",6,2),
    Point("全国发电量_核电_本月值_同比_%"  ,6,3),
    Point("全国发电量_核电_本年累计值_亿千瓦时",6,4),
    Point("全国发电量_核电_本年累计值_同比_%",6,5),

    Point("全社会用电量_本月值_亿千瓦时",7,2),
    Point("全社会用电量_本月值_同比_%"  ,7,3),
    Point("全社会用电量_本年累计值_亿千瓦时",7,4),
    Point("全社会用电量_本年累计值_同比_%",7,5),

    Point("全社会用电量_第一产业用电量_本月值_亿千瓦时",8,2),
    Point("全社会用电量_第一产业用电量_本月值_同比_%"  ,8,3),
    Point("全社会用电量_第一产业用电量_本年累计值_亿千瓦时",8,4),
    Point("全社会用电量_第一产业用电量_本年累计值_同比_%",8,5),

    Point("全社会用电量_第二产业用电量_本月值_亿千瓦时",9,2),
    Point("全社会用电量_第二产业用电量_本月值_同比_%"  ,9,3),
    Point("全社会用电量_第二产业用电量_本年累计值_亿千瓦时",9,4),
    Point("全社会用电量_第二产业用电量_本年累计值_同比_%",9,5),

    Point("全社会用电量_第二产业用电量_工业用电_本月值_亿千瓦时",10,2),
    Point("全社会用电量_第二产业用电量_工业用电_本月值_同比_%"  ,10,3),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_亿千瓦时",10,4),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_同比_%",10,5),

    Point("全社会用电量_第二产业用电量_轻工业_本月值_亿千瓦时",11,2),
    Point("全社会用电量_第二产业用电量_轻工业_本月值_同比_%"  ,11,3),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_亿千瓦时",11,4),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_同比_%",11,5),

    Point("全社会用电量_第二产业用电量_重工业_本月值_亿千瓦时",12,2),
    Point("全社会用电量_第二产业用电量_重工业_本月值_同比_%"  ,12,3),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_亿千瓦时",12,4),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_同比_%",12,5),

    Point("全社会用电量_第三产业用电量_本月值_亿千瓦时",13,2),
    Point("全社会用电量_第三产业用电量_本月值_同比_%"  ,13,3),
    Point("全社会用电量_第三产业用电量_本年累计值_亿千瓦时",13,4),
    Point("全社会用电量_第三产业用电量_本年累计值_同比_%",13,5),

    Point("全社会用电量_城乡居民生活用电量_本月值_亿千瓦时",14,2),
    Point("全社会用电量_城乡居民生活用电量_本月值_同比_%"  ,14,3),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_亿千瓦时",14,4),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_同比_%",14,5),

    Point("6000千瓦及以上电厂发电设备容量_本年累计值_万千瓦",15,4),
    Point("6000千瓦及以上电厂发电设备容量_本年累计值_同比_%",15,5),

    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_万千瓦",16,4),
    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_同比_%",16,5),

    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_万千瓦",17,4),
    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_同比_%",17,5),

    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_万千瓦",18,4),
    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_同比_%",18,5),

    Point("全国供热量_本年累计值_万百万焦",19,4),
    Point("全国供热量_本年累计值_同比_%",19,5),

    Point("全国供热耗用原煤_本年累计值_万吨",20,4),
    Point("全国供热耗用原煤_本年累计值_同比_%",20,5),

    Point("全国发电设备累计平均利用小时_本年累计值_小时",21,4),
    Point("全国发电设备累计平均利用小时_本年累计值_同比_%",21,5),

    Point("全国发电设备累计平均利用小时_水电_本年累计值_小时",22,4),
    Point("全国发电设备累计平均利用小时_水电_本年累计值_同比_%",22,5),
    
    Point("全国发电设备累计平均利用小时_火电_本年累计值_小时",23,4),
    Point("全国发电设备累计平均利用小时_火电_本年累计值_同比_%",23,5),

    Point("全国发电累计厂用电率_本年累计值_%",24,4),
    Point("全国发电累计厂用电率_本年累计值_同比_%",24,5),

    Point("全国发电累计厂用电率_水电_本年累计值_%",25,4),
    Point("全国发电累计厂用电率_水电_本年累计值_同比_%",25,5),

    Point("全国发电累计厂用电率_火电_本年累计值_%",26,4),
    Point("全国发电累计厂用电率_火电_本年累计值_同比_%",26,5),

    Point("电源基本建设投资完成额_本年累计值_亿元",27,4),
    Point("电源基本建设投资完成额_本年累计值_同比_%",27,5),

    Point("电源基本建设投资完成额_水电_本年累计值_亿元",28,4),
    Point("电源基本建设投资完成额_水电_本年累计值_同比_%",28,5),

    Point("电源基本建设投资完成额_火电_本年累计值_亿元",29,4),
    Point("电源基本建设投资完成额_火电_本年累计值_同比_%",29,5),

    Point("电源基本建设投资完成额_核电_本年累计值_亿元",30,4),
    Point("电源基本建设投资完成额_核电_本年累计值_同比_%",30,5),

    Point("电网基本建设投资完成额_本年累计值_亿元",31,4),

    Point("发电新增设备容量_本年累计值_万千瓦",32,4),

    Point("发电新增设备容量_水电_本年累计值_万千瓦",33,4),

    Point("发电新增设备容量_火电_本年累计值_万千瓦",34,4),

    Point("新增220千伏及以上变电设备容量_本年累计值_万千伏安",35,4),

    Point("新增220千伏及以上线路长度_本年累计值_千米",36,4)
    ]


value_from_cell201103 = [
    Point("全国发电量_本月值_亿千瓦时",3,2),
    Point("全国发电量_本月值_同比_%"  ,3,3),
    Point("全国发电量_本年累计值_亿千瓦时",3,4),
    Point("全国发电量_本年累计值_同比_%",3,5),

    Point("全国发电量_水电_本月值_亿千瓦时",4,2),
    Point("全国发电量_水电_本月值_同比_%"  ,4,3),
    Point("全国发电量_水电_本年累计值_亿千瓦时",4,4),
    Point("全国发电量_水电_本年累计值_同比_%",4,5),


    Point("全国发电量_火电_本月值_亿千瓦时",5,2),
    Point("全国发电量_火电_本月值_同比_%"  ,5,3),
    Point("全国发电量_火电_本年累计值_亿千瓦时",5,4),
    Point("全国发电量_火电_本年累计值_同比_%",5,5),
    

    Point("全国发电量_核电_本月值_亿千瓦时",6,2),
    Point("全国发电量_核电_本月值_同比_%"  ,6,3),
    Point("全国发电量_核电_本年累计值_亿千瓦时",6,4),
    Point("全国发电量_核电_本年累计值_同比_%",6,5),

    Point("全社会用电量_本月值_亿千瓦时",7,2),
    Point("全社会用电量_本月值_同比_%"  ,7,3),
    Point("全社会用电量_本年累计值_亿千瓦时",7,4),
    Point("全社会用电量_本年累计值_同比_%",7,5),

    Point("全社会用电量_第一产业用电量_本月值_亿千瓦时",8,2),
    Point("全社会用电量_第一产业用电量_本月值_同比_%"  ,8,3),
    Point("全社会用电量_第一产业用电量_本年累计值_亿千瓦时",8,4),
    Point("全社会用电量_第一产业用电量_本年累计值_同比_%",8,5),

    Point("全社会用电量_第二产业用电量_本月值_亿千瓦时",9,2),
    Point("全社会用电量_第二产业用电量_本月值_同比_%"  ,9,3),
    Point("全社会用电量_第二产业用电量_本年累计值_亿千瓦时",9,4),
    Point("全社会用电量_第二产业用电量_本年累计值_同比_%",9,5),

    Point("全社会用电量_第二产业用电量_工业用电_本月值_亿千瓦时",10,2),
    Point("全社会用电量_第二产业用电量_工业用电_本月值_同比_%"  ,10,3),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_亿千瓦时",10,4),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_同比_%",10,5),

    Point("全社会用电量_第二产业用电量_轻工业_本月值_亿千瓦时",11,2),
    Point("全社会用电量_第二产业用电量_轻工业_本月值_同比_%"  ,11,3),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_亿千瓦时",11,4),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_同比_%",11,5),

    Point("全社会用电量_第二产业用电量_重工业_本月值_亿千瓦时",12,2),
    Point("全社会用电量_第二产业用电量_重工业_本月值_同比_%"  ,12,3),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_亿千瓦时",12,4),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_同比_%",12,5),

    Point("全社会用电量_第三产业用电量_本月值_亿千瓦时",13,2),
    Point("全社会用电量_第三产业用电量_本月值_同比_%"  ,13,3),
    Point("全社会用电量_第三产业用电量_本年累计值_亿千瓦时",13,4),
    Point("全社会用电量_第三产业用电量_本年累计值_同比_%",13,5),

    Point("全社会用电量_城乡居民生活用电量_本月值_亿千瓦时",14,2),
    Point("全社会用电量_城乡居民生活用电量_本月值_同比_%"  ,14,3),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_亿千瓦时",14,4),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_同比_%",14,5),

    Point("6000千瓦及以上电厂发电设备容量_本年累计值_万千瓦",15,4),
    Point("6000千瓦及以上电厂发电设备容量_本年累计值_同比_%",15,5),

    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_万千瓦",16,4),
    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_同比_%",16,5),

    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_万千瓦",17,4),
    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_同比_%",17,5),

    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_万千瓦",18,4),
    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_同比_%",18,5),

    Point("全国供电煤耗率_本年累计值_克/千瓦时",19,4),
    Point("全国供电煤耗率_本年累计值_克/千瓦时_同比_%",19,5),

    Point("全国线路损失率_本年累计值_%",20,4),
    Point("全国线路损失率_本年累计值_同比增减_%",20,5),

    Point("全国供热量_本年累计值_万百万焦",21,4),
    Point("全国供热量_本年累计值_同比_%",21,5),

    Point("全国供热耗用原煤_本年累计值_万吨",22,4),
    Point("全国供热耗用原煤_本年累计值_同比_%",22,5),

    Point("全国发电设备累计平均利用小时_本年累计值_小时",23,4),
    Point("全国发电设备累计平均利用小时_本年累计值_同比_%",23,5),

    Point("全国发电设备累计平均利用小时_水电_本年累计值_小时",24,4),
    Point("全国发电设备累计平均利用小时_水电_本年累计值_同比_%",24,5),
    
    Point("全国发电设备累计平均利用小时_火电_本年累计值_小时",25,4),
    Point("全国发电设备累计平均利用小时_火电_本年累计值_同比_%",25,5),

    Point("全国发电累计厂用电率_本年累计值_%",26,4),
    Point("全国发电累计厂用电率_本年累计值_同比_%",26,5),

    Point("全国发电累计厂用电率_水电_本年累计值_%",27,4),
    Point("全国发电累计厂用电率_水电_本年累计值_同比_%",27,5),

    Point("全国发电累计厂用电率_火电_本年累计值_%",28,4),
    Point("全国发电累计厂用电率_火电_本年累计值_同比_%",28,5),
    
    Point("电源基本建设投资完成额_本年累计值_亿元",29,4),
    Point("电源基本建设投资完成额_本年累计值_同比_%",29,5),

    Point("电源基本建设投资完成额_水电_本年累计值_亿元",30,4),
    Point("电源基本建设投资完成额_水电_本年累计值_同比_%",30,5),

    Point("电源基本建设投资完成额_火电_本年累计值_亿元",31,4),
    Point("电源基本建设投资完成额_火电_本年累计值_同比_%",31,5),

    Point("电源基本建设投资完成额_核电_本年累计值_亿元",32,4),

    Point("电网基本建设投资完成额_本年累计值_亿元",33,4),

    Point("发电新增设备容量_本年累计值_万千瓦",34,4),

    Point("发电新增设备容量_水电_本年累计值_万千瓦",35,4),

    Point("发电新增设备容量_火电_本年累计值_万千瓦",36,4),

    Point("新增220千伏及以上变电设备容量_本年累计值_万千伏安",37,4),

    Point("新增220千伏及以上线路长度_本年累计值_千米",38,4)
    ]

value_from_cell201105 = [
    Point("全国发电量_本月值_亿千瓦时",3,2),
    Point("全国发电量_本月值_同比_%"  ,3,3),
    Point("全国发电量_本年累计值_亿千瓦时",3,4),
    Point("全国发电量_本年累计值_同比_%",3,5),

    Point("全国发电量_水电_本月值_亿千瓦时",4,2),
    Point("全国发电量_水电_本月值_同比_%"  ,4,3),
    Point("全国发电量_水电_本年累计值_亿千瓦时",4,4),
    Point("全国发电量_水电_本年累计值_同比_%",4,5),


    Point("全国发电量_火电_本月值_亿千瓦时",5,2),
    Point("全国发电量_火电_本月值_同比_%"  ,5,3),
    Point("全国发电量_火电_本年累计值_亿千瓦时",5,4),
    Point("全国发电量_火电_本年累计值_同比_%",5,5),
    

    Point("全国发电量_核电_本月值_亿千瓦时",6,2),
    Point("全国发电量_核电_本月值_同比_%"  ,6,3),
    Point("全国发电量_核电_本年累计值_亿千瓦时",6,4),
    Point("全国发电量_核电_本年累计值_同比_%",6,5),

    Point("全社会用电量_本月值_亿千瓦时",7,2),
    Point("全社会用电量_本月值_同比_%"  ,7,3),
    Point("全社会用电量_本年累计值_亿千瓦时",7,4),
    Point("全社会用电量_本年累计值_同比_%",7,5),

    Point("全社会用电量_第一产业用电量_本月值_亿千瓦时",8,2),
    Point("全社会用电量_第一产业用电量_本月值_同比_%"  ,8,3),
    Point("全社会用电量_第一产业用电量_本年累计值_亿千瓦时",8,4),
    Point("全社会用电量_第一产业用电量_本年累计值_同比_%",8,5),

    Point("全社会用电量_第二产业用电量_本月值_亿千瓦时",9,2),
    Point("全社会用电量_第二产业用电量_本月值_同比_%"  ,9,3),
    Point("全社会用电量_第二产业用电量_本年累计值_亿千瓦时",9,4),
    Point("全社会用电量_第二产业用电量_本年累计值_同比_%",9,5),

    Point("全社会用电量_第二产业用电量_工业用电_本月值_亿千瓦时",10,2),
    Point("全社会用电量_第二产业用电量_工业用电_本月值_同比_%"  ,10,3),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_亿千瓦时",10,4),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_同比_%",10,5),

    Point("全社会用电量_第二产业用电量_轻工业_本月值_亿千瓦时",11,2),
    Point("全社会用电量_第二产业用电量_轻工业_本月值_同比_%"  ,11,3),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_亿千瓦时",11,4),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_同比_%",11,5),

    Point("全社会用电量_第二产业用电量_重工业_本月值_亿千瓦时",12,2),
    Point("全社会用电量_第二产业用电量_重工业_本月值_同比_%"  ,12,3),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_亿千瓦时",12,4),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_同比_%",12,5),

    Point("全社会用电量_第三产业用电量_本月值_亿千瓦时",13,2),
    Point("全社会用电量_第三产业用电量_本月值_同比_%"  ,13,3),
    Point("全社会用电量_第三产业用电量_本年累计值_亿千瓦时",13,4),
    Point("全社会用电量_第三产业用电量_本年累计值_同比_%",13,5),

    Point("全社会用电量_城乡居民生活用电量_本月值_亿千瓦时",14,2),
    Point("全社会用电量_城乡居民生活用电量_本月值_同比_%"  ,14,3),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_亿千瓦时",14,4),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_同比_%",14,5),

    Point("6000千瓦及以上电厂发电设备容量_本年累计值_万千瓦",15,4),
    Point("6000千瓦及以上电厂发电设备容量_本年累计值_同比_%",15,5),

    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_万千瓦",16,4),
    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_同比_%",16,5),

    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_万千瓦",17,4),
    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_同比_%",17,5),

    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_万千瓦",18,4),
    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_同比_%",18,5),

    Point("全国供电煤耗率_本年累计值_克/千瓦时",19,4),
    Point("全国供电煤耗率_本年累计值_克/千瓦时_同比_%",19,5),

    Point("全国线路损失率_本年累计值_%",20,4),
    Point("全国线路损失率_本年累计值_同比增减_%",20,5),

    Point("全国供热量_本年累计值_万百万焦",21,4),
    Point("全国供热量_本年累计值_同比_%",21,5),

    Point("全国供热耗用原煤_本年累计值_万吨",22,4),
    Point("全国供热耗用原煤_本年累计值_同比_%",22,5),

    Point("全国供电量_本年累计值_亿千瓦时",23,4),
    Point("全国供电量_本年累计值_同比_%",23,5),

    Point("全国售电量_本年累计值_亿千瓦时",24,4),
    Point("全国售电量_本年累计值_同比_%",24,5),

    Point("全国线损电量_本年累计值_亿千瓦时",25,4),
    Point("全国线损电量_本年累计值_同比_%",25,5),

    Point("全国发电设备累计平均利用小时_本年累计值_小时",26,4),
    Point("全国发电设备累计平均利用小时_本年累计值_同比_%",26,5),

    Point("全国发电设备累计平均利用小时_水电_本年累计值_小时",27,4),
    Point("全国发电设备累计平均利用小时_水电_本年累计值_同比_%",27,5),
    
    Point("全国发电设备累计平均利用小时_火电_本年累计值_小时",28,4),
    Point("全国发电设备累计平均利用小时_火电_本年累计值_同比_%",28,5),

    Point("全国发电累计厂用电率_本年累计值_%",29,4),
    Point("全国发电累计厂用电率_本年累计值_同比_%",29,5),

    Point("全国发电累计厂用电率_水电_本年累计值_%",30,4),
    Point("全国发电累计厂用电率_水电_本年累计值_同比_%",30,5),

    Point("全国发电累计厂用电率_火电_本年累计值_%",31,4),
    Point("全国发电累计厂用电率_火电_本年累计值_同比_%",31,5),
    
    Point("电源基本建设投资完成额_本年累计值_亿元",32,4),
    Point("电源基本建设投资完成额_本年累计值_同比_%",32,5),

    Point("电源基本建设投资完成额_水电_本年累计值_亿元",33,4),
    Point("电源基本建设投资完成额_水电_本年累计值_同比_%",33,5),

    Point("电源基本建设投资完成额_火电_本年累计值_亿元",34,4),
    Point("电源基本建设投资完成额_火电_本年累计值_同比_%",34,5),

    Point("电源基本建设投资完成额_核电_本年累计值_亿元",35,4),

    Point("电网基本建设投资完成额_本年累计值_亿元",36,4),

    Point("发电新增设备容量_本年累计值_万千瓦",37,4),

    Point("发电新增设备容量_水电_本年累计值_万千瓦",38,4),

    Point("发电新增设备容量_火电_本年累计值_万千瓦",39,4),

    Point("新增220千伏及以上变电设备容量_本年累计值_万千伏安",40,4),

    Point("新增220千伏及以上线路长度_本年累计值_千米",41,4)
    ]


value_from_cell201306 = [
    Point("全国发电量_本月值_亿千瓦时",3,2),
    Point("全国发电量_本月值_同比_%"  ,3,3),
    Point("全国发电量_本年累计值_亿千瓦时",3,4),
    Point("全国发电量_本年累计值_同比_%",3,5),

    Point("全国发电量_水电_本月值_亿千瓦时",4,2),
    Point("全国发电量_水电_本月值_同比_%"  ,4,3),
    Point("全国发电量_水电_本年累计值_亿千瓦时",4,4),
    Point("全国发电量_水电_本年累计值_同比_%",4,5),


    Point("全国发电量_火电_本月值_亿千瓦时",5,2),
    Point("全国发电量_火电_本月值_同比_%"  ,5,3),
    Point("全国发电量_火电_本年累计值_亿千瓦时",5,4),
    Point("全国发电量_火电_本年累计值_同比_%",5,5),
    

    Point("全国发电量_核电_本月值_亿千瓦时",6,2),
    Point("全国发电量_核电_本月值_同比_%"  ,6,3),
    Point("全国发电量_核电_本年累计值_亿千瓦时",6,4),
    Point("全国发电量_核电_本年累计值_同比_%",6,5),

    Point("全社会用电量_本月值_亿千瓦时",7,2),
    Point("全社会用电量_本月值_同比_%"  ,7,3),
    Point("全社会用电量_本年累计值_亿千瓦时",7,4),
    Point("全社会用电量_本年累计值_同比_%",7,5),

    Point("全社会用电量_第一产业用电量_本月值_亿千瓦时",8,2),
    Point("全社会用电量_第一产业用电量_本月值_同比_%"  ,8,3),
    Point("全社会用电量_第一产业用电量_本年累计值_亿千瓦时",8,4),
    Point("全社会用电量_第一产业用电量_本年累计值_同比_%",8,5),

    Point("全社会用电量_第二产业用电量_本月值_亿千瓦时",9,2),
    Point("全社会用电量_第二产业用电量_本月值_同比_%"  ,9,3),
    Point("全社会用电量_第二产业用电量_本年累计值_亿千瓦时",9,4),
    Point("全社会用电量_第二产业用电量_本年累计值_同比_%",9,5),

    Point("全社会用电量_第二产业用电量_工业用电_本月值_亿千瓦时",10,2),
    Point("全社会用电量_第二产业用电量_工业用电_本月值_同比_%"  ,10,3),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_亿千瓦时",10,4),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_同比_%",10,5),

    Point("全社会用电量_第二产业用电量_轻工业_本月值_亿千瓦时",11,2),
    Point("全社会用电量_第二产业用电量_轻工业_本月值_同比_%"  ,11,3),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_亿千瓦时",11,4),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_同比_%",11,5),

    Point("全社会用电量_第二产业用电量_重工业_本月值_亿千瓦时",12,2),
    Point("全社会用电量_第二产业用电量_重工业_本月值_同比_%"  ,12,3),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_亿千瓦时",12,4),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_同比_%",12,5),

    Point("全社会用电量_第三产业用电量_本月值_亿千瓦时",13,2),
    Point("全社会用电量_第三产业用电量_本月值_同比_%"  ,13,3),
    Point("全社会用电量_第三产业用电量_本年累计值_亿千瓦时",13,4),
    Point("全社会用电量_第三产业用电量_本年累计值_同比_%",13,5),

    Point("全社会用电量_城乡居民生活用电量_本月值_亿千瓦时",14,2),
    Point("全社会用电量_城乡居民生活用电量_本月值_同比_%"  ,14,3),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_亿千瓦时",14,4),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_同比_%",14,5),

    Point("6000千瓦及以上电厂发电设备容量_本年累计值_万千瓦",15,4),
    Point("6000千瓦及以上电厂发电设备容量_本年累计值_同比_%",15,5),

    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_万千瓦",16,4),
    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_同比_%",16,5),

    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_万千瓦",17,4),
    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_同比_%",17,5),

    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_万千瓦",18,4),
    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_同比_%",18,5),

    Point("全国供电煤耗率_本年累计值_克/千瓦时",19,4),
    Point("全国供电煤耗率_本年累计值_克/千瓦时_同比_%",19,5),

    Point("全国线路损失率_本年累计值_%",20,4),
    Point("全国线路损失率_本年累计值_同比增减_%",20,5),

    Point("全国供热量_本年累计值_万百万焦",21,4),
    Point("全国供热量_本年累计值_同比_%",21,5),

    Point("全国供热耗用原煤_本年累计值_万吨",22,4),
    Point("全国供热耗用原煤_本年累计值_同比_%",22,5),

    Point("全国供电量_本年累计值_亿千瓦时",23,4),
    Point("全国供电量_本年累计值_同比_%",23,5),

    Point("全国售电量_本年累计值_亿千瓦时",24,4),
    Point("全国售电量_本年累计值_同比_%",24,5),

    Point("全国线损电量_本年累计值_亿千瓦时",25,4),
    Point("全国线损电量_本年累计值_同比_%",25,5),

    Point("全国发电设备累计平均利用小时_本年累计值_小时",26,4),
    Point("全国发电设备累计平均利用小时_本年累计值_同比_%",26,5),

    Point("全国发电设备累计平均利用小时_水电_本年累计值_小时",27,4),
    Point("全国发电设备累计平均利用小时_水电_本年累计值_同比_%",27,5),
    
    Point("全国发电设备累计平均利用小时_火电_本年累计值_小时",28,4),
    Point("全国发电设备累计平均利用小时_火电_本年累计值_同比_%",28,5),

    Point("全国发电累计厂用电率_本年累计值_%",29,4),
    Point("全国发电累计厂用电率_本年累计值_同比_%",29,5),

    Point("全国发电累计厂用电率_水电_本年累计值_%",30,4),
    Point("全国发电累计厂用电率_水电_本年累计值_同比_%",30,5),

    Point("全国发电累计厂用电率_火电_本年累计值_%",31,4),
    Point("全国发电累计厂用电率_火电_本年累计值_同比_%",31,5),
    
    Point("电源基本建设投资完成额_本年累计值_亿元",32,4),
    Point("电源基本建设投资完成额_本年累计值_同比_%",32,5),

    Point("电源基本建设投资完成额_水电_本年累计值_亿元",33,4),
    Point("电源基本建设投资完成额_水电_本年累计值_同比_%",33,5),

    Point("电源基本建设投资完成额_火电_本年累计值_亿元",34,4),
    Point("电源基本建设投资完成额_火电_本年累计值_同比_%",34,5),

    Point("电源基本建设投资完成额_核电_本年累计值_亿元",35,4),

    Point("电网基本建设投资完成额_本年累计值_亿元",36,4),

    Point("发电新增设备容量_本年累计值_万千瓦",37,4),

    Point("发电新增设备容量_水电_本年累计值_万千瓦",38,4),

    Point("发电新增设备容量_火电_本年累计值_万千瓦",39,4),

    Point("发电新增设备容量_核电_本年累计值_万千瓦",40,4),

    Point("新增220千伏及以上变电设备容量_本年累计值_万千伏安",41,4),

    Point("新增220千伏及以上线路长度_本年累计值_千米",42,4)
    ]

value_from_cell201312 = [
    Point("全国发电量_本月值_亿千瓦时",3,2),
    Point("全国发电量_本月值_同比_%"  ,3,3),
    Point("全国发电量_本年累计值_亿千瓦时",3,4),
    Point("全国发电量_本年累计值_同比_%",3,5),

    Point("全国发电量_水电_本月值_亿千瓦时",4,2),
    Point("全国发电量_水电_本月值_同比_%"  ,4,3),
    Point("全国发电量_水电_本年累计值_亿千瓦时",4,4),
    Point("全国发电量_水电_本年累计值_同比_%",4,5),


    Point("全国发电量_火电_本月值_亿千瓦时",5,2),
    Point("全国发电量_火电_本月值_同比_%"  ,5,3),
    Point("全国发电量_火电_本年累计值_亿千瓦时",5,4),
    Point("全国发电量_火电_本年累计值_同比_%",5,5),
    

    Point("全国发电量_核电_本月值_亿千瓦时",6,2),
    Point("全国发电量_核电_本月值_同比_%"  ,6,3),
    Point("全国发电量_核电_本年累计值_亿千瓦时",6,4),
    Point("全国发电量_核电_本年累计值_同比_%",6,5),

    Point("全社会用电量_本月值_亿千瓦时",7,2),
    Point("全社会用电量_本月值_同比_%"  ,7,3),
    Point("全社会用电量_本年累计值_亿千瓦时",7,4),
    Point("全社会用电量_本年累计值_同比_%",7,5),

    Point("全社会用电量_第一产业用电量_本月值_亿千瓦时",8,2),
    Point("全社会用电量_第一产业用电量_本月值_同比_%"  ,8,3),
    Point("全社会用电量_第一产业用电量_本年累计值_亿千瓦时",8,4),
    Point("全社会用电量_第一产业用电量_本年累计值_同比_%",8,5),

    Point("全社会用电量_第二产业用电量_本月值_亿千瓦时",9,2),
    Point("全社会用电量_第二产业用电量_本月值_同比_%"  ,9,3),
    Point("全社会用电量_第二产业用电量_本年累计值_亿千瓦时",9,4),
    Point("全社会用电量_第二产业用电量_本年累计值_同比_%",9,5),

    Point("全社会用电量_第二产业用电量_工业用电_本月值_亿千瓦时",10,2),
    Point("全社会用电量_第二产业用电量_工业用电_本月值_同比_%"  ,10,3),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_亿千瓦时",10,4),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_同比_%",10,5),

    Point("全社会用电量_第二产业用电量_轻工业_本月值_亿千瓦时",11,2),
    Point("全社会用电量_第二产业用电量_轻工业_本月值_同比_%"  ,11,3),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_亿千瓦时",11,4),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_同比_%",11,5),

    Point("全社会用电量_第二产业用电量_重工业_本月值_亿千瓦时",12,2),
    Point("全社会用电量_第二产业用电量_重工业_本月值_同比_%"  ,12,3),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_亿千瓦时",12,4),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_同比_%",12,5),

    Point("全社会用电量_第三产业用电量_本月值_亿千瓦时",13,2),
    Point("全社会用电量_第三产业用电量_本月值_同比_%"  ,13,3),
    Point("全社会用电量_第三产业用电量_本年累计值_亿千瓦时",13,4),
    Point("全社会用电量_第三产业用电量_本年累计值_同比_%",13,5),

    Point("全社会用电量_城乡居民生活用电量_本月值_亿千瓦时",14,2),
    Point("全社会用电量_城乡居民生活用电量_本月值_同比_%"  ,14,3),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_亿千瓦时",14,4),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_同比_%",14,5),

    Point("6000千瓦及以上电厂发电设备容量_本年累计值_万千瓦",15,4),
    Point("6000千瓦及以上电厂发电设备容量_本年累计值_同比_%",15,5),

    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_万千瓦",16,4),
    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_同比_%",16,5),

    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_万千瓦",17,4),
    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_同比_%",17,5),

    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_万千瓦",18,4),
    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_同比_%",18,5),

    Point("6000千瓦及以上电厂发电设备容量_风电_本年累计值_万千瓦",19,4),
    Point("6000千瓦及以上电厂发电设备容量_风电_本年累计值_同比_%",19,5),

    Point("全国供电煤耗率_本年累计值_克/千瓦时",20,4),
    Point("全国供电煤耗率_本年累计值_克/千瓦时_同比_%",20,5),

    Point("全国线路损失率_本年累计值_%",21,4),
    Point("全国线路损失率_本年累计值_同比增减_%",21,5),

    Point("全国供热量_本年累计值_万百万焦",22,4),
    Point("全国供热量_本年累计值_同比_%",22,5),

    Point("全国供热耗用原煤_本年累计值_万吨",23,4),
    Point("全国供热耗用原煤_本年累计值_同比_%",23,5),

    Point("全国供电量_本年累计值_亿千瓦时",24,4),
    Point("全国供电量_本年累计值_同比_%",24,5),

    Point("全国售电量_本年累计值_亿千瓦时",25,4),
    Point("全国售电量_本年累计值_同比_%",25,5),

    Point("全国线损电量_本年累计值_亿千瓦时",26,4),
    Point("全国线损电量_本年累计值_同比_%",26,5),

    Point("全国发电设备累计平均利用小时_本年累计值_小时",27,4),
    Point("全国发电设备累计平均利用小时_本年累计值_同比_%",27,5),

    Point("全国发电设备累计平均利用小时_水电_本年累计值_小时",28,4),
    Point("全国发电设备累计平均利用小时_水电_本年累计值_同比_%",28,5),
    
    Point("全国发电设备累计平均利用小时_火电_本年累计值_小时",29,4),
    Point("全国发电设备累计平均利用小时_火电_本年累计值_同比_%",29,5),

    Point("全国发电设备累计平均利用小时_风电_本年累计值_小时",30,4),
    Point("全国发电设备累计平均利用小时_风电_本年累计值_同比_%",30,5),

    Point("全国发电累计厂用电率_本年累计值_%",31,4),
    Point("全国发电累计厂用电率_本年累计值_同比_%",31,5),

    Point("全国发电累计厂用电率_水电_本年累计值_%",32,4),
    Point("全国发电累计厂用电率_水电_本年累计值_同比_%",32,5),

    Point("全国发电累计厂用电率_火电_本年累计值_%",33,4),
    Point("全国发电累计厂用电率_火电_本年累计值_同比_%",33,5),
    
    Point("电源基本建设投资完成额_本年累计值_亿元",34,4),
    Point("电源基本建设投资完成额_本年累计值_同比_%",34,5),

    Point("电源基本建设投资完成额_水电_本年累计值_亿元",35,4),
    Point("电源基本建设投资完成额_水电_本年累计值_同比_%",35,5),

    Point("电源基本建设投资完成额_火电_本年累计值_亿元",36,4),
    Point("电源基本建设投资完成额_火电_本年累计值_同比_%",36,5),

    Point("电源基本建设投资完成额_核电_本年累计值_亿元",37,4),

    Point("电网基本建设投资完成额_本年累计值_亿元",38,4),

    Point("发电新增设备容量_本年累计值_万千瓦",39,4),

    Point("发电新增设备容量_水电_本年累计值_万千瓦",40,4),

    Point("发电新增设备容量_火电_本年累计值_万千瓦",41,4),

    Point("新增220千伏及以上变电设备容量_本年累计值_万千伏安",42,4),

    Point("新增220千伏及以上线路长度_本年累计值_千米",43,4)
    ]

value_from_cell201404 = [
    Point("全国发电量_本月值_亿千瓦时",3,2),
    Point("全国发电量_本月值_同比_%"  ,3,3),
    Point("全国发电量_本年累计值_亿千瓦时",3,4),
    Point("全国发电量_本年累计值_同比_%",3,5),

    Point("全国发电量_水电_本月值_亿千瓦时",4,2),
    Point("全国发电量_水电_本月值_同比_%"  ,4,3),
    Point("全国发电量_水电_本年累计值_亿千瓦时",4,4),
    Point("全国发电量_水电_本年累计值_同比_%",4,5),


    Point("全国发电量_火电_本月值_亿千瓦时",5,2),
    Point("全国发电量_火电_本月值_同比_%"  ,5,3),
    Point("全国发电量_火电_本年累计值_亿千瓦时",5,4),
    Point("全国发电量_火电_本年累计值_同比_%",5,5),
    

    Point("全国发电量_核电_本月值_亿千瓦时",6,2),
    Point("全国发电量_核电_本月值_同比_%"  ,6,3),
    Point("全国发电量_核电_本年累计值_亿千瓦时",6,4),
    Point("全国发电量_核电_本年累计值_同比_%",6,5),

    Point("全国发电量_风电_本月值_亿千瓦时",7,2),
    Point("全国发电量_风电_本月值_同比_%"  ,7,3),
    Point("全国发电量_风电_本年累计值_亿千瓦时",7,4),
    Point("全国发电量_风电_本年累计值_同比_%",7,5),


    Point("全社会用电量_本月值_亿千瓦时",8,2),
    Point("全社会用电量_本月值_同比_%"  ,8,3),
    Point("全社会用电量_本年累计值_亿千瓦时",8,4),
    Point("全社会用电量_本年累计值_同比_%",8,5),

    Point("全社会用电量_第一产业用电量_本月值_亿千瓦时",9,2),
    Point("全社会用电量_第一产业用电量_本月值_同比_%"  ,9,3),
    Point("全社会用电量_第一产业用电量_本年累计值_亿千瓦时",9,4),
    Point("全社会用电量_第一产业用电量_本年累计值_同比_%",9,5),

    Point("全社会用电量_第二产业用电量_本月值_亿千瓦时",10,2),
    Point("全社会用电量_第二产业用电量_本月值_同比_%"  ,10,3),
    Point("全社会用电量_第二产业用电量_本年累计值_亿千瓦时",10,4),
    Point("全社会用电量_第二产业用电量_本年累计值_同比_%",10,5),

    Point("全社会用电量_第二产业用电量_工业用电_本月值_亿千瓦时",11,2),
    Point("全社会用电量_第二产业用电量_工业用电_本月值_同比_%"  ,11,3),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_亿千瓦时",11,4),
    Point("全社会用电量_第二产业用电量_工业用电_本年累计值_同比_%",11,5),

    Point("全社会用电量_第二产业用电量_轻工业_本月值_亿千瓦时",12,2),
    Point("全社会用电量_第二产业用电量_轻工业_本月值_同比_%"  ,12,3),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_亿千瓦时",12,4),
    Point("全社会用电量_第二产业用电量_轻工业_本年累计值_同比_%",12,5),

    Point("全社会用电量_第二产业用电量_重工业_本月值_亿千瓦时",13,2),
    Point("全社会用电量_第二产业用电量_重工业_本月值_同比_%"  ,13,3),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_亿千瓦时",13,4),
    Point("全社会用电量_第二产业用电量_重工业_本年累计值_同比_%",13,5),

    Point("全社会用电量_第三产业用电量_本月值_亿千瓦时",14,2),
    Point("全社会用电量_第三产业用电量_本月值_同比_%"  ,14,3),
    Point("全社会用电量_第三产业用电量_本年累计值_亿千瓦时",14,4),
    Point("全社会用电量_第三产业用电量_本年累计值_同比_%",14,5),

    Point("全社会用电量_城乡居民生活用电量_本月值_亿千瓦时",15,2),
    Point("全社会用电量_城乡居民生活用电量_本月值_同比_%"  ,15,3),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_亿千瓦时",15,4),
    Point("全社会用电量_城乡居民生活用电量_本年累计值_同比_%",15,5),

    Point("6000千瓦及以上电厂发电设备容量_本年累计值_万千瓦",16,4),
    Point("6000千瓦及以上电厂发电设备容量_本年累计值_同比_%",16,5),

    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_万千瓦",17,4),
    Point("6000千瓦及以上电厂发电设备容量_水电_本年累计值_同比_%",17,5),

    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_万千瓦",18,4),
    Point("6000千瓦及以上电厂发电设备容量_火电_本年累计值_同比_%",18,5),

    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_万千瓦",19,4),
    Point("6000千瓦及以上电厂发电设备容量_核电_本年累计值_同比_%",19,5),

    Point("6000千瓦及以上电厂发电设备容量_风电_本年累计值_万千瓦",20,4),
    Point("6000千瓦及以上电厂发电设备容量_风电_本年累计值_同比_%",20,5),

    Point("全国供电煤耗率_本年累计值_克/千瓦时",21,4),
    Point("全国供电煤耗率_本年累计值_克/千瓦时_同比_%",21,5),

    Point("全国线路损失率_本年累计值_%",22,4),
    Point("全国线路损失率_本年累计值_同比增减_%",22,5),

    Point("全国供热量_本年累计值_万百万焦",23,4),
    Point("全国供热量_本年累计值_同比_%",23,5),

    Point("全国供热耗用原煤_本年累计值_万吨",24,4),
    Point("全国供热耗用原煤_本年累计值_同比_%",24,5),

    Point("全国供电量_本年累计值_亿千瓦时",25,4),
    Point("全国供电量_本年累计值_同比_%",25,5),

    Point("全国售电量_本年累计值_亿千瓦时",26,4),
    Point("全国售电量_本年累计值_同比_%",26,5),

    Point("全国线损电量_本年累计值_亿千瓦时",27,4),
    Point("全国线损电量_本年累计值_同比_%",27,5),

    Point("全国发电设备累计平均利用小时_本年累计值_小时",28,4),
    Point("全国发电设备累计平均利用小时_本年累计值_同比_%",28,5),

    Point("全国发电设备累计平均利用小时_水电_本年累计值_小时",29,4),
    Point("全国发电设备累计平均利用小时_水电_本年累计值_同比_%",29,5),
    
    Point("全国发电设备累计平均利用小时_火电_本年累计值_小时",30,4),
    Point("全国发电设备累计平均利用小时_火电_本年累计值_同比_%",30,5),

    Point("全国发电设备累计平均利用小时_核电_本年累计值_小时",31,4),
    Point("全国发电设备累计平均利用小时_核电_本年累计值_同比_%",31,5),

    Point("全国发电设备累计平均利用小时_风电_本年累计值_小时",32,4),
    Point("全国发电设备累计平均利用小时_风电_本年累计值_同比_%",32,5),

    Point("全国发电累计厂用电率_本年累计值_%",33,4),
    Point("全国发电累计厂用电率_本年累计值_同比_%",33,5),

    Point("全国发电累计厂用电率_水电_本年累计值_%",34,4),
    Point("全国发电累计厂用电率_水电_本年累计值_同比_%",34,5),

    Point("全国发电累计厂用电率_火电_本年累计值_%",35,4),
    Point("全国发电累计厂用电率_火电_本年累计值_同比_%",35,5),
    
    Point("电源基本建设投资完成额_本年累计值_亿元",36,4),
    Point("电源基本建设投资完成额_本年累计值_同比_%",36,5),

    Point("电源基本建设投资完成额_水电_本年累计值_亿元",37,4),
    Point("电源基本建设投资完成额_水电_本年累计值_同比_%",37,5),

    Point("电源基本建设投资完成额_火电_本年累计值_亿元",38,4),
    Point("电源基本建设投资完成额_火电_本年累计值_同比_%",38,5),

    Point("电源基本建设投资完成额_核电_本年累计值_亿元",39,4),

    Point("电网基本建设投资完成额_本年累计值_亿元",40,4),

    Point("发电新增设备容量_本年累计值_万千瓦",41,4),

    Point("发电新增设备容量_水电_本年累计值_万千瓦",42,4),

    Point("发电新增设备容量_火电_本年累计值_万千瓦",43,4),

    Point("新增220千伏及以上变电设备容量_本年累计值_万千伏安",44,4),

    Point("新增220千伏及以上线路长度_本年累计值_千米",45,4)
    ]

##
# 读取一个本地的xls文件，将其转换成CSV文件。
# CSV一条数据格式：业务时间,数据名称，数据值
# 2014年11月, 新增220千伏及以上变电设备容量_本年累计值_万千伏安, 18233
# 2014年12月, 新增220千伏及以上变电设备容量_本年累计值_万千伏安, 23495
# 通常将同一业务时间的数据转换成一条数据，即CSV文件中的一行数据
# @param xlsfile The path to the xls file 将要转换的xls文件.
# @param csvfile Tha path to the csv file 将要生成的csv文件.


def trans_xls_csv(xlsfilexls, csvfile):
    xlrd.biffh.unpack_unicode.func_globals["unicode"] = lambda s, e: unicode(s, e, errors="ignore")
    book = xlrd.open_workbook(xlsfilexls)
    table = book.sheets()[0]
    csvhead = '业务时间,'
    biztime = ''
    dtime = table.cell(0,0).value
    m = re.findall(r'(\w*[0-9]+)\w*',dtime)

    if(len(m)==3):
        year = int(m[0])
        month = int(m[2])
        value_from_cell = get_version(year, month)
        biztime = m[0].encode("gbk") +'年' + m[2].encode("gbk") + '月'
    else:
        return
        #csvline = m[0].encode("gbk") +'年12月'+ ','
    print biztime

    try:
        with open(csvfile,'w+') as f:
            for items in value_from_cell:
                rowno = items.get_x()
                colno = items.get_y()
                csvline =biztime + ',' + items.get_s() + ',' + str(table.row(rowno)[colno].value) + '\n'
                f.write(csvline)
    except IOError as err:  
        print("File Error:"+str(err))

##
# 读取一个本地的xls文件，将其转换成CSV文件。
# CSV一条数据格式：带表头，时间（标准英文时间格式）,字段1,字段2,字段3,字段4
# 通常将同一业务时间的数据转换成一条数据，即CSV文件中的一行数据
# @param xlsfile The path to the xls file 将要转换的xls文件.
# @param csvfile Tha path to the csv file 将要生成的csv文件.


def get_version(year, month):
    
    if year==2015:
        return value_from_cell201404
    if year==2014:
        if month >= 4:
            return value_from_cell201404
        else:
            return value_from_cell201312
    if year==2013:
        if month ==11:
            return value_from_cell201312
        elif month >=6:
            return value_from_cell201306
        else:
            return value_from_cell201105
    if year==2012:
        return value_from_cell201105
    if year==2011:
        if month >=5:
            return value_from_cell201105
        elif month >=3:
            return value_from_cell201103
        else:
            return value_from_cell201102
    if year>=2009 & year<=2010:
        return value_from_cell201011
    else:
        return value_from_cell201404
    

    
'''
db=MySQLdb.connect(host='localhost', user='lican', passwd='abcd1234',charset='utf8')
cur=db.cursor()
cur.execute('use data_ems')
cur.execute('select * from geo limit 100')

f=file("e:\\down\\tes.txt",'w')
#f=file("/home/lican/Downloads/test.txt","w")

for i in cur.fetchall():
    f.write(str(i))
    f.write("\n")

f.close()
cur.close()
'''






#!/usr/bin/python
#encoding:utf-8

import MySQLdb
import random
import requests
import json
from datetime import datetime


access_token = '3cb2253f2ff5c763bf23a0d87d869c9a'

def instertdate(username , name , tel , email , group , sex ):
    db = MySQLdb.connect("114.115.153.250", "root", "Sniper@!#14", "haizhi-jly", charset='utf8')
    cursor = db.cursor()
    sql = "INSERT INTO user_info (username , name , tel,email,group,sex) " \
          "VALUES (%s, %s, %s, %s, %s ,%s)" \
          %(username , name , tel , email , group , sex)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def selectgroup(sql):
    db = MySQLdb.connect("114.115.153.250", "root", "Sniper@!#14", "haizhi-jly", charset='utf8')
    cursor = db.cursor()
    #sql = "select %s from user_group" %s_group
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except:
        print "Error! Unable to fetch data"
        return "Null"
    db.close()

def createuser():
    num = random.randint(20000 , 50000)
    username = 'haizhi' + str(num)
    name = username
    email = username + '@haizhi.com'
    sex = random.randint(0,1)
    tel = str(13800000000+random.randint(10000000 , 99999999))
    return username , name , email , sex , tel


def createBDPgroup(group_name , parent_group_id):

    data = {
        "name" : group_name ,
        "parent_id" :parent_group_id,
        "access_token": access_token

    }
    print requests.post("http://114.115.244.30:2470/api/v2/group/create", data=data).content

def getBDPgroup():
    data = {
        "access_token":access_token
    }
    results =  requests.post("http://114.115.244.30:2470/api/v2/group/list", data=data).content
    re_data =  json.loads(results)
    result_data =  re_data['result']
    first_group = result_data[0]['group_list']
    parent_group_name =  first_group[0]['group_name']
    parent_group_id =  first_group[0]['group_id']
    if parent_group_name == 'haizhi':
       # print parent_group_id
	return parent_group_id , result_data
    return "ERROR"



def createBDPuser():
    access_token = '3cb2253f2ff5c763bf23a0d87d869c9a'
    manage_groups = ['984a1e340e96ab5c312cb000e466490a']
    data = {
        "username":"haizhi",
        "name":"haizhi" ,
        "mobile":"15200199910" ,
        "email" :"haa@haha.com",
        "sex": 0,
        "role": 2,
        "manage_groups":json.dumps(manage_groups),
        "belong_groups":json.dumps(manage_groups),
        "password":"haizhi1234!",
        "has_dsh_permission":1,
        "has_tb_permission":1,
        "has_data_permission":1,
        "has_machine_learning_permission":0,
        "has_data_screen_permission":0,
        "has_date_filter_permission":0,
        "function_manage":1,
        "tb_manage":1,
        "data_source_manage":1,
        "tml_manage":1,
        "account_manage":1,
        "access_token":access_token

    }

    print requests.post("http://114.115.244.30:2470/api/v2/user/create", data=data).content



def getParentgroup():
    sql = "select f_group , s_group , t_group  from user_group group by f_group , s_group , t_group"
    f_grouplist = []
    s_grouplist = []
    t_grouplist = []
    for raw in selectgroup(sql):
        #sql = "select %s from user_group" % s_group
        #print createuser() , raw
        if raw[0] not in f_grouplist:
            f_grouplist.append(raw[0])
        if raw[1] not in s_grouplist:
            s_grouplist.append(raw[1])
        if raw[2] not in t_grouplist:
            t_grouplist.append(raw[2])
    # print s_grouplist
    # print t_grouplist
    # print f_grouplist
    print getBDPgroup()

getParentgroup()
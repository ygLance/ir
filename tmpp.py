# -*- coding:utf-8 -*-
import redis

R = redis.Redis(host='127.0.0.1',port=6379,db=0)
R.rpush("h3",1,2,3,4,5,6,7)
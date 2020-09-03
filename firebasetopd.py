#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 03:04:35 2020

@author: shayyyyyy
"""


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import base64
import os
import uuid
import pandas as pd
import numpy as np



# initializations, we have a try an accept function because if you were to run the same script twice on the 
# the same console, you will receive the error below
    # ValueError: The default Firebase app already exists. This means you called initialize_app() 
    # more than once without providing an app name as the second argument. In most cases you only 
    # need to call initialize_app() once. But if you do want to initialize multiple apps, pass a 
    # second argument to initialize_app() to give each app a unique name.
try:
    cred = credentials.Certificate('./connexta.json')#please download the json file to gain admin access
    databaseURL = {'databaseURL': "https://connexsta-01.firebaseio.com"}
    firebase_admin.initialize_app(cred,databaseURL)
except :
    cred = credentials.Certificate('./connexta.json')
    databaseURL = {'databaseURL': "https://connexsta-01.firebaseio.com"}
db = firestore.client()

########################################################
article_category_dict = {}
emp_ref = db.collection('articles1')
docs = emp_ref.stream()

postID_list = []
for doc in docs:
    x = doc.id
    postID_list.append(x)
    a = db.collection('articles1').document(x).get()
    data = a.to_dict()
    article_category_dict.update({x:data["category"]})#choose a field that you would like to call
    # dict key will be doc_id which is "00..." and value will be category , "trading".
    
new_dict = {}
for i in article_category_dict:
    uid = i #gives us the key in dict
    data = article_category_dict[i]#gives us the value in dict
    new_dict.update({uid:data})
    
art_df = pd.DataFrame.from_dict(new_dict,orient='index')
art_df = art_df.reset_index()
art_df = art_df.rename({"index": "postID", 0: "category"}, axis='columns')#rename column headers/names. Index and 0 were the column names, 
#if you had more columns it would be named starting from 0, "0,1,2,3 .. "

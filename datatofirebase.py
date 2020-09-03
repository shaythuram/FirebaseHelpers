import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import base64
import os
import uuid

# initializations, we have a try an accept function because if were to run the same script twice on the 
# the same console, u will receive the error below
    # ValueError: The default Firebase app already exists. This means you called initialize_app() 
    # more than once without providing an app name as the second argument. In most cases you only 
    # need to call initialize_app() once. But if you do want to initialize multiple apps, pass a 
    # second argument to initialize_app() to give each app a unique name.
try:
    cred = credentials.Certificate('./project_admin.json')#please download the json file to gain admin access
    databaseURL = {'databaseURL': "databaseURL"}
    firebase_admin.initialize_app(cred,databaseURL)
except :
    cred = credentials.Certificate('./connexta.json')
    databaseURL = {'databaseURL': "databaseURL"}

db = firestore.client()


data = {
 
    u'content': "",
    u'ownerID':"",
    u'postID':"",   
    u'postedBy':"",
    u'title': "",
    u'PostURL':"",

}



i = 0
b = 100
while i < 100:
    i += 1 
    uid = uuid.uuid4()#setting a Unique Document ID
    uid = uid.hex
    db.collection(u'article1').document(uid).set(data)
    
    
    
    
    
    
    
    

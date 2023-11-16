import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("C:/Users/18JSongin.ACC/Documents/test-dc64b-firebase-adminsdk-7jnbj-4f16c3e5d3.json") #might need changes
firebase_admin.initialize_app(cred,{'databaseURL': 'https://test-dc64b-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference("/")
ref.set({'users':{'user1':{'name':'bob',
                           'height':'tall',
                           'age':200},
                  
                  'user2':{'name':'jane',
                           'height':'small',
                           'age':200}
                  
                  
                  
    }})
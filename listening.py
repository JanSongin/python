import time
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
def something_Changed(response):
    print(response.event_type)
    print(response.data)

cred = credentials.Certificate("C:/Users/Jan/Documents/test-dc64b-firebase-adminsdk-7jnbj-4f16c3e5d3.json")#might need changes
firebase_admin.initialize_app(cred,{'databaseURL': 'https://test-dc64b-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference().child('temp_log')
my_ref = ref.listen(something_Changed)

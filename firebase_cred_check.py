import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/Jan/Documents/test-dc64b-firebase-adminsdk-7jnbj-4f16c3e5d3.json")#might need changes
firebase_admin.initialize_app(cred,{'databaseURL': 'https://test-dc64b-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference().child('classes')

results = ref.get()
#print(results)
#print(type(results))
for k,v in results.items():
    print("Key is: ", k, "\t value is: ",v)
    for k2, v2 in v.items():
        print("Key is: ", k2, "\t value is: ",v2)












#ref.update({'class_enrolements':''})
#ref.update({'classes':''})

#ref = db.reference().child('classes')
#ref.update({'Biology123':''})
#ref.update({'Math123':''})

#ref = db.reference().child('classes').child('Biology123')
#ref.update({'Description':'Biology123 class', 'id':'Biology123', 'title':'Biology 123'})
#ref = db.reference().child('classes').child('Math123')
#ref.update({'Description':'Math123 class', 'id':'Math123','title':'Math 123'})

ref = db.reference().child('classes').child('Biology123')
ref.delete()
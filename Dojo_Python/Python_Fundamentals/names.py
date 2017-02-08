# Names part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for item in students:
    # print data
    # print str(data.values()), len(data)
    # print data.values(), len(data)
    name = ''
    for key, data in item.iteritems():
        name += (data + " ")
    print name

# part II
users = { #dictionary
#key value pair
 'Students': [ #list
     {'first_name':  'Michael', 'last_name' : 'Jordan'}, #dictionary
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
#key value pair
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.iteritems():
    print key
    counter = 1
    for element in data:
        str = element['first_name']+" "+element['last_name']
        print counter, '-', str.upper(), len(str)-1
        counter += 1

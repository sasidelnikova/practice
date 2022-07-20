import json

my_json = """{
   "article": [
      {
         "id":"01",
         "language": "JSON",
         "edition": "first",
         "author": "Derrick Mwiti"
      },
      {
         "id":"02",
         "language": "Python",
         "edition": "second",
         "author": "Derrick Mwiti"
      }
   ],
   "blog":[
   {
       "name": "Datacamp",
       "URL":"datacamp.com"
   }
   ]
}
"""
my_json_string = json.loads(my_json)
with open('test_file.json', 'w') as file:
    json.dump(my_json_string, file, indent=4)

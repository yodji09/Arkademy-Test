import json as js

my_biodata = {"name" : "Yodi Febrian",
              "address" : "Jln. Kedoya Raya No.23 Depok",
              "age" : 25,
              "hobbies" : "Adventure",
              "married_status" : False,
              "school": "Universitas Padjajaran",
              "skill" : "python",
              "interest in coding" : True}
biodata = js.dumps(my_biodata)
print (biodata)
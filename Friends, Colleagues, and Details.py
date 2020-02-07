staff = [{"name": "Ron Swanson", "age": 55, "department": "Management", "phone": "555-1234", "salary": "2,000"} , 
         {"name": "Leslie Knope", "age": 40, "department": "Middle Management", "phone": "555-4321", "salary": "1,000"} ,
         {"name": "Andy Dwyer", "age": 32, "department": "Shoe Shining", "phone": "555-1122", "salary": "300"} ,
         {"name": "April Ludgate", "age": 27, "department": "Administration", "phone": "555-3345", "salary": "1,000"}
        ]
for i in staff:
    name = i["name"]
    dept = i["department"]
    number = i["phone"]
    print(f"\n{name} in {dept} can be reached at {number}.\n")
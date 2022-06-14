#Example1: creating dictionary
# mydic={101:"x",102:"y",103:"z"}
# print(mydic)        #{101: 'x', 102: 'y', 103: 'z'}

#Example2: Accessing item in dictionary
# mydic={
#     "brand":"hyundai",
#     "model":"i20",
#     "year": 2022
# }
# print(mydic["brand"])       #hyundai
# print(mydic["model"])       #i20

#using get
#print(mydic.get("brand"))   #hyundai

#Example3: change values in dictionary
# mydic={
#     "brand":"hyundai",
#     "model":"i20",
#     "year": 2022
# }
# mydic["year"]=2023
# print(mydic.get("year"))        #2023

#Example4: reading items from dictionary using loop.
mydic={
    "brand":"hyundai",
    "model":"i20",
    "year": 2022
}
# for i in mydic:
#     print(i)        #prints only keys from dictionary

# for i in mydic:
#     print(mydic[i])     #Prints only values from dictionary

# for i in mydic.values():
#     print(i)            #directly print values using function

# for x,y in mydic.items():
#     print(x,y)          #print keys along with values

#Exapmle5: check key is existing in dictionary or not

# if "brand" in mydic:
#     print("present")        #present
# else:
#     print("absent")

#print("model" in mydic)        #True

#Example6: find total number of items in dictionary
#print(len(mydic))       #3

#Example7: adding items to dictionary
# mydic["color"]="red"
# print(mydic)

#Example8: remove items of dictionary
# mydic.pop("brand")
# print(mydic)        #{'model': 'i20', 'year': 2022}

# del mydic['brand']
# print(mydic)      #{'model': 'i20', 'year': 2022}

# mydic.clear()
# print(mydic)        #{}

#Example9 copying dictionary
#without using copy function
# mydic2=mydic
# print(mydic2)       #{'brand': 'hyundai', 'model': 'i20', 'year': 2022}

#using copy funtion
# mydic2=mydic.copy()
# print(mydic2)       #{'brand': 'hyundai', 'model': 'i20', 'year': 2022}




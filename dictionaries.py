band = {
    "vocals":"Plant\n",

    "guitar":"Page"
}
band2= dict(vocals="Plant",guitar ="page")
print(band)
print(band2)

print(type(band))
print(len(band2))
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values 
print(band.values())
#List of key/values

print(band.items()) 
#verify if a key exists
print("guitar" in band)
print("triangle" in band)

#value
band["vocals"]="Coverdale"
band.update({"bass":"JPJ"})
print(band)

#remove items
print(band.pop("bass"))
print(band)
band["drums"] = "Bonhman"
print(band)
print(band.popitem()) #tuple 

#copying dictionaries
band2 = band.copy()
band2["drums"] = 'dAVE'
print("Goodboy!")
print(band)
print(band2)

#or use the dict() constructor function
band3 = dict(band)
print("Good Copy!")
print("band3")

print("")

#Nested dictionaries
member1 = {
    "name": "Page",
    "instrument" :"vocals"
}
member2 = {
    "name": "R&R",
        "instrument" :"guitar"
}
member3 = {
    "name": "R&R",
        "instrument" :"guitar"
}
band = {
    "member1" :member1,
    "member2" :member2,
    "member3" :member3,
}
print(band)
print(band["member2"]["instrument"])

#sets
nums ={ 1, 2, 3, 4, 5}

nums2 = set (( 1, 2, 3, 4, 5))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))
#no duplicates allowed
nums = {1 ,2 ,2 ,3 ,3 ,4 }
nums ={1 ,True, 2,False, 3, 4, 0}
print(nums)


#add a new element to set
nums.add(8)
print(nums)
# add elements from one set to another
morenums={5, 6, 7}
nums.update(morenums)
print(nums)

#Merge two sets to create a new set
one={1 ,2 ,3 ,4}
two={6 ,1 , 3, 5 ,7 }
mynewset = one.union(two)
print(mynewset)

print()
#Keep everything except the duplicates
# set:无序，不重复

mySet = set([1,2,3])
mySet2 = set([3,4,5])

mySet.add('four')
mySet.remove(1)

print(mySet)
print("交集",mySet & mySet2)
print("并集",mySet | mySet2)
print("差集",mySet - mySet2)
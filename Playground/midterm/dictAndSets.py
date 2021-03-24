s1 = set([1,2,3,4,5])
s2 = set([19,3,4,5,5,5,5,5,5])


print(s2)

s2.update([100,200])


print(s2)

# Remove duplicates from a set
# [s2.add(item) for item in l1 if item not in s2]

print(s1.union(s2))
print(s1.intersection(s2))
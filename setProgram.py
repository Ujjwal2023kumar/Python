# Python Set Methods Demonstration

a = {1, 2, 3}
b = {3, 4, 5}

# 1. add
a.add(6)
print("add:", a)

# 2. clear
temp = a.copy()
temp.clear()
print("clear:", temp)

# 3. copy
a_copy = a.copy()
print("copy:", a_copy)

# 4. difference
print("difference:", a.difference(b))

# 5. difference_update
temp = a.copy()
temp.difference_update(b)
print("difference_update:", temp)

# 6. discard
temp = a.copy()
temp.discard(2)
temp.discard(99)  # no error
print("discard:", temp)

# 7. intersection
print("intersection:", a.intersection(b))

# 8. intersection_update
temp = a.copy()
temp.intersection_update(b)
print("intersection_update:", temp)

# 9. isdisjoint
print("isdisjoint:", a.isdisjoint({7, 8}))

# 10. issubset
print("issubset:", {1, 2}.issubset(a))

# 11. issuperset
print("issuperset:", a.issuperset({1, 2}))

# 12. pop
temp = a.copy()
popped = temp.pop()
print("pop:", popped, temp)

# 13. remove
temp = a.copy()
temp.remove(1)
print("remove:", temp)

# 14. symmetric_difference
print("symmetric_difference:", a.symmetric_difference(b))

# 15. symmetric_difference_update
temp = a.copy()
temp.symmetric_difference_update(b)
print("symmetric_difference_update:", temp)

# 16. union
print("union:", a.union(b))

# 17. update
temp = {1, 2}
temp.update([3, 4], {5})
print("update:", temp)


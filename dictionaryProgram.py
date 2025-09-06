# Python Dictionary Methods Demonstration

d = {"a": 1, "b": 2, "c": 3}

# 1. clear()
d_copy = d.copy()
d_copy.clear()
print("clear:", d_copy)

# 2. copy()
d_copy = d.copy()
print("copy:", d_copy)

# 3. fromkeys()
new_dict = dict.fromkeys(["x", "y", "z"], 0)
print("fromkeys:", new_dict)

# 4. get()
print("get('a'):", d.get("a"))
print("get('z', 99):", d.get("z", 99))

# 5. items()
print("items:", list(d.items()))

# 6. keys()
print("keys:", list(d.keys()))

# 7. pop()
print("pop('b'):", d.pop("b"))
print("after pop:", d)

# 8. popitem()
key, value = d.popitem()
print("popitem:", (key, value))
print("after popitem:", d)

# 9. setdefault()
d.setdefault("d", 4)  # adds since 'd' not in dict
d.setdefault("a", 100)  # doesn't change since 'a' already exists
print("setdefault:", d)

# 10. update()
d.update({"e": 5, "f": 6})
print("update:", d)

# 11. values()
print("values:", list(d.values()))


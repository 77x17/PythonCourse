ls = [5, 1, 4, 3, 2]

val = 6
ls.append(val)
print(f"ls.append({val}):\t{ls}")

id = 2
val = 7
ls.insert(id, val)
print(f"ls.insert({id}, {val}):{ls}")

val = 3 
print(f"ls.index({val}):\t{ls.index(val)}")

val = 7
ls.remove(val)
print(f"ls.remove({val}):\t{ls}")

ls.sort()
print(f"ls.sort():\t{ls}")

ls.reverse()
print(f"ls.reverse():\t{ls}")

id = 4
ls.pop(id)
print(f"ls.pop({id}):\t{ls}")


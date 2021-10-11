lucky_number = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim",  "Jim",  "Jim", "Oscar", "Toby"]
Secondfriends = ["Wyman", "Kelly"]

friends.append("Victor")
friends.insert(1, Secondfriends)
friends.pop()
# friends.clear()
print(friends)

print(friends.index("Oscar"))

# print(friends.index("Mile"))

print(friends.count("Jim"))


# print(friends.remove())

print(friends.reverse())

friends=friends.copy
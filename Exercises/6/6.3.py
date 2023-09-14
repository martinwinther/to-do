file = open('007 members.txt', 'r')
members = file.readlines()
file.close()

members.append(input("Add a new member: " + "\n"))

file = open('007 members.txt', 'w')
file.writelines(members)
file.close()


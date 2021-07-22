# List of names
names = ["Harry", "Ron", "Hermione", "Ginny"]
# THIS CAUSES ERROR     names[4]="meem"

#THIS DOESN'T CAUSE ERROE
names.insert(4,"meem")
# Print first name
print(names[0])

# Add a new name
names.append("Draco")

# Sort names alphabetically
names.sort()

# Print list of names
print(names)

#Extend method 
names.extend(["jjdsajk","dsjfkdas","dsafk"])
print(names)

#Remove method and Pop method
names.remove("Ron")
print(names)

names.pop()
print(names)

names.pop(0)
print(names)
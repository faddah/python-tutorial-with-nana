from hmac import new


my_set = {"January", "February", "March"}
for element in my_set:
	print(element)
  
my_set.add('April')
for element in my_set:
	print(element)


my_set.add('March')
for element in my_set:
	print(element)
my_set.remove('January')
print(element)

my_list = ["January", "February", "March", "January"]
print(my_list)
my_list.remove("January")
print(my_list)

new_set = set(my_list)
print(new_set)
new_set.add("April")
print(new_set)
new_set.remove("January")
print(new_set)


 
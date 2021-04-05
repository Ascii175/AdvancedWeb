def return_unique(lst):
	result = []
	for char in lst:
        
		if lst.count(char) < 2:
			result.append(char)
	return result
    
# lst = input("Enter number of elements : ")
lst = '1','9','8','8','7','6','1','6'

print("return_unitque",lst,"==>")
print(return_unique(lst))









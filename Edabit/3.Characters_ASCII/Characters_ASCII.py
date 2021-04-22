def to_dict(lst):
		lst_2=[]
		if not lst:
				return []
		else:
				for i in lst:
						dict={}
						dict[i]=ord(i)
						lst_2.append(dict)
		return lst_2

lst = 'a','b','c'
print(to_dict(lst))

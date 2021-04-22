def longest_time(h, m, s):
	if max(h, m/60, s/3600) == m/60:
		return m
	elif max(h, m/60, s/3600) == s/3600:
		return s
	return h

# h = int(input("Hours : "))
# m = int(input("minustes : "))
# s = int(input("seconds : "))
h = 1
m = 59
s = 3598
print(longest_time(h, m, s))
def car_timer(n):
	h = n // 60
	m = n - h * 60 
	return sum(int(x) for x in str(h % 24) + str(m))

# n = int(input("n : ")) 
n = 240
print("Car_timer(",(n),") ==> ",car_timer(n))
# print(car_timer(240))

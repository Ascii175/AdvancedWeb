def hamming_distance(txt1, txt2):
	count = 0
	for n in range(len(txt1)):
		if txt1[n] != txt2[n]:
			count += 1
	return count

# txt1 = input("txt1 : ")
# txt2 = input("txt2 : ")

# txt1 = "adcde"
# txt2 = "bcdef"
# print("hamming_distance",txt1,txt2)
print(hamming_distance("adcde","bcdef"))

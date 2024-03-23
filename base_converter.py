
def main():
	
	base = int(input("base? "))
	if base < 0:
		print("Absolutely not")
		quit()
		
	num = int(input("value to convert? "))
	if num < 0:
		neg = "- "
		num = abs(num)
	else:
		neg = ""
		
	result = []
	while True:
		i = base ** len(result)
		if i <= num:
			result.append(i)
		else:
			break
	
	for key, value in enumerate(temp := result[::-1]):
		result[key] = num // value
		num = num % value
	
	return neg + " ".join([str(x) for x in result])
	

print(main())

def check_number(num) :
	if num % 2== 0 :
		print(f"{num} is an even number.")
	else:
		print(f"{num} is an old number.")
		
while True:
	num = int(input("enter a number: "))
	check_number(num)
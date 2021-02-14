

counter=0

def callfunc(n):
	if n<=1:
		global counter
		counter = counter+1
	else:
		for i in range(n):
			callfunc(int(n/2))
def main():
	n = input("(power of two)Enter your value: ")
	callfunc(int(n))
	print("number of line: ",counter)


main()
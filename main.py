def rec_mul(num1: int, num2: int) -> int:
	n = max(len(str(num1)), len(str(num2)))
	b, a = int(str(num1)[:n//2]), int(str(num1)[n//2:])
	d, c = int(str(num2)[:n//2]), int(str(num2)[n//2:])
	print(a, b, c, d)

rec_mul(123, 1234) 

"""x="123"
y="234"
a=int(x)
b=int(y)
print(a+b)"""

#in leetcode (python has a limit so set like that)
def addStrings(self, num1: str, num2: str) -> str:
        # Increase the maximum limit for the number of digits in an integer string
        sys.set_int_max_str_digits(10000)  # Increase the limit to 10000 digits (or any larger number)
        
        x = int(num1)
        y = int(num2)
        c = x + y
        return str(c)

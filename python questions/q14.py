def gcd(a, b):
   if a == b:
      return a
   elif a < b:
      return gcd(b, a)
   else:
      return gcd(b, a - b)

a = 25
b = 2
print(gcd(a, b))
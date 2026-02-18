
# 3. Check Armstrong Number
#
# Question:
# Armstrong number → sum of its digits each raised to power of digits count = number
# Example: 153 → 1³ + 5³ + 3³ = 153


num=153
digit=str(num)
power=len(digit)  #3
sum=0
for i in range(power):
    sum+=int(digit[i])**power
if num==sum:
    print(f'{num} is an Amstrong Number')
else:
    print(f'{num} is not an Amstrong Number')
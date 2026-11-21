
oten = str("olok")

left = 0
right = len(oten)-1
is_palindrome = bool(True)

while left<right:
    if oten[left]!=oten[right]:
        is_palindrome=False
        break
    left +=1
    right -=1

print(f"{oten}:is ",is_palindrome)


n=input('Enter a string:')
v,c,ws=0,0,0
vowels="aeiouAEIOU"
for i in n:
    if i in vowels:
        v+=1
    elif i==" ":
        ws+=1
    else :
        if (i>="a" and i<="z") or (i>="A" and i<="Z"):
            c+=1
print("Consonents:",c)
print("vowels:",v)
print("white spaces:",ws)

str1=input("Enter a string:")
print("It is a Palindrome"if str1==str1[::-1]else "not a palindrome")
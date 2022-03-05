#coded by harish

#printing string
#approach 1
s = input("ENter the string")
# print(s)

#approach 2
'''
for x in range(0,len(s)):
    print(s[x],end="")

'''

#approach 3
'''
for x in range(-len(s),0):
    print(s[x],end="")
'''

#approach 4
'''
for x in range(len(s),0,-1):
    print(s[-x],end="")
'''

#reverse approach 1
'''
for x in range(-1,-len(s)-1,-1):
    print(s[x],end="")
'''
#reverse approach 2 
for x in range(1,len(s)+1):
    print(s[-x],end="")

x=int(input())
h=x//3600
x=x%3600
m=x//60
x=x%60
s=x//1
print(str(h)+":"+str(m)+":"+str(s))
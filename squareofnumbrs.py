a = input("enter the numbers separate by commas:", ).split(',')
print(a)
result = map(lambda x:int(x)*2,a)
print(list(result))
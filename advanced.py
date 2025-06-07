# Walrus
# if(n:=len([1,2,3,4,5]))>4:
#   print(n)

#type

'''
n:int=5
name:str="adarsh"
def sum(a:int,b:int )->int:
  return a+b
'''

#Match Case
'''
def match_status(status):
  match status:
    case 200:
      return "ok"
    case 300:
      return"not found"
    case _:
      return"unknown found"
print(match_status(404))   
'''

#exception
'''
try:
  a=int(input("enter a number: "))
  print(a)
except Exception as e:
  print(e)
  '''

# a=int(input("enter a number: "))
# b=int(input("enter num: "))
# if(b==0):
#   raise ZeroDivisionError("Do not enter zero!")
# else:
#   print(a/b)


'''list comprehence'''

l=[1,2,3,4,5]
squared_l=[i*i for i in l]
print(squared_l)
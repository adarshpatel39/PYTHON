# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()

# st="hi adasrh"
# f=open("file.txt","a")
# f.write(st)
# f.close()

with open("file.txt","rb") as f:
  
  print(f.read())
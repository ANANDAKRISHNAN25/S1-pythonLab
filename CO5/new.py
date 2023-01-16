fn=open("demo.txt",'r')
s=fn.readline()
print(s)

print(fn.closed)
print(fn.mode)
print(fn.name)
fn.close()


#to open a new file and write in it and then read it again
fo=open("demo2.txt",'w')
fo.write("python is great")
fo.close()
fo=open("demo2.txt",'r')
str=fo.read();
print("Read string is :",str)
fo.close()

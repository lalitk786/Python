f=open('a/name1.xml','r')
print("Enter")
name=input()
for line in f:
    line=line.split()
    path1='location="'
    path2=("/home/lalitk/Oracle/Middleware/Oracle_Home/user_projects/domains/%s"%name)
    path3='"/>'
    path=path1+path2+path3
    print(path)
    if path in line:
        print("Yes it is")
    else:
        print("NO")
    print (line)
print("Ended Successfully...")

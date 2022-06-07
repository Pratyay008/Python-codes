f=open("sample.txt", "r")
data=f.read()
if "document" in data:
    print("document is present")
else:
    print("document is not present")
f.close()

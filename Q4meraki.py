new_file=open("qustion3.txt","w")
for i in new_file :
    if "delhi" in i:
        new_file=open("delhi.txt","a")
        new_file.write(i)
    elif "Shimla" in i:
        new_file=open("Shimla.txt","a")
        new_file.write(i)
    else:
        new_file=open("other.txt","a")
        new_file.write(i)
new_file.close()
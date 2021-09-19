# new_file=open("people1_exercise.txt","r")
# count=0
# for i in new_file:
#     count=count+1
# print(count)
# new_file.close()

new_file=open("people1_excercise.txt",'r')
line=new_file.readlines()
i=0
count=0
while i<len(line):
    count+=1
    i+=1
print(count)
new_file.close() 







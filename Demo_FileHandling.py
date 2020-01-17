

#Writing in to file
Mytext = input("Enter your text for writing in file ")
myfile = open("details.csv","w+")
myfile.write(Mytext)
myfile.close()


#creating object of file
myfile = open("details.csv","r+")
#reading file
text = myfile.readlines()
#printing values of file
print(text)


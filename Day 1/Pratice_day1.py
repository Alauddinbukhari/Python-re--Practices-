import os
print(os.getcwd())
print("Hello,This is my practice program in a long time" )

print(os.name)

#create a directory in this current path and a directory again in that path

# create a directory into this folder

# change the path to that directroy  or go inside that directory
#
#
# create another directory


dir_name=["hello","aqeel","owaise","fahad"]
for dir in dir_name:
    os.makedirs(dir)
    current_working_dir= os.getcwd()
    os.chdir(f"{current_working_dir}/{dir}")
    print(os.getcwd())

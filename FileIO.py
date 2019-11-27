#Reading Text Files consists of 3 steps
#Open File
#Read In file (Either one line at a time, or all together)
#Close File

#reading program into python
#open, path to file, 'r' = read only
#jabber = open("C:\\Users\\matthanderson\\Documents\\PythonSamples\\sample.txt", 'r')

#if working text file is already in project folder, path doesn't need to be specified
#use the .lower method allows us to do a comparison regardless of what case the text is in
# jabber = open('sample.txt', 'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line)
#
# jabber.close()

#using with statement, with cleans up once file is no longer needed
#No close statement is needed
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         #using end='' removes the extra space between lines
#         print(line, end='')
#         line = jabber.readline()

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
        #using end='' removes the extra space between lines
    print(lines)

for line in lines:
    print(line, end='')
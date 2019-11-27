#use w for write rather than r for read
#specify a file object to send data to

cities = ['adalaide', 'alice springs', 'darwin', 'melbourne', 'sydney']
# #specifying write either creates the file or overwrites the file
# with open('cities.txt', 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)
#
# cities = []
#
# with open('cities.txt', 'r') as city_file:
#     for line in city_file:
#         #use .strip to remove characters, the below line of code removes \n
#         #strip only removes characters from the beginning or end of a line, would remove things that are a partial match
#         cities.append(line.strip('\n'))
#     print(cities)

# imelda = "More Mayhem", "Imelda May", "2011", ((1, "Pulling the Rug"), (2, "Pyscho"))
# #Prints out a tuple, stores as a string
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

#use eval function to read back in tuple
with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()
#eval not great for using external data
imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
# #write a program to append the times tables to the jabberwocky poem "sample.txt. We want the tables from 2 to 12 (similar to the output from the loops for part 2 lecture 6)
#
# # The first colum of numbers should be right justified. The 2 times table should look like this
# # 1 times 2 is 2
# # 2 times 2 is 4
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# multiplier = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# with open("sample.txt", 'a') as jabber:
#     for n in number:
#         for m in multiplier:
#             calculatedValue = n * m
#             print("{} times {} is {}".format(n, m, calculatedValue), file=jabber)
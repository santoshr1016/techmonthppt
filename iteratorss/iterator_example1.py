# define a list
my_list = [4, 7, 0, 3]

# # get an iterator using iter()
# my_iter = iter(my_list)
#
# ## iterate through it using next()
#
# #prints 4
# print(next(my_iter))
#
# #prints 7
# print(next(my_iter))
#
# ## next(obj) is same as obj.__next__()
#
# #prints 0
# print(my_iter.__next__())
#
# #prints 3
# print(my_iter.__next__())
#
#
# ## This will raise error, no items left
# # next(my_iter)
#
# for i in my_list:
#     print(i)
# # In fact the for loop can iterate over any iterable. A closer look at how the for loop is actually implemented in Python.
# # create an iterator object from that iterable
iter_obj = iter(my_list)
#
# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        print(element)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

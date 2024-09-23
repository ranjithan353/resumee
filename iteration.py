# # #return an iterator from a list,printb each value
# # # city=['mumbai','shagh','new york','tokyo','gfyu' ]
# # # city=iter(city)
# # # print(next(city))
# # # print(next(city))
# # # print(next(city))
# # #strings are also iterable objects,containing a sequence of characters
# # country_name="india"
# # myit = iter (country_name)
# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# class Counter:
#     def __init__(self,low,high):
#         self.current=low
#         self.high=high

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current>self.high:
#             raise StopIteration
#         else:
#             self.current+=1
#             return self.current-1
# counter=Counter(1,5)
# for number in counter:
#     print(number)

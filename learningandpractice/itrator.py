# list1 = [2,4,5,6,2,1]
# for i in list1:
#     print(i)
#
# it = iter(list1)
#
# print(it.__next__())
# print(it.__next__())

class Topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration;
nums = Topten()
print(next(nums))
for i in nums:
    print(i)

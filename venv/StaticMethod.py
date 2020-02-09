# Staic decorator allows us to use a method from a class without declaring an object of the class. The following example shows us how to create a static method.

class Sum:

    @staticmethod
    def get_sum(*args):
        sum_1 = 0
        for i in args:
            sum_1 += i
        return sum_1
def main():
    test_sum = Sum.get_sum(1,2,3,4)
    print(test_sum)

main()
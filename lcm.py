import math # using a new function .prod (Python 3.8 +) 

class K:
    def __init__(self, *numbers):
        self.numbers = numbers
        self.factors  = [self.__get_factors(i) for i in numbers]      

    def __get_factors(self, number):
        temp = number
        factors = []
        while temp > 1:
            for i in range(2, temp +1):
                if temp % i == 0:
                    temp /= i
                    temp = int(temp)
                    factors.append(i)
                    break
        return factors

    def __count (self, factors1, factors2):
        item_list = []
        fac1_content = set(factors1)
        for i in fac1_content:
            i_fac1_count = factors1.count(i)
            i_fac2_count = factors2.count(i)
            if i_fac1_count != i_fac2_count:
                for j in range(0, abs(i_fac1_count - i_fac2_count)):
                    item_list.append(i)
        return item_list + factors2

    def get(self):
        item_list = []
        for i in range(0, len(self.factors)):
            item_list = self.__count(item_list, self.factors[i]) 
        return math.prod(item_list) 
    
if __name__ == "__main__":
    print( K(3, 6).get() )       # 6
    print( K(20, 70, 15).get() ) # 420
    print( K(72, 99).get() )     # 792

 



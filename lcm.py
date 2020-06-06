import math # using a new function .prod (Python 3.8 +) 

class K:
    def __init__(self, *numbers):
        self.numbers = numbers
        self.factors  = [self.__get_factors(i) for i in numbers]
        self.common_factors = self.__get_common_factors(self.factors)
        self.max_common_factor = math.prod(self.common_factors) 
        self.lcm = self.__get_lcm()

    def __count_common_factors(self, factors1, factors2):
        item_list = []
        fac1_content = set(factors1)
        for i in fac1_content:
            if i in factors2:
                    item_list.append(i)
        return item_list
         

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

    def __get_lcm(self):
        item_list = []
        for i in range(0, len(self.factors)):
            item_list = self.__count(item_list, self.factors[i]) 
        return math.prod(item_list) 
    
    def __get_common_factors(self, factors):
        item_list = []
        for i in range(0, len(factors)):
            if i != len(factors) - 1:
                temp_factors = factors[i]                
                if i != 0:
                    temp_factors = item_list                   
                item_list = self.__count_common_factors(temp_factors, factors[i+1])
        return item_list
    
if __name__ == "__main__":
    
    k = K( 20, 90, 30 )
    print( k.lcm )
    print( k.factors ) 
    print( k.common_factors ) 
    print( k.max_common_factor )

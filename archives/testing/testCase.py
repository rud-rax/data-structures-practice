
class TestCase :
    '''
Creates a testcase object to define new testcases for a problem. Accepts 2 parameters while creating an object.
First Parameter : Function name to call.
    '''

    def __init__(self,function) -> None:
        self.function = function

    def test(self, params : list , expected_results = None ) :
        '''
Calls the function specified while the object is created using parameters and checks if it matches the expected result.
Return True if the value returned by the called function is equal to the expected value.
First Parameter : Parameter provided for a function to run.
Second Parameter : Expected Result the function should return.
        '''
        return self.function(*params) == expected_results
        

    def runTestcases(self, testcaselist : list  = "all" ) :
        n = 5

        if testcaselist == "all" :
            testcaselist = range(n)

        

        for i in testcaselist :
            print(i)

def add(a,b) :
    return a + b

if __name__ == "__main__" :
    t = TestCase(add)
    print(t.test([3,2] , 5))

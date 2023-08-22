from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    if n<=1:
        return term(n)
    else: 
        return term(n)* product(n-1,term)


def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    if n==0: 
        return start
    else:
        return merger(term(n), accumulate(merger,start,n-1,term))
    

def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, n ,term)
    


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n ,term)


def funception(func1, start):
    """ Takes in a function (function 1) and a start value.
    Returns a function (function 2) that will find the product of
    function 1 applied to the range of numbers from
    start (inclusive) to stop (exclusive)

    >>> def func1(num):
    ...     return num + 1
    >>> func2_1 = funception(func1, 0)
    >>> func2_1(3)    # func1(0) * func1(1) * func1(2) = 1 * 2 * 3 = 6
    6
    >>> func2_2 = funception(func1, 1)
    >>> func2_2(4)    # func1(1) * func1(2) * func1(3) = 2 * 3 * 4 = 24
    24
    >>> func2_3 = funception(func1, 3)
    >>> func2_3(2)    # Returns func1(3) since start >= stop
    4
    >>> func2_4 = funception(func1, 3)
    >>> func2_4(3)    # Returns func1(3) since start >= stop
    4
    >>> func2_5 = funception(func1, -2)
    >>> func2_5(-3)    # Returns None since start < 0
    >>> func2_6 = funception(func1, -1)
    >>> func2_6(4)    # Returns None since start < 0
    """
    "*** YOUR CODE HERE ***"
    
    def helper(stop):
        product=1
        if start<0:
            return None
        if start>= stop:
            return func1(start)
        else: 
            for i in range(start,stop):
                product *= func1(i)
            return product
    return helper


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n%10 ==8:           
        return 1 + num_eights(n//10)
    elif n<10:
        return 0
    else:
        return num_eights(n//10)

    



def waves(n):
    """Return whether n is balanced.

    >>> waves(1)
    True
    >>> waves(10001)
    False
    >>> waves(12233121)
    False
    >>> waves(1313)
    True
    >>> waves(12332023213)
    True
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'waves',
    ...       ['For', 'While'])
    True
    """
    def helper(n, count, prev):
        curr, next, rest = n % 10, (n // 10) % 10, n // 10
        "*** YOUR CODE HERE ***"
        if n<10:
            return (count==0)
       
        elif curr<next and curr<prev:
            return helper(rest,count-1,curr)
            
        elif curr>next and curr>prev:
            return helper(rest,count+1,curr)
        
        elif curr == next:
            return helper(rest ,count, prev)
        
        else:
            return helper(rest,count,curr)


    return helper(n // 10, 0, n % 10)
    
  








def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper (total,current_coin):
        if total ==0:
            return 1
        elif total<0:
            return 0
        elif current_coin==None:
            return 0 
        else:
            return helper(total-current_coin, current_coin)+ helper(total, next_smaller_coin(current_coin))

    return helper(total, 25)
        
        
    
   
    



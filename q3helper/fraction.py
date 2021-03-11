from goody import irange
from goody import type_as_str
import math


class Fraction:
    # Call as Fraction._gcd(...); no self parameter
    # Helper method computes the Greatest Common Divisor of x and y
    @staticmethod
    def _gcd(x: int, y: int) -> int:
        assert x >= 0 and y >= 0, \
            'Fraction._gcd: x(' + str(x) + ') and y(' + str(y) + ') must be >= 0'
        while y != 0:
            x, y = y, x % y
        return x

    # Returns a string that is the decimal representation of a Fraction, with
    #   decimal_places digitst appearing after the decimal points.
    # For example: if x = Fraction(23,8), then x(5) returns '2.75000'
    def __call__(self, decimal_places):
        answer = ''
        num = self.num
        denom = self.denom

        # handle negative values
        if num < 0:
            num, answer = -num, '-'

        # handle integer part
        if num >= denom:
            answer += str(num // denom)
            num = num - num // denom * denom

        # handle decimal part
        answer += '.' + str(num * 10 ** decimal_places // denom)
        return answer

    @staticmethod
    # Call as Fraction._validate_arithmetic(..); with no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), lt (left type) and rt (right type)
    # An example call (from my __add__ method), which checks whether the type of
    #   right is a Fraction or int is...
    # Fraction._validate_arithmetic(right, {Fraction,int},'+','Fraction',type_as_str(right))
    def _validate_arithmetic(v, t: set, op: str, lt: str, rt: str):
        if type(v) not in t:
            raise TypeError('unsupported operand type(s) for ' + op +
                            ': \'' + lt + '\' and \'' + rt + '\'')

    @staticmethod
    # Call as Fraction._validate_relational(..); with no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), and rt (right type)
    def _validate_relational(v, t: set, op: str, rt: str):
        if type(v) not in t:
            raise TypeError('unorderable types: ' +
                            'Fraction() ' + op + ' ' + rt + '()')

    def __init__(self, num=0, denom=1):
        #self.num = num
        #self.denom = denom
        assert type(denom) is int and denom != 0
        assert type(num) is int
        if num == 0:
            denom = 1
        if denom < 0:
            num = -num
            denom = -denom
        a = Fraction._gcd(abs(num), abs(denom))
        denom = int(denom // a)
        num = int(num // a)
        self.num = num
        self.denom = denom

    def __repr__(self):
        return 'Fraction(' + ''.join(str(self.num)) + ',' + ''.join(str(self.denom)) + ')'

    def __str__(self):
        return ''.join(str(self.num)) + '/' + ''.join(str(self.denom))

    def __bool__(self):
        return self.num != 0

    def __getitem__(self, i):
        if i == 1:
            return self.denom
        elif i == 0:
            return self.num
        elif 'denominator'.find(i) == 0:
            return self.denom
        elif 'numerator'.find(i) == 0:
            return self.num
        else:
            raise TypeError

    def __pos__(self):
        a = Fraction(self.num, self.denom)
        return a

    def __neg__(self):
        a = Fraction(-self.num, self.denom)
        return a

    def __abs__(self):
        a = Fraction(abs(self.num), abs(self.denom))
        return a

    def __add__(self, right):
        Fraction._validate_arithmetic(right, {Fraction, int}, '+', 'Fraction', type_as_str(right))
        if type(right) is float:
            raise TypeError
        elif type(right) is not int:
            a = Fraction(((right.num * self.denom) + (right.denom * self.num)), right.denom * self.denom)
        else:
            a = Fraction(((right * self.denom) + self.num), self.denom)
        return a

    def __radd__(self, left):
        Fraction._validate_arithmetic(left, {Fraction, int}, '+', 'Fraction', type_as_str(left))
        if type(left) is float:
            raise TypeError
        elif type(left) is not int:
            a = Fraction(((left.num * self.denom) + (left.denom * self.num)), left.denom * self.denom)
        else:
            a = Fraction(((left * self.denom) + self.num), self.denom)
        return a

    def __sub__(self, right):
        Fraction._validate_arithmetic(right, {Fraction, int}, '-', 'Fraction', type_as_str(right))
        if type(right) is int:
            a = Fraction(self.num-right*self.denom, self.denom)
        else:
            a = Fraction(((right.denom * self.num) - (right.num * self.denom)), right.denom * self.denom)
        return a

    def __rsub__(self, left):
        Fraction._validate_arithmetic(left, {Fraction, int}, '-', 'Fraction', type_as_str(left))
        if type(left) is int:
            a = Fraction(left*self.denom - self.num, self.denom)
        else:
            a = Fraction(((left.num * self.denom) - (left.denom * self.num)), left.denom * self.denom)
        return a

    def __mul__(self, right):
        Fraction._validate_arithmetic(right, {Fraction, int}, '*', 'Fraction', type_as_str(right))
        if type(right) is int:
            a = Fraction(right*self.num, self.denom)
        else:
            a = Fraction(self.num * right.num, self.denom * right.denom)
        return a

    def __rmul__(self, left):
        Fraction._validate_arithmetic(left, {Fraction, int}, '*', 'Fraction', type_as_str(left))
        if type(left) is int:
            a = Fraction(left*self.num, self.denom)
        else:
            a = Fraction(self.num * left.num, self.denom * left.denom)
        return a

    def __truediv__(self, right):
        Fraction._validate_arithmetic(right, {Fraction, int}, '/', 'Fraction', type_as_str(right))
        if type(right) is int:
            a = Fraction(self.num, self.denom*right)
        else:
            a = Fraction(right.denom*self.num, right.num*self.denom)
        return a

    def __rtruediv__(self, left):
        Fraction._validate_arithmetic(left, {Fraction, int}, '/', 'Fraction', type_as_str(left))
        if type(left) is int:
            a = Fraction(self.denom * left, self.num)
        else:
            a = Fraction(self.num, self.denom*left)
        return a

    def __pow__(self, right):
        Fraction._validate_arithmetic(right, {Fraction, int}, '**', 'Fraction', type_as_str(right))
        if right > 0:
            a = Fraction(self.num ** right, self.denom ** right)
        elif right == 0:
            a = 1
        elif right < 0:
            right = -right
            a = Fraction(self.denom ** right, self.num ** right)
        return a

    def __eq__(self, right):
        Fraction._validate_relational(right, {Fraction, int}, '==', type_as_str(right))
        Fraction(self.num, self.denom)
        if type(right) is int:
            if self.num == right*self.denom:
                return True
            else:
                return False
        else:
            Fraction(right.num, right.denom)
            if self.num == right.num and self.denom == right.denom:
                return True
            else:
                return False

    def __lt__(self, right):
        Fraction._validate_relational(right, {Fraction, int}, '<', type_as_str(right))
        Fraction(self.num, self.denom)
        if type(right) is int:
            if (self.num / self.denom) < right:
                return True
            else:
                return False
        else:
            Fraction(right.num, right.denom)
            if (self.num / self.denom) < (right.num / right.denom):
                return True
            else:
                return False

    def __gt__(self, right):
        Fraction._validate_relational(right, {Fraction, int}, '>', type_as_str(right))
        Fraction(self.num, self.denom)
        if type(right) is int:
            if (self.num / self.denom) > right:
                return True
            else:
                return False
        else:
            Fraction(right.num, right.denom)
            if (self.num / self.denom) > (right.num / right.denom):
                return True
            else:
                return False

    # Uncomment this method when you are ready to write/test it
    # If this is pass, then no attributes will be set!
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise NameError
        else:
            self.__dict__[name] = value




##############################


# Newton: pi = 6*arcsin(1/2); see the arcsin series at
# http://mathforum.org/library/drmath/view/54137.html
# Check your results at http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
#   also see http://www.numberworld.org/misc_runs/pi-5t/details.html
def compute_pi(n):
    def prod(r):
        answer = 1
        for i in r:
            answer *= i
        return answer

    answer = Fraction(1, 2)
    x = Fraction(1, 2)
    for i in irange(1, n):
        big = 2 * i + 1
        answer += Fraction(prod(range(1, big, 2)), prod(range(2, big, 2))) * x ** big / big
    return 6 * answer


if __name__ == '__main__':
    # Put in simple tests for Fraction before allowing driver to run

    print()
    import driver

    driver.default_file_name = 'bscq31F20.txt'
    #     driver.default_show_traceback= True
    #     driver.default_show_exception= True
    #     driver.default_show_exception_message= True
    driver.driver()

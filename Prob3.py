##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################


# Class definition
class Fraction:
    def __init__():
        pass

    def __str__():
        '''
        Returns the string numerator/denominator (with no spaces)

        Usage:
        >>> A = Fraction(4,6)
        >>> print(A)
        4/6
        '''
        pass

    def reduce():
        '''
        Returns a new Fraction object of self in simplest form. Does
        NOT simplify self in-place.

        Usage of a method to find the greatest common divisor may be
        useful here, which we have looked at earlier in the semester.

        Output:
            - (Fraction): simplified version of self

        Usage:
        >>> A = Fraction(8,24)
        >>> print(A.reduce())
        1/3
        '''
        pass

    def __float__():
        '''
        Returns self as a floating point number.

        Output:
            - (float): self as a floating point number

        Usage:
        >>> float(Fraction(1,2))
        0.5
        '''
        pass

    def inverse():
        '''
        Returns the inverse of self.

        Output:
            - (Fraction): inverse of self

        Usage:
        >>> A = Fraction(2,3)
        >>> print(A.inverse())
        3/2
        '''
        pass

    def __mul__():
        '''
        Returns the output of self * (either another Fraction or an integer)

        Inputs (beyond self):
            - other (Fraction or Int): The value that is multiplied by self
        Output:
            - (Fraction): the result of the multiplication

        Example Usage:
        >>> A = Fraction(1,2)
        >>> B = Fraction(4,5)
        >>> print(A*B)
        4/10
        >>> print(A*3)
        3/2
        '''
        pass

    def __rmul__():
        '''
        Returns the output of (Fraction or integer) * self

        The reverse multiplication direction as __mul__. Same inputs and outputs.

        Example Usage:
        >>> A = Fraction(1,2)
        >>> B = Fraction(4,5)
        >>> print(B*A)
        4/10
        >>> print(3*A)
        3/2
        '''
        pass

    def __truediv__():
        '''
        Returns the output of self / (fraction or integer)

        Inputs (beyond self):
            - other (Fraction or int): The value for self to be divided by
        Output:
            - (Fraction): the result of the division

        Example Usage:
        >>> A = Fraction(1,2)
        >>> B = Fraction(4,5)
        >>> print(A/B)
        5/8
        >>> print(A/6)
        1/12
        '''
        pass








# Remember that if you don't want to test things
# in the console manually you can add testing lines
# below the following 'if' statement to have them run
# when the program is run directly but not to
# interfere with the autotesting when the program
# is imported
if __name__ == '__main__':
    # Creating a instance of Fraction
    A = Fraction(1,2)

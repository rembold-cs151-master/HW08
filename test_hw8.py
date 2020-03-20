# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest
import os

import Prob2
import Prob3

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_Prob1:
    def test_pdf_present(self):
        assert os.path.isfile('HW8.pdf') == True


class Test_Prob2:
    def report(self,args):
        return f"\nProgram fails to get the correct value with parameters of {args}."

    def test_can_create_instance(self):
        x = Prob2.Queue()
        assert isinstance(x, Prob2.Queue)

    def test_q_has_length(self):
        x = Prob2.Queue()
        assert len(x.q) == 0, 'Queue not initially empty or no data attribute self.q exists?'

    def test_q_add_3(self):
        x = Prob2.Queue()
        x.add(1)
        x.add('hi')
        x.add((2,5))
        assert len(x.q) == 3, 'Queue is improper length after adding 3 items?'

    def test_remove(self):
        x = Prob2.Queue()
        x.add(1)
        x.add(2)
        x.add(3)
        value = x.remove()
        assert len(x.q) == 2, 'Value was not actually removed from the queue?'
        assert value == 1, f'Incorrect value returned from queue. Expected "1" and got "{value}".'

    def test_q_empty(self):
        x = Prob2.Queue()
        x.add('bazinga')
        v = x.remove()
        v = x.remove()
        assert v == 'The queue is empty!', 'Method not handling an empty queue properly! Are you returning the exact string correctly?'


class Test_Prob3:
    def test_can_create_instance(self):
        A = Prob3.Fraction(1,2)
        assert isinstance(A, Prob3.Fraction)

    def test_prints_nicely(self):
        vals = {
                (1,2):'1/2',
                (5,2):'5/2',
                (4,8):'4/8',
                (9,3):'9/3'
                }
        for key in vals:
            A = Prob3.Fraction(*key)
            assert str(A) == vals[key], f'The fraction of Fraction{key} did not print properly as {vals[key]}'

    def test_reduces_proper_value(self):
        vals = {
                (1,2):'1/2',
                (3,6):'1/2',
                (8,24):'1/3',
                (10,100):'1/10'
                }
        for key in vals:
            A = Prob3.Fraction(*key)
            assert str(A.reduce()) == vals[key], f'The fraction of Fraction{key} did not properly reduce to a printed value of {vals[key]}.'
            assert isinstance(A.reduce(), Prob3.Fraction), 'You should still be returning a Fraction type object, but you are not.'

    def test_reduces_proper_mutability(self):
        A = Prob3.Fraction(4,8)
        B = Prob3.Fraction(4,8)
        C = B.reduce()
        assert str(A) == str(B), 'In the process of reducing you changed the value of your Fraction. You want to return a NEW FRACTION without changing anything in place!'

    def test_float_conversion(self):
        vals = {
                (4,5):float(4/5),
                (2,3):float(2/3),
                (7,1):float(7/1),
                }
        for key in vals:
            A = Prob3.Fraction(*key)
            assert float(A) == vals[key], f'Conversion to a float is not equaling the desired value of {vals[key]} for Fraction{key}.'

    def test_inverse(self):
        vals = {
                (3,2):'2/3',
                (1,8):'8/1',
                (2,16):'16/2'
                }
        for key in vals:
            A = Prob3.Fraction(*key)
            assert str(A.inverse()) == vals[key], f'The inverse is not correct. Should be {vals[key]} but is getting a printed value of {str(A.inverse())}'
            assert isinstance(A.inverse(), Prob3.Fraction), 'You should be returning a Fraction object type.'

    def test_multiply_fractions(self):
        vals = {
                ((1,2),(1,2)):'1/4',
                ((3,4),(1,2)):'3/8',
                ((6,3),(1,8)):'6/24',
                }
        for key in vals:
            A = Prob3.Fraction(*key[0])
            B = Prob3.Fraction(*key[1])
            assert str(A*B) == vals[key], f'Multiplying Fraction{key[0]} by Fraction{key[1]} should equal {vals[key]} but is equaling {str(A*B)}'
            assert isinstance(A*B, Prob3.Fraction), 'Multiplying two fractions should return an object of type Fraction.'


    def test_multiply_fraction_by_integer(self):
        vals = {
                ((1,2),3):'3/2',
                ((3,4),2):'6/4',
                ((8,5),10):'80/5'
                }
        for key in vals:
            A = Prob3.Fraction(*key[0])
            B = key[1]
            assert str(A*B) == vals[key], f'Multiplying Fraction{key[0]} by {key[1]} should give {vals[key]} but instead gives {str(A*B)}.'
            assert str(B*A) == vals[key], f'Multiplying {key[1]} by Fraction{key[0]} should give {vals[key]} but instead gives {str(A*B)}.'
            assert isinstance(A*B, Prob3.Fraction), 'Multiplying a fraction by an integer should return an object of type Fraction.'

    def test_divide_by_fraction(self):
        vals = {
                ((1,2),(1,2)):'2/2',
                ((3,4),(1,2)):'6/4',
                ((6,3),(1,8)):'48/3',
                }
        for key in vals:
            A = Prob3.Fraction(*key[0])
            B = Prob3.Fraction(*key[1])
            assert str(A/B) == vals[key], f'Dividing Fraction{key[0]} by Fraction{key[1]} should equal {vals[key]} but is equaling {str(A/B)}'
            assert isinstance(A*B, Prob3.Fraction), 'Dividing a fraction by another fraction should return an object of type Fraction.'
    
    def test_divide_by_integer(self):
        vals = {
                ((1,2),3):'1/6',
                ((3,4),4):'3/16',
                ((6,3),2):'6/6',
                }
        for key in vals:
            A = Prob3.Fraction(*key[0])
            B = key[1]
            assert str(A/B) == vals[key], f'Dividing Fraction{key[0]} by {key[1]} should equal {vals[key]} but is equaling {str(A/B)}'
            assert isinstance(A*B, Prob3.Fraction), 'Dividing a fraction by an integer should return an object of type Fraction.'

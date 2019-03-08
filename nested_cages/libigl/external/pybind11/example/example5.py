#!/usr/bin/env python
from __future__ import print_function
import sys
sys.path.append('.')

from example import Pet
from example import Dog
from example import dog_bark
from example import pet_print

polly = Pet('Polly', 'parrot')
molly = Dog('Molly')
print(polly.name() + " is a " + polly.species())
pet_print(polly)
print(molly.name() + " is a " + molly.species())
pet_print(molly)
dog_bark(molly)
try:
    dog_bark(polly)
except Exception as e:
    print('The following error is expected: ' + str(e))

from example import test_callback1
from example import test_callback2
from example import test_callback3
from example import test_callback4
from example import test_callback5
from example import Example5

def func1():
    print('Callback function 1 called!')

def func2(a, b, c, d):
    print('Callback function 2 called : ' + str(a) + ", " + str(b) + ", " + str(c) + ", "+ str(d))
    return c

class MyCallback(Example5):
    def __init__(self, value):
        Example5.__init__(self, self, value)

    def callback(self, value1, value2):
        print('got callback: %i %i' % (value1, value2))

print(test_callback1(func1))
print(test_callback2(func2))

callback = MyCallback(3)
test_callback3(callback, 4)

test_callback4(lambda i: i+1)
f = test_callback5()
print("func(43) = %i" % f(43))

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:36:41 2021

@author: maths
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, sympify
import math
from sympy import Rational

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:35:04 2021

@author: asmaldone
"""

import sys
import math
import pandas as pd
from sympy import Symbol, sympify
from sympy import Rational



def getTheFuncs():
    theFuncs = ['-3*x^2 - 4*x + 1',
                'x',
                '3*x^2 + 5*x - 2',
                'x^5 - x^4 + 3*x^2 - 22',
                '-3*x^2 - 4*x + 1',
                '-x^4 + 16',
                '-56*x^3 - 22*x + 34',
                '-56*x^3 - 22*x^2 + x',
                '-23*x^3 - x',
                'x^2',
                '-x^2',
                '88*x - 5',
                '-4*x^2 - 3*x',
                '-36*x^6-x^4+3*x-22'
                ]
    return(theFuncs)
    
def getFuncsToTestDegree():
    funcsToTestDegree = ['x','-x',
                         '-2*x',
                         '222*x',
                         'x^2','-x^3','-402*x^5','-14*x^5',
                         'x^2 - x','-x^2 + 3*x - 1','22*x^2',
                         '4*x^7-x^6+x-3','-5*x^5- 3*x + 4',
                         '-254*x^7-x^6+x-3','-x^8-3*x^2',
                         'x^3 + 10*x^2 + 33*x + 36',
                         '4*x^7-x^6+x-3',
                         '4*x^7-x^6+x^2-5',
                         '-x^2',
                         '3*x^4 - 2*x^3 + x',
                         '-2*x^6 - 4*x^5 + x^2',
                         'x^6 - 2*x^5 - 5*x^4 + 6*x^3']
    return(funcsToTestDegree)
    
def getFuncsToTestQuadratics():
    funcsToTestQuadratics = ['x^2 + 2*x - 3',
                             '-3*x^2 + 3*x + 6',
                             '6*x^2 - x - 1',
                             'x^2 - 4*x + 4',
                             'x^5 + 6*x^4 + 11*x^3']
    return(funcsToTestQuadratics)

def getQuadFuncs():
    funcsToTestQuadratics = ['x^2 + 2*x - 3',
                             '-3*x^2 + 3*x + 6',
                             '6*x^2 - x - 1',
                             'x^2 - 4*x + 4',
                             'x^2 + 6*x + 11',
                             'x^2 - 2']
    return(funcsToTestQuadratics)

def preCalcHfuncs():
    funcsToTest1 = ['x^3 - 2*x^2 - 11*x + 12',
                   'x^4 + 4*x^3 - 5*x^2 - 36*x - 36',
                   '24*x^3 - 14*x^2 - x + 1']
    funcsToTest2 = ['15*x^4 - 41*x^3 - 6*x^2 + 18*x - 4',
                   '7*x^5 - 59*x^4 + 213*x^3 - 347*x^2 + 296*x - 78',
                   'x^4 - 2*x^3 + 18*x^2 - 2*x + 17',
                   'x^6 - 2*x^5 + 18*x^4 - 2*x^3 + 17*x^2']
    funcsToTest3 = ['x^4 - 5*x^3 +15*x^2 - 5*x - 26',
                    'x^3 - 2*x^2 + x - 2',
                    'x^6 - 3*x^5 + 7*x^4 - 5*x^3',
                    'x^5 - 8*x^4 + 27*x^3 - 48*x^2 + 46*x - 20']
    funcsToTest4 = ['x^3 - 5*x^2 + 2*x + 12',
                    '2*x^3 - x^2 + 2*x - 1',
                    'x^4 - x^3 - 2*x^2 + 6*x - 4',
                    '8*x^4 - 38*x^3 + 129*x^2 - 82*x + 13',
                    '3*x^5 - 20*x^4 + 36*x^3 - 34*x^2 + 33*x - 14']
    funcsToTest5 = ['x^3 - 2*x^2 - 5*x + 6',
                    '6*x^3 + 5*x^2 - 2*x - 1',
                    '4*x^4 - 4*x^3 - 44*x^2 + 20*x + 120',
                    'x^4 + 5*x^3 + 6*x^2 - 4*x - 8',
                    '12*x^5 - 60*x^3 + 48*x',
                    '4*x^4 + 3*x^3 - 29*x^2 - 5*x + 3']
    return(funcsToTest5)
    
def verifiedFuncs():
        verfiedFuncs = ['-3*x^2 - 4*x + 1',
                        'x',
                        '3*x^2 + 5*x - 2',
                        'x^5 - x^4 + 3*x^2 - 22',
                        '-3*x^2 - 4*x + 1',
                        '-x^4 + 16',
                        '-56*x^3 - 22*x + 34',
                        '-56*x^3 - 22x^2 + x',
                        '-23*x^3 - x',
                        'x^2',
                        '-x^2',
                        '88*x - 5',
                        '-4*x^2 -3*x',
                        '-36*x^6-x^4+3*x-22',
                        '-2*x^4 - 4*x^3 + 1',
                        'x^3+-2*x^2+-5*x^1+6',
                        'x^3 - x',
                        'x^2 - 4*x + 13',
                        'x^5 - 4*x^4 + 13*x^3',
                        'x^3 - 3*x + 2',
                        'x^4 - 2*x^2 + 1',
                        'x^4 - 2*x^3 + 2*x^2 - 2*x + 1',
                        'x^2 + 2*x - 3',
                        '-3*x^2 + 3*x + 6',
                        '6*x^2 - x - 1',
                        '6*x^2 - x - 1',
                        'x^2 - 4*x + 4',
                        'x^2 + 6*x + 11',
                        '2*x^3 - x^2 + 2*x - 1',
                        '4*x^5 - x^4 + 20*x^3 - 5*x^2 + 16*x - 4',
                        '24*x^3 + 46*x^2 - x - 14',
                        '2*x^3 - 9*x^2 + 30*x - 13',
                        'x^3 - 5*x^2 + 3*x +6',
                        '4*x^3 - 3*x^2 - 25*x - 6',
                        'x^5 - 4*x^4 - 7*x^3 + 14*x^2 - 44*x + 120',
                        '3*x^3 - x^2 - x + 4',
                        'x^3 - x^2 + 2*x - 2',
                        '2*x^3 - 7*x^2 + 58*x - 78',
                        '2*x^5 + x^4 - 2*x - 1',
                        'x^4+x^3-16*x^2-58*x-60',
                        '2*x^5 + x^4 - 2*x - 1',
                        '7*x^2 - 4*x - 8',
                        '-x^4 + 16']
        return(verfiedFuncs)
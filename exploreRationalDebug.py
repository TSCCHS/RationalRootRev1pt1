# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 06:55:23 2022

@author: asmaldone
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:49:56 2021

@author: maths
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:13:52 2021

@author: asmaldone
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:16:11 2021

@author: asmaldone
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:33:10 2021

@author: asmaldone
"""


import sys
import math
import pandas as pd
from sympy import Symbol, sympify
from sympy import Rational


from parseLib             import *
from plotLib              import *
from polynomialLib        import *
from functionTestLib      import *
from rationalRootLib      import *
from functionMathRoutines import *
from exploreRationalLib   import *


def main(argv):
    '''
    The main routine

    Tony Smaldone
    '''
    
    #https://www.calculatorsoup.com/calculators/math/factors.php
    #https://www.mathsisfun.com/numbers/factors-all-tool.html
    #https://realpython.com/python-strings/
    
    print('\n\n\n\tWelcome To Root Finding\n')
    
    theFuncs = verifiedFuncs()
    #theFuncs = ['x^3 - 3*x^2 + 7*x - 5',
                #'x^4 - 3*x^3 + 7*x^2 - 5*x',
                #'x^6 - 3*x^5 + 7*x^4 - 5*x^3']
    #theFuncs = ['x^3 - 3*x^2 + 7*x - 5',
                #'x^4 - 3*x^3 + 7*x^2 - 5*x',
                #]
    #theFuncs = ['x^4 - 5*x^3 + 15*x^2 - 5*x - 26',
                #'x^5 - 5*x^4 + 15*x^3 - 5*x^2 - 26*x',
                #'x^7 - 5*x^6 + 15*x^5 - 5*x^4 - 26*x^3']
    #theFuncs = ['-3*x^2 - 4*x + 1',
                #'x','x^5 - x^4 + 3*x^2 - 22',
                #'-x^4 + 16',
                #'-56*x^3 - 22*x^2 + 34',
                #'-56*x^3 - 22*x^2 + x',
                #'-23*x^3 - x','x^2','-4*x^2 - 3*x']
    #theFuncs = getFuncsToTestQuadratics()
    #theFuncs = preCalcHfuncs()
    theFuncs = ['x^2 - 2*x + 2']
    for theFunc in theFuncs:
        theRealFunc = theFunc
        print('\nProcessing Function:',theFunc)
        theDegree = getPolyDegree(theFunc)
        (allCoeffs,coeffDict) = getAllCoeffs(theFunc)
        coeffList = formCoeffList(coeffDict,theDegree)
        printProcessFuncInfo(theDegree,coeffList)
        #
        # now get the constant coefficient
        useReducedFunc = False
        theConstCoeff = getConstCoeff(theFunc)
        numRemoved = 0
        if (theConstCoeff == 0):
            (numRemoved,reducedFunc) = zeroConstHandling(coeffList)
            rDegree = getPolyDegree(reducedFunc)
            (rCoeffs,rCoeffDict) = getAllCoeffs(reducedFunc)
            rCoeffList = formCoeffList(rCoeffDict,rDegree)
            theFunc = reducedFunc
            useReducedFunc = True
            printZeroConstInfo(numRemoved,reducedFunc,rDegree,rCoeffList)
        
        # Find Possible Rational Roots

        print('\n\tIdentify Possible Rational Roots')
        if useReducedFunc:
            print('\t\tUsing factored function',theFunc)
        theConstCoeff   = getConstCoeff(theFunc)
        constFactors    = findFactors(theConstCoeff)
        theLeadingCoeff = getLeadingCoeff(theFunc)
        leadingFactors  = findFactors(theLeadingCoeff)
        (posRatlRoots,listOfPosRatlRoots) = getPosRatlRoots(theFunc)
        printRatlRootInfo(theConstCoeff,constFactors,
                          theLeadingCoeff,leadingFactors,
                          posRatlRoots,listOfPosRatlRoots)
        
        # Rational Root Finding Via Function Evaluation
        print('\n\tRational Root Finding Via Function Evaluation')
        if useReducedFunc:
            print('\t\tThere was a constant coefficient of zero')
            print('\t\tWill proceed using the reduced (factored) function')
            print('\t\t\t',theFunc)
        theRoots = findRootsViaFuncEval(theFunc,listOfPosRatlRoots)
        if len(theRoots) == 0:
            print('\t\tNo rational roots found via function evaluation')
        else:
            print('\t\tRational roots found via function evaluation:')
            print('\t\t\t',theRoots)
        if useReducedFunc:
            numRootsToFind = getPolyDegree(theFunc)
        else:
            numRootsToFind = theDegree
        rDegree = getPolyDegree(theFunc)
        if useReducedFunc:
            print('\t\tNow add the zero roots')
            for i in range(0,numRemoved):
                theRoots.append(0)
            print('\t\t\t',theRoots)
        if len(theRoots) != theDegree:
             print('\t\tThere are still',theDegree - len(theRoots),' roots to find')
        else:
             print('\t\tAll roots were found for',theRealFunc)
             print('\t\t\t',theRoots)
        #
        
        # NOW HERE IS WHERE WILL USE SYNTHETIC DIVISION
        print('\n\tRoot Finding Via Synthetic Division')
        if useReducedFunc:
            print('\t\tThere was a constant coefficient of zero')
            print('\t\tWill proceed using the reduced (factored) function')
            print('\t\t\t',theFunc)
        (theRoots,returnCoeffList) = findRootsViaSD(theFunc,listOfPosRatlRoots)
        if len(theRoots) == 0:
            print('\t\tNo rational roots found via synthetic division')
        else:
            print('\t\tRational roots found via synthetic division:')
            print('\t\t\t',theRoots)
        if useReducedFunc:
            numRootsToFind = getPolyDegree(theFunc)
        else:
            numRootsToFind = theDegree
        if useReducedFunc:
            print('\t\tNow add the zero roots')
            for i in range(0,numRemoved):
                theRoots.append(0)
            print('\t\t\t',theRoots)
        if (theDegree - len(theRoots)) == 2:
            print('\t\tThere are still two roots to find; will find the roots via the quadratic formula')
            fromQuadFormula = solveQuadratic(returnCoeffList)
            theRoots.append(fromQuadFormula[0])
            theRoots.append(fromQuadFormula[1])
            print('\t\t\t',fromQuadFormula)
            print('\t\tThe roots found so far')
            print('\t\t\t',theRoots)
        
        if len(theRoots) != theDegree:
             print('\t\tThere are still',theDegree - len(theRoots),' roots to find')
        if len(theRoots) == theDegree:
             print('\t\tAll roots were found for',theRealFunc)
             print('\t\t\t',theRoots)
    #
    print("\nAll Done!")
    print("\nGood-bye.........................\n")
    return()

if __name__ == "__main__" :
    main(sys.argv[1:])
#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Root"], products=["Y_Y"], ownReverse=False)

reverse = "Bond_Dissociation"
reversible = True

reactantNum = 2

productNum = 1

recipe(actions=[
    ['FORM_BOND', '*', 1, '*'],
    ['LOSE_RADICAL', '*', '1'],
])

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 * R u1
2 * R u1
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "Root_1R->H",
    group = 
"""
1 * H u1
2 * R u1
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Root_1R->H_2R-inRing",
    group = 
"""
1 * H u1
2 * C u1 r1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * H u1
2 * C u1 r1 {3,S}
3   C u0 {2,S} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,S}
6   C u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R",
    group = 
"""
1 * H u1
2 * C u1 r1 {3,S}
3   C u0 {2,S} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,S}
6   C u0 {5,S} {7,D}
7   C u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-4R!H-=3R!H",
    group = 
"""
1 * H u1
2 * C u1 r1 {3,S}
3   C u0 r1 {2,S} {4,B}
4   C u0 r1 {3,B} {5,[S,D,T,B]}
5   C u0 r1 {4,[S,D,T,B]} {6,S}
6   C u0 r1 {5,S} {7,D}
7   C u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H",
    group = 
"""
1 * H u1
2 * C u1 r1 {3,S}
3   C u0 {2,S} {4,[S,D]}
4   C u0 {3,[S,D]} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,S}
6   C u0 {5,S} {7,D}
7   C u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-3R!H-R",
    group = 
"""
1 * H   u1 r0
2 * C   u1 r1 {3,S}
3   C   u0 r1 {2,S} {4,[S,D]} {8,[S,D,T,B]}
4   C   u0 r1 {3,[S,D]} {5,[S,D,T,B]}
5   C   u0 r1 {4,[S,D,T,B]} {6,S}
6   C   u0 r1 {5,S} {7,D}
7   C   u0 {6,D}
8   R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-4R!H-R",
    group = 
"""
1 * H   u1
2 * C   u1 r1 {3,S}
3   C   u0 r1 {2,S} {4,[S,D]}
4   C   u0 r1 {3,[S,D]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5   C   u0 r1 {4,[S,D,T,B]} {6,S}
6   C   u0 r1 {5,S} {7,D}
7   C   u0 {6,D}
8   R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R-R",
    group = 
"""
1 * H   u1
2 * C   u1 r1 {3,S} {7,[S,D,T,B]}
3   C   u0 r1 {2,S} {4,[S,D,T,B]}
4   C   u0 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C   u0 r1 {4,[S,D,T,B]} {6,S}
6   C   u0 {5,S}
7   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 * H   u1
2 * C   u1 r1 {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B]} {7,[S,D,T,B]}
4   C   u0 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C   u0 r1 {4,[S,D,T,B]} {6,S}
6   C   u0 r1 {5,S}
7   R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * H u1
2 * C u1 r1 {3,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,[B,D,T]}
6   C u0 {5,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 * H   u1 r0
2 * C   u1 r1 {3,[S,D,T,B]}
3   C   u0 r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4   C   u0 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C   u0 r1 {4,[S,D,T,B]} {6,[B,D,T]}
6   C   u0 r1 {5,[B,D,T]}
7   R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R",
    group = 
"""
1 * H u1
2 * C u1 r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,[B,D,T]}
6   C u0 {5,[B,D,T]}
7   C u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_Sp-3R!H-=2R",
    group = 
"""
1 * H u1 r0
2 * C u1 r1 {3,B} {7,[S,D,T,B]}
3   C u0 r1 {2,B} {4,[S,D,T,B]}
4   C u0 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 r1 {4,[S,D,T,B]} {6,[B,D,T]}
6   C u0 r1 {5,[B,D,T]}
7   C u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_N-Sp-3R!H-=2R",
    group = 
"""
1 * H u1 r0
2 * C u1 r1 {3,S} {7,[S,D,T,B]}
3   C u0 r1 {2,S} {4,[S,D,T,B]}
4   C u0 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 r1 {4,[S,D,T,B]} {6,[B,D,T]}
6   C u0 r1 {5,[B,D,T]}
7   C u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Root_1R->H_N-2R-inRing",
    group = 
"""
1 * H u1
2 * R u1 r0
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Root_1R->H_N-2R-inRing_2R->H",
    group = 
"""
1 * H u1
2 * H u1 r0
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Root_1R->H_N-2R-inRing_N-2R->H",
    group = 
"""
1 * H         u1
2 * [C,S,N,O] u1 r0
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S",
    group = 
"""
1 * H u1
2 * S u1 r0
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S_Ext-2S-R",
    group = 
"""
1 * H   u1
2 * S   u1 r0 {3,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S",
    group = 
"""
1 * H       u1
2 * [N,C,O] u1 r0
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C",
    group = 
"""
1 * H u1
2 * C u1 r0
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R",
    group = 
"""
1 * H   u1
2 * C   u1 r0 {3,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C",
    group = 
"""
1 * H   u1
2 * C   u1 r0 {3,D}
3   R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R",
    group = 
"""
1 * H   u1
2 * C   u1 r0 {3,D} {4,S}
3   C   u0 {2,D} {5,[S,D,T,B]}
4   C   u0 {2,S}
5   R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,D}
3   C u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R",
    group = 
"""
1 * H u1 r0
2 * C u1 r0 {3,D}
3   C u0 r0 {2,D} {4,D}
4   C u0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,D}
3   O u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C",
    group = 
"""
1 * H   u1
2 * C   u1 r0 {3,[B,S,T]}
3   R!H u0 {2,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S} {4,S}
3   C u0 {2,S}
4   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S} {4,S} {5,S}
3   C u0 {2,S}
4   C u0 {2,S}
5   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Ext-3R!H-R",
    group = 
"""
1 * H   u1
2 * C   u1 r0 {3,S} {4,S} {5,S}
3   C   u0 r0 {2,S} {7,[S,D,T,B]}
4   C   u0 r0 {2,S}
5   C   u0 {2,S} {6,D}
6   C   u0 r0 {5,D}
7   R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S} {4,S}
3   C u0 {2,S} {5,D}
4   C u0 {2,S}
5   C u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * H   u1 r0
2 * C   u1 r0 {3,S} {4,S}
3   C   u0 r0 {2,S} {5,D}
4   C   u0 r0 {2,S} {6,[S,D,T,B]}
5   C   u0 r0 {3,D}
6   R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->S",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,[B,S,T]}
3   S u0 {2,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,[B,S,T]}
3   C u0 {2,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 {2,S} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 {2,S} {4,D}
4   C u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * H u1 r0
2 * C u1 r0 {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D} {5,S}
5   C u0 r1 {4,S} {6,S}
6   C u0 r1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * H u1 r0
2 * C u1 r0 {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D} {5,S}
5   C u0 r1 {4,S} {6,[B,D,T]}
6   C u0 r1 {5,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 r0 {2,S} {4,D}
4   C u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 {2,S} {4,[B,S,T]}
4   C u0 {3,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 {2,S} {4,[B,T]}
4   C u0 {3,[B,T]}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing",
    group = 
"""
1 * H u1 r0
2 * C u1 r0 {3,S}
3   C u0 r1 {2,S} {4,[B,T]}
4   C u0 {3,[B,T]}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing",
    group = 
"""
1 * H u1
2 * C u1 r0 {3,S}
3   C u0 r0 {2,S} {4,T}
4   C u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R",
    group = 
"""
1 * H   u1
2 * C   u1 r0 {3,S}
3   C   u0 r0 {2,S} {4,T}
4   C   u0 r0 {3,T} {5,[S,D,T,B]}
5   R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_N-Sp-3C-2C",
    group = 
"""
1 * H u1 r0
2 * C u1 r0 {3,T}
3   C u0 {2,T}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C",
    group = 
"""
1 * H     u1
2 * [N,O] u1 r0
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R",
    group = 
"""
1 * H     u1
2 * [N,O] u1 r0 {3,[S,D,T,B]}
3   R!H   ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_2NO->N",
    group = 
"""
1 * H   u1
2 * N   u1 r0 {3,[S,D,T,B]}
3   R!H ux r0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N",
    group = 
"""
1 * H   u1
2 * O   u1 r0 {3,S}
3   R!H ux {2,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_3R!H->C",
    group = 
"""
1 * H u1 r0
2 * O u1 r0 {3,S}
3   C ux {2,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_N-3R!H->C",
    group = 
"""
1 * H u1 r0
2 * O u1 r0 {3,S}
3   O ux {2,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Root_N-1R->H",
    group = 
"""
1 * [Cl,C,N,Si,S,O] u1
2 * R               u1
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Root_N-1R->H_1CClNOSSi->N",
    group = 
"""
1 * N u1
2 * R u1
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R",
    group = 
"""
1 * N   u1
2 * R   u1 {3,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0",
    group = 
"""
1 * N   u1
2 * R   u1 {3,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_2R->C",
    group = 
"""
1 * N   u1 r0
2 * C   u1 r0 {3,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C",
    group = 
"""
1 * N     u1
2 * [N,O] u1 {3,S}
3   R!H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C",
    group = 
"""
1 * N     u1
2 * [N,O] u1 {3,S}
3   C     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R",
    group = 
"""
1 * N     u1 r0 {4,[S,D,T,B]}
2 * [N,O] u1 r0 {3,S}
3   C     u0 {2,S}
4   R!H   ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C",
    group = 
"""
1 * N     u1
2 * [N,O] u1 {3,S}
3   [N,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R",
    group = 
"""
1 * N     u1 {4,[S,D]}
2 * [N,O] u1 {3,S}
3   [N,O] u0 {2,S}
4   O     u0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->N",
    group = 
"""
1 * N     u1 {4,[S,D]}
2 * N     u1 {3,S}
3   [N,O] u0 r0 {2,S}
4   O     u0 r0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->N",
    group = 
"""
1 * N     u1 {4,[S,D]}
2 * O     u1 {3,S}
3   [N,O] u0 r0 {2,S}
4   O     u0 r0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0",
    group = 
"""
1 * N u1
2 * O u1 {3,S}
3   O u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R",
    group = 
"""
1 * N   u1 r0 {4,[S,D,T,B]}
2 * O   u1 r0 {3,S}
3   O   u1 {2,S}
4   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-1N-R",
    group = 
"""
1 * N   u1 {3,[S,D,T,B]}
2 * R   u1
3   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R",
    group = 
"""
1 * N   u1 {3,[S,D,T,B]} {4,[S,D,T,B]}
2 * R   u1
3   R!H ux {1,[S,D,T,B]}
4   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_2R->C",
    group = 
"""
1 * N   u1 {3,[S,D,T,B]} {4,[S,D,T,B]}
2 * C   u1
3   R!H ux {1,[S,D,T,B]}
4   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C",
    group = 
"""
1 * N   u1 r0 {3,[S,D,T,B]} {4,[S,D,T,B]}
2 * O   u1 r0
3   R!H ux {1,[S,D,T,B]}
4   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Root_N-1R->H_N-1CClNOSSi->N",
    group = 
"""
1 * [S,C,O] u1
2 * R       u1
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O",
    group = 
"""
1 * O u1
2 * R u1
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R",
    group = 
"""
1 * O   u1 {3,S}
2 * R   u1
3   R!H ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R",
    group = 
"""
1 * O   u1 {3,S}
2 * R   u1 {4,[S,D,T,B]}
3   R!H ux {1,S}
4   R!H u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R",
    group = 
"""
1 * O   u1 {3,S}
2 * C   u1 {4,[S,D,T,B]}
3   O   u1 {1,S}
4   C   u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R",
    group = 
"""
1 * O   u1 {3,S}
2 * C   u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
3   O   u1 {1,S}
4   C   u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H ux {4,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R",
    group = 
"""
1 * O   u1 r0 {3,S}
2 * C   u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
3   O   u1 {1,S}
4   C   u0 {2,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5   R!H ux {4,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]}
7   R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {3,S}
2 * C   u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
3   O   u1 r0 {1,S}
4   C   u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   C   u0 {4,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]}
7   R!H ux {5,[S,D,T,B]}
8   R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing",
    group = 
"""
1 * O u1 r0 {3,S}
2 * C u1 r1 {4,B} {6,B}
3   O u1 r0 {1,S}
4   C u0 r1 {2,B} {5,B}
5   C u0 r1 {4,B}
6   C u0 r1 {2,B}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing",
    group = 
"""
1 * O   u1 {3,S}
2 * C   u1 r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
3   O   u1 {1,S}
4   C   u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   C   u0 {4,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R",
    group = 
"""
1 * O u1 {3,S}
2 * C u1 {4,S}
3   O u1 {1,S}
4   C u0 {2,S} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H",
    group = 
"""
1 * O u1 r0 {3,S}
2 * C u1 {4,S}
3   O u1 r0 {1,S}
4   C u0 {2,S} {5,S}
5   C u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * O u1 {3,S}
2 * C u1 {4,S}
3   O u1 {1,S}
4   C u0 {2,S} {5,[B,D,T]}
5   C u0 {4,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing",
    group = 
"""
1 * O u1 {3,S}
2 * C u1 r0 {4,S}
3   O u1 {1,S}
4   C u0 r1 {2,S} {5,[B,D,T]}
5   C u0 {4,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing",
    group = 
"""
1 * O u1 {3,S}
2 * C u1 r0 {4,S}
3   O u1 {1,S}
4   C u0 r0 {2,S} {5,[B,D,T]}
5   C u0 {4,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R",
    group = 
"""
1 * O u1 {3,S}
2 * C u1 r0 {4,[B,D]}
3   O u1 {1,S}
4   C u0 {2,[B,D]} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R",
    group = 
"""
1 * O   u1 {3,S}
2 * C   u1 {4,S} {5,[S,D,T,B]}
3   R!H ux {1,S}
4   R!H u0 {2,S}
5   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O",
    group = 
"""
1 * O   u1 r0 {3,S}
2 * C   u1 {4,S} {5,S}
3   R!H ux r0 {1,S}
4   O   u0 {2,S}
5   C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O",
    group = 
"""
1 * O   u1 {3,S}
2 * C   u1 {4,S} {5,[S,D,T,B]}
3   R!H ux {1,S}
4   C   u0 {2,S}
5   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R",
    group = 
"""
1 * O   u1 {3,S}
2 * C   u1 {4,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H ux {1,S}
4   C   u0 {2,S}
5   R!H ux {2,[S,D,T,B]}
6   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->C",
    group = 
"""
1 * O   u1 r0 {3,S}
2 * C   u1 {4,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
3   C   ux r0 {1,S}
4   C   u0 {2,S}
5   R!H ux {2,[S,D,T,B]}
6   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->C",
    group = 
"""
1 * O   u1 r0 {3,S}
2 * C   u1 {4,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
3   O   ux r0 {1,S}
4   C   u0 {2,S}
5   R!H ux {2,[S,D,T,B]}
6   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->C",
    group = 
"""
1 * O u1 {3,S}
2 * C u1 {4,S} {5,S}
3   C ux {1,S}
4   C u0 {2,S}
5   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->C",
    group = 
"""
1 * O u1 {3,S}
2 * C u1 {4,S} {5,S}
3   O ux {1,S}
4   C u0 {2,S}
5   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R",
    group = 
"""
1 * O   u1 {3,S}
2 * R   u1 {4,S}
3   R!H ux {1,S}
4   C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C",
    group = 
"""
1 * O u1 r0 {3,S}
2 * C u1 r0 {4,S}
3   O u1 r0 {1,S}
4   C u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C",
    group = 
"""
1 * O   u1 r0 {3,S}
2 * O   u1 {4,S}
3   R!H ux r0 {1,S}
4   C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R",
    group = 
"""
1 * O   u1 {3,S}
2 * C   u1 {4,D}
3   O   u1 {1,S}
4   R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C",
    group = 
"""
1 * O u1 r0 {3,S}
2 * C u1 {4,D}
3   O u1 r0 {1,S}
4   C u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {3,S}
2 * C u1 {4,D}
3   O u1 r0 {1,S}
4   O u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C",
    group = 
"""
1 * O   u1 {3,S}
2 * C   u1
3   R!H ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_3R!H->C",
    group = 
"""
1 * O u1 r0 {3,S}
2 * C u1
3   C ux r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {3,S}
2 * C u1 r0
3   O u1 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C",
    group = 
"""
1 * O     u1 {3,S}
2 * [S,O] u1
3   R!H   ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N",
    group = 
"""
1 * O     u1 r0 {3,S}
2 * [S,O] u1
3   N     ux r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N",
    group = 
"""
1 * O     u1 {3,S}
2 * [S,O] u1
3   [C,O] ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->S",
    group = 
"""
1 * O     u1 {3,S}
2 * S     u1 r0
3   [C,O] ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->S",
    group = 
"""
1 * O     u1 {3,S}
2 * O     u1 r0
3   [C,O] ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C",
    group = 
"""
1 * O u1
2 * C u1
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0
2 * C   u1 {3,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_N-2R->C",
    group = 
"""
1 * O     u1
2 * [S,O] u1 r0
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O",
    group = 
"""
1 * [C,S] u1
2 * R     u1
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C",
    group = 
"""
1 * C u1
2 * R u1
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing",
    group = 
"""
1 * C u1 r1
2 * C u1
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C",
    group = 
"""
1 * C u1 r1 {3,S}
2 * C u1
3   C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing",
    group = 
"""
1 * C u1 r1 {3,S}
2 * C u1 r1
3   C u0 r1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing",
    group = 
"""
1 * C u1 r1 {3,S}
2 * C u1 r0
3   C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R",
    group = 
"""
1 * C   u1 r1 {3,S}
2 * C   u1 r0 {4,[S,D,T,B]}
3   C   u0 r1 {1,S}
4   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C",
    group = 
"""
1 * C u1 r1 {3,B}
2 * C u1
3   C u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R",
    group = 
"""
1 * C u1 r1 {3,B}
2 * C u1 {4,[S,D,T,B]}
3   C u0 {1,B}
4   C u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing",
    group = 
"""
1 * C u1 r1 {3,B}
2 * C u1 r1 {4,[S,D,T,B]}
3   C u0 r1 {1,B}
4   C u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing",
    group = 
"""
1 * C u1 r1 {3,B}
2 * C u1 r0 {4,[S,D,T,B]}
3   C u0 {1,B}
4   C u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R",
    group = 
"""
1 * C u1 r1 {3,B}
2 * C u1 r0 {4,S}
3   C u0 r1 {1,B}
4   C u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R",
    group = 
"""
1 * C u1 r1 {3,B}
2 * C u1 r0 {4,[B,D]}
3   C u0 r1 {1,B}
4   C u0 r0 {2,[B,D]}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0
2 * R u1
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R",
    group = 
"""
1 * C   u1 r0
2 * R   u1 {3,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R",
    group = 
"""
1 * C   u1 r0
2 * C   u1 {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R",
    group = 
"""
1 * C   u1 r0
2 * C   u1 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
5   R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {6,[S,D,T,B]}
2 * C   u1 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
5   R!H ux {2,[S,D,T,B]}
6   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C",
    group = 
"""
1 * C   u1 r0 {6,[S,D,T,B]}
2 * C   u1 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
5   R!H ux {2,[S,D,T,B]}
6   C   ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {6,[S,D,T,B]} {7,[S,D,T,B]}
2 * C   u1 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
5   R!H ux {2,[S,D,T,B]}
6   C   ux {1,[S,D,T,B]}
7   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {6,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
2 * C   u1 r0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
5   R!H ux {2,[S,D,T,B]}
6   C   u0 r0 {1,S}
7   R!H ux {1,[S,D,T,B]}
8   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->C",
    group = 
"""
1 * C   u1 r0 {6,[S,D,T,B]} {7,[S,D,T,B]}
2 * C   u1 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
5   R!H ux {2,[S,D,T,B]}
6   C   ux {1,[S,D,T,B]}
7   C   ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->C",
    group = 
"""
1 * C   u1 r0 {6,S} {7,[S,D,T,B]}
2 * C   u1 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
5   R!H ux {2,[S,D,T,B]}
6   C   u0 {1,S}
7   O   u0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R",
    group = 
"""
1 * C   u1 r0 {6,S}
2 * C   u1 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]}
4   R!H ux {2,[S,D,T,B]}
5   R!H ux {2,[S,D,T,B]}
6   C   u0 {1,S} {7,[S,D,T,B]}
7   R!H ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C",
    group = 
"""
1 * C             u1 r0 {6,[S,D,T,B]}
2 * C             u1 r0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H           ux {2,[S,D,T,B]}
4   R!H           ux {2,[S,D,T,B]}
5   R!H           ux {2,[S,D,T,B]}
6   [Cl,N,O,S,Si] u0 r0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,D} {4,S}
3   O u0 {2,D}
4   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {5,[S,D,T,B]}
2 * C   u1 {3,D} {4,S}
3   O   u0 {2,D}
4   C   u0 {2,S}
5   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {5,[S,D,T,B]}
2 * C u1 {3,D} {4,S}
3   O u0 {2,D}
4   C u0 {2,S}
5   C ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {5,[S,D,T,B]} {6,[S,D,T,B]}
2 * C   u1 {3,D} {4,S}
3   O   u0 {2,D}
4   C   u0 {2,S}
5   C   ux {1,[S,D,T,B]}
6   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C",
    group = 
"""
1 * C u1 r0 {5,[S,D,T,B]} {6,[S,D,T,B]}
2 * C u1 {3,D} {4,S}
3   O u0 {2,D}
4   C u0 {2,S}
5   C ux {1,[S,D,T,B]}
6   C ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C",
    group = 
"""
1 * C             u1 r0 {5,S} {6,[S,D,T,B]}
2 * C             u1 {3,D} {4,S}
3   O             u0 {2,D}
4   C             u0 {2,S}
5   C             u0 r0 {1,S}
6   [Cl,N,O,S,Si] u0 r0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C",
    group = 
"""
1 * C             u1 r0 {5,[S,D,T,B]}
2 * C             u1 {3,D} {4,S}
3   O             u0 {2,D}
4   C             u0 {2,S}
5   [Cl,N,O,S,Si] u0 r0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,S} {4,S}
3   C u0 {2,S}
4   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r0
2 * C   u1 r0 {3,S} {4,S}
3   C   u0 r0 {2,S} {5,[S,D,T,B]}
4   C   u0 r0 {2,S}
5   R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {5,[S,D,T,B]}
2 * C   u1 {3,S} {4,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {5,S}
2 * C   u1 r0 {3,S} {4,S}
3   C   u0 r0 {2,S}
4   C   u0 r0 {2,S}
5   C   u0 r0 {1,S} {6,[S,D,T,B]}
6   R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {5,[S,D,T,B]} {6,[S,D,T,B]}
2 * C   u1 {3,S} {4,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   R!H ux {1,[S,D,T,B]}
6   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,D}
3   C u0 {2,D} {4,D}
4   C u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R",
    group = 
"""
1 * C u1 r0 {5,[S,D,T,B]}
2 * C u1 {3,D}
3   C u0 {2,D} {4,D}
4   C u0 {3,D}
5   C u0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C",
    group = 
"""
1 * C u1 r0 {5,S}
2 * C u1 {3,D}
3   C u0 {2,D} {4,D}
4   C u0 {3,D}
5   C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing",
    group = 
"""
1 * C u1 r0 {5,S}
2 * C u1 {3,D}
3   C u0 r0 {2,D} {4,D}
4   C u0 r0 {3,D}
5   C u0 r1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing",
    group = 
"""
1 * C u1 r0 {5,S}
2 * C u1 {3,D}
3   C u0 r0 {2,D} {4,D}
4   C u0 r0 {3,D}
5   C u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C",
    group = 
"""
1 * C u1 r0 {5,D}
2 * C u1 r0 {3,D}
3   C u0 r0 {2,D} {4,D}
4   C u0 r0 {3,D}
5   C u0 r0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,S}
3   C u0 {2,S} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,S}
3   C u0 {2,S} {4,D}
4   C u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R",
    group = 
"""
1 * C u1 r0 {5,S}
2 * C u1 {3,S}
3   C u0 {2,S} {4,D}
4   C u0 {3,D}
5   C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {5,S}
2 * C   u1 {3,S}
3   C   u0 {2,S} {4,D}
4   C   u0 {3,D}
5   C   u0 r0 {1,S} {6,[S,D,T,B]}
6   R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,S}
3   C u0 {2,S} {4,T}
4   C u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing",
    group = 
"""
1 * C u1 r0
2 * C u1 r0 {3,S}
3   C u0 r1 {2,S} {4,T}
4   C u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing",
    group = 
"""
1 * C u1 r0
2 * C u1 r0 {3,S}
3   C u0 r0 {2,S} {4,T}
4   C u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R",
    group = 
"""
1 * C   u1 r0
2 * R   u1 {3,S}
3   R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C",
    group = 
"""
1 * C u1 r0
2 * R u1 {3,S}
3   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,S}
3   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {4,[S,D,T,B]}
2 * C   u1 {3,S}
3   C   u0 {2,S}
4   R!H u0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {4,S}
2 * C u1 r0 {3,S}
3   C u0 r0 {2,S}
4   C u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C",
    group = 
"""
1 * C             u1 r0 {4,[S,D,T,B]}
2 * C             u1 {3,S}
3   C             u0 r0 {2,S}
4   [Cl,N,O,S,Si] u0 r0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C",
    group = 
"""
1 * C u1 r0
2 * S u1 {3,S}
3   C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {4,[S,D,T,B]}
2 * S   u1 {3,S}
3   C   u0 {2,S}
4   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * S   u1 {3,S}
3   C   u0 r0 {2,S}
4   R!H ux {1,[S,D,T,B]}
5   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C",
    group = 
"""
1 * C u1 r0
2 * S u1 {3,S}
3   S u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {4,[S,D,T,B]}
2 * S   u1 {3,S}
3   S   u0 r0 {2,S}
4   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R",
    group = 
"""
1 * C   u1 r0
2 * C   u1 {3,[D,T]}
3   R!H u0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,D}
3   O u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {4,D}
2 * C   u1 {3,D}
3   O   u0 {2,D}
4   R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {4,D}
2 * C u1 r0 {3,D}
3   O u0 {2,D}
4   C u0 r0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C",
    group = 
"""
1 * C             u1 r0 {4,D}
2 * C             u1 r0 {3,D}
3   O             u0 {2,D}
4   [Cl,N,O,S,Si] u0 r0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,[D,T]}
3   C u0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,T}
3   C u0 r0 {2,T}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R",
    group = 
"""
1 * C u1 r0
2 * C u1 {3,D}
3   C u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {4,[S,D,T,B]}
2 * C   u1 r0 {3,D}
3   C   u0 {2,D}
4   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C",
    group = 
"""
1 * S u1
2 * S u1
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C_Ext-1S-R",
    group = 
"""
1 * S   u1 r0 {3,[S,D,T,B]}
2 * S   u1 r0
3   R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: Root_1R->H
        L3: Root_1R->H_2R-inRing
            L4: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
                L5: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R
                    L6: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-4R!H-=3R!H
                    L6: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H
                        L7: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-3R!H-R
                        L7: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-4R!H-R
                L5: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R-R
                L5: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R
            L4: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                L5: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
                L5: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R
                    L6: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_Sp-3R!H-=2R
                    L6: Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_N-Sp-3R!H-=2R
        L3: Root_1R->H_N-2R-inRing
            L4: Root_1R->H_N-2R-inRing_2R->H
            L4: Root_1R->H_N-2R-inRing_N-2R->H
                L5: Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S
                    L6: Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S_Ext-2S-R
                L5: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S
                    L6: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C
                        L7: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R
                            L8: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C
                                L9: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R
                                    L10: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R
                                L9: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C
                                    L10: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R
                                L9: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C
                            L8: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C
                                L9: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R
                                    L10: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R
                                        L11: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Ext-3R!H-R
                                    L10: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R
                                        L11: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R_Ext-4R!H-R
                                L9: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->S
                                L9: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S
                                    L10: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C
                                        L11: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R
                                            L12: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C
                                                L13: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing
                                                    L14: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
                                                    L14: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                                                L13: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing
                                            L12: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C
                                                L13: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C
                                                L13: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C
                                                    L14: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing
                                                    L14: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing
                                                        L15: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R
                                    L10: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->S_N-Sp-3C-2C
                    L6: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C
                        L7: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R
                            L8: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_2NO->N
                            L8: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N
                                L9: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_3R!H->C
                                L9: Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_N-3R!H->C
    L2: Root_N-1R->H
        L3: Root_N-1R->H_1CClNOSSi->N
            L4: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R
                L5: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0
                    L6: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_2R->C
                    L6: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
                        L7: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
                            L8: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
                        L7: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
                            L8: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
                                L9: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->N
                                L9: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->N
                L5: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0
                    L6: Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
            L4: Root_N-1R->H_1CClNOSSi->N_Ext-1N-R
                L5: Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R
                    L6: Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_2R->C
                    L6: Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
        L3: Root_N-1R->H_N-1CClNOSSi->N
            L4: Root_N-1R->H_N-1CClNOSSi->N_1COS->O
                L5: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R
                    L6: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R
                        L7: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R
                        L7: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->C
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->C
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->C
                                L9: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->C
                        L7: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C
                        L7: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
                    L6: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C
                        L7: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_3R!H->C
                        L7: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->C
                    L6: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C
                        L7: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N
                        L7: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->S
                            L8: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->S
                L5: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C
                    L6: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C_Ext-2C-R
                L5: Root_N-1R->H_N-1CClNOSSi->N_1COS->O_N-2R->C
            L4: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O
                L5: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C
                    L6: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing
                        L7: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C
                            L8: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing
                            L8: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R
                        L7: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C
                            L8: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
                    L6: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing
                        L7: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R
                            L8: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R
                                                L13: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R
                                                L13: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->C
                                                L13: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->C
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R
                                                L13: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
                                                L13: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R
                            L8: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing
                            L8: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R
                                            L12: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R
                            L8: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C
                                L9: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R
                                    L10: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R
                                        L11: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R
                L5: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C
                    L6: Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C_Ext-1S-R
"""
)

forbidden(
    label = "Cl",
    group = 
"""
1 * Cl u1
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "O4",
    group = 
"""
1   O u1 {2,S}
2 * O u0 {1,S} {3,S}
3 * O u0 {2,S} {4,S}
4   O u1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


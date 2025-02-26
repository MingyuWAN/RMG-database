#!/usr/bin/env python
# encoding: utf-8

name = "Radical Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "Radical",
    group = "OR{RJ, RJ2_triplet, RJ3}",
    thermo = u'RJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "RJ",
    group = 
"""
1 * R u1
""",
    thermo = u'CJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "CJ",
    group = 
"""
1 * C u1
""",
    thermo = u'CsJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CsJ",
    group = 
"""
1 * Cs u1
""",
    thermo = u'Cs_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CH3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.71,0.34,-0.33,-1.07,-2.43,-3.54,-5.43],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol','+|-',0.1),
        S298 = (0.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "Cs_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""Generic primary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CsCsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cs_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "CJCOOH",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.76,-1.34,-1.91,-2.87,-3.6,-4.69],'cal/(mol*K)'),
        H298 = (103.26,'kcal/mol'),
        S298 = (3.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.21,-1.75,-2.24,-3.02,-3.63,-3.63],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "RCCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Isobutyl",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.54,-1.26,-1.92,-2.46,-3.27,-3.84,-3.84],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Neopentyl",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.32,-2.05,-2.65,-3.5,-4.06,-4.87],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (3.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 3047,
    label = "CJC(C)2C=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   CO u0 {1,S} {8,D}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.9,2.5,-1.1,-4.4,-9.7,-13.6,-19],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (7.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3045,
    label = "CJC(C=O)2C",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   CO u0 {1,S} {8,D}
4   CO u0 {1,S} {9,D}
5   C  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,2.5,0.6,-1.9,-6.9,-10.9,-17.1],'J/(mol*K)'),
        H298 = (427,'kJ/mol'),
        S298 = (8.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3067,
    label = "C=CC(C=O)2CJ",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs u1 {1,S} {6,S} {7,S}
3    CO u0 {1,S} {9,D}
4    CO u0 {1,S} {10,D}
5    Cd u0 {1,S} {8,D}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    C  u0 {5,D}
9    O2d u0 {3,D}
10   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,2.4,-0.6,-3.5,-8.4,-12.1,-17.6],'J/(mol*K)'),
        H298 = (429.8,'kJ/mol'),
        S298 = (5.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3066,
    label = "C=CC(C)(C=O)CJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   CO u0 {1,S} {9,D}
4   Cd u0 {1,S} {8,D}
5   C  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
8   C  u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,0.6,-2.7,-5.8,-10.8,-14.4,-19.3],'J/(mol*K)'),
        H298 = (430.6,'kJ/mol'),
        S298 = (9.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3017,
    label = "CJC(C)OC",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * Cs u1 {1,S} {5,S} {6,S}
3   O2s u0 {1,S} {7,S}
4   C  u0 {1,S}
5   H  u0 {2,S}
6   H  u0 {2,S}
7   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,1.8,-2,-5.5,-11,-14.7,-19.8],'J/(mol*K)'),
        H298 = (429.9,'kJ/mol'),
        S298 = (7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3018,
    label = "CJC(C)2O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   O2s u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.1,1.1,-2.1,-5.1,-9.7,-13.1,-18.5],'J/(mol*K)'),
        H298 = (431.1,'kJ/mol'),
        S298 = (5.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3031,
    label = "C=CC(C)(O)CJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   Cd u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
8   C  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.5,-2.7,-5.5,-7.9,-11.8,-14.6,-19],'J/(mol*K)'),
        H298 = (431.9,'kJ/mol'),
        S298 = (9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3065,
    label = "C=CC(O)(C=O)CJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   CO u0 {1,S} {9,D}
4   Cd u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
8   C  u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4,0.9,-2.4,-5.2,-9.7,-13,-18.1],'J/(mol*K)'),
        H298 = (432.3,'kJ/mol'),
        S298 = (6.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3046,
    label = "CJC(C)(C=O)O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   CO u0 {1,S} {8,D}
4   C  u0 {1,S}
5   O2s u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.6,5.1,2.3,-0.9,-6.8,-11.3,-17.8],'J/(mol*K)'),
        H298 = (430.9,'kJ/mol'),
        S298 = (3.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3019,
    label = "CJC(O)2C",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4,-1.5,-5,-7.4,-10.8,-13.6,-18.2],'J/(mol*K)'),
        H298 = (435.3,'kJ/mol'),
        S298 = (8.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3032,
    label = "C=CC(O)2CJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   Cd u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
8   C  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-0.2,-2,-4,-8.1,-11.6,-17.2],'J/(mol*K)'),
        H298 = (431.8,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3044,
    label = "CJC(C)C=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * Cs u1 {1,S} {5,S} {6,S}
3   CO u0 {1,S} {7,D}
4   C  u0 {1,S}
5   H  u0 {2,S}
6   H  u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.6,0.2,-3,-5.8,-10.5,-14.1,-19.3],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3076,
    label = "CJC(C)C=C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.2,-0.5,-4.1,-7.2,-11.8,-15,-19.5],'J/(mol*K)'),
        H298 = (430.1,'kJ/mol'),
        S298 = (9.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 12,
    label = "Benzyl_P",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.492000,0.642000,0.109000,-0.656000,-1.606000,-2.293000,-4.101000],'cal/(mol*K)'),
        H298 = (90.788000,'kcal/mol','+|-',2.4),
        S298 = (-5.163000,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted From  Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
[CH2]C1C=CC=CC=1
""",
)

entry(
    index = 13,
    label = "Allyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62,-0.56,-0.78,-1.12,-1.84,-2.46,-3.49],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (-2.56,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C=CC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83,-1.86,-1.98,-1.99,-2.3,-2.5,-2.5],'cal/(mol*K)'),
        H298 = (80,'kcal/mol'),
        S298 = (-1.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CTCC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Ct u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09,-1.62,-2.01,-2.63,-3.07,-3.48,-3.48],'cal/(mol*K)'),
        H298 = (81,'kcal/mol'),
        S298 = (-3.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 3029,
    label = "C=C(O)CJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   O2s u0 {2,S}
6   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-2.3,-4.6,-7.1,-11,-13.5,-16.6],'J/(mol*K)'),
        H298 = (376.8,'kJ/mol'),
        S298 = (-3.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3062,
    label = "C=C(C=O)CJ",
    group = 
"""
1   Cd u0 {2,S} {3,S} {4,D}
2 * Cs u1 {1,S} {5,S} {6,S}
3   CO u0 {1,S} {7,D}
4   C  u0 {1,D}
5   H  u0 {2,S}
6   H  u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8,-1.2,-2.4,-4.4,-8.2,-11.3,-15.9],'J/(mol*K)'),
        H298 = (374,'kJ/mol'),
        S298 = (-16.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3074,
    label = "CJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-2.6,-4.5,-8.1,-11,-15.6],'J/(mol*K)'),
        H298 = (373.5,'kJ/mol'),
        S298 = (-1.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3082,
    label = "C=C(CJ)C=C=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {5,D}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,D}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-5.6,-5.7,-6.4,-8.2,-10,-12.8],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (-8.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 17,
    label = "Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.84,-1.17,-1.56,-1.95,-2.7,-3.31,-5.31],'cal/(mol*K)'),
        H298 = (89.4,'kcal/mol'),
        S298 = (-0.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 3010,
    label = "CJCO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S} {5,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3038,
    label = "CJC=O",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CO u0 {1,S} {5,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5,1.1,-0.4,-2.3,-6.1,-9.2,-14.4],'J/(mol*K)'),
        H298 = (402.4,'kJ/mol'),
        S298 = (-7.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 16,
    label = "C2JC=O",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CO u0 {1,S} {5,D} {6,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   O2d u0 {2,D}
6   C  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.32,0.19,-0.15,-0.57,-1.43,-2.22,-3.67],'cal/(mol*K)'),
        H298 = (94.4,'kcal/mol'),
        S298 = (-1.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 3039,
    label = "CJCC=O",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   C  u0 {1,S} {3,S}
3   CO u0 {2,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3075,
    label = "CJCC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {5,S} {6,S}
2   C   u0 {1,S} {3,S}
3   Cd  u0 {2,S} {4,D}
4   Cdd u0 {3,D} {7,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.3,-5.8,-8.1,-10.1,-13.4,-15.9,-19.9],'J/(mol*K)'),
        H298 = (420.3,'kJ/mol'),
        S298 = (16.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 18,
    label = "Cs_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-2.33,-3.1,-3.39,-3.75,-4.45,-5.2],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""Generic secondary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "(Cs)2CsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cs_S',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "cyclopropane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""D.F. McMillen, D.M. Golden, HYDROCARBON BOND-DISSOCIATION ENERGIES, Annual Review of Physical Chemistry, 33 (1982) 493-532.. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "bicyclo[1.1.0]butane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {5,S}
4   Cs u0 {1,S} {2,S}
5   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "spiro[2.2]pentane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {3,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (107.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "bicyclo[2.1.0]pentane-secondary-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "bicyclo[2.1.0]pent-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.2,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "tricyclo[1.1.1.0(1,3)]pentane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (111.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "bicyclo[3.1.0]hexane-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {7,S}
2   Cs u0 {1,S} {3,S} {4,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {5,S}
5   C  u0 {1,S} {4,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "cyclobutane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "bicyclo[2.1.0]pentane-secondary-C4",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {5,S} {6,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "bicyclo[2.2.0]hexane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {7,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "bicyclo[3.2.0]heptane-C5-6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "CCJCOOH",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.4,-2,-2.5,-3.27,-3.84,-4.73],'cal/(mol*K)'),
        H298 = (99.98,'kcal/mol'),
        S298 = (4.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "cyclopentene-4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "bicyclo[2.1.1]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (104.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "bicyclo[1.1.1]pentane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "bicyclo[3.1.0]hexane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {3,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (93.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "bicyclo[3.1.0]hexane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {6,S} {8,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {1,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "bicyclo[2.1.1]hexane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "bicyclo[2.1.1]hexane-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "7-norbornyl",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "2-norbornyl",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S} {8,S}
2 * Cs u1 {1,S} {5,S} {9,S}
3   Cs u0 {4,S} {5,S} {7,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {1,S}
9   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.02,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "cycloheptane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {5,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {3,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (92.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "bicyclo[3.2.0]heptane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "bicyclo[3.2.0]heptane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S}
3 * Cs u1 {4,S} {5,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "bicyclo[3.1.1]heptane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "bicyclo[3.1.1]heptane-C3",
    group = 
"""
1   Cs u0 {4,S} {5,S} {7,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "bicyclo[3.1.1]heptane-C6",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "octahydro-pentalene-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {8,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {5,S}
8   C  u0 {4,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "octahydro-pentalene-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {5,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "bicyclo[4.2.0]octane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {5,S}
5   C  u0 {2,S} {4,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "bicyclo[4.2.0]octane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {8,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {3,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "bicyclo[2.2.2]octane-C2",
    group = 
"""
1   Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "tricyclo[2.2.2.0(1,4)]octane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "CCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "RCCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.77,-3.49,-3.9,-4.35,-4.64,-4.64],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (5.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "RCCJCC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    C  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "cyclopentane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {6,S} {7,S}
2    Cs u0 {3,S} {5,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S} {5,S}
5    C  u0 {2,S} {4,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (96.4,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "cyclohexane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {7,S} {8,S}
2    Cs u0 {3,S} {5,S} {9,S} {10,S}
3  * Cs u1 {1,S} {2,S} {11,S}
4    C  u0 {1,S} {6,S}
5    C  u0 {2,S} {6,S}
6    C  u0 {4,S} {5,S}
7    H  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {2,S}
10   H  u0 {2,S}
11   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Benzyl_S",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.044800,-1.300200,-2.199000,-2.554600,-2.587200,-2.807400,-5.633600],'cal/(mol*K)'),
        H298 = (88.064000,'kcal/mol','+|-',2.4),
        S298 = (-4.855400,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted From Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[CH]C1C=CC=CC=1
CC[CH]C1C=CC=CC=1
CCC[CH]C1C=CC=CC=1
CCCC[CH]C1C=CC=CC=1
CCCCC[CH]C1C=CC=CC=1
""",
)

entry(
    index = 26,
    label = "Indenyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   Cd u0 {1,S} {5,D}
4   Cb u0 {2,B} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.36,-0.72,-1.23,-1.77,-2.7,-3.43,-4.54],'cal/(mol*K)'),
        H298 = (81.62,'kcal/mol'),
        S298 = (0.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""A.G. Vandeputte CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Allyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85.6,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "cyclobutene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (91.2,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "cyclopentene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (82.3,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Furuyama, S.; Golden, D. M.; Benson, S. W., "Kinetic Study of the Gas-Phase Reaction c-C5H8+I2 c-C5H6+2HI. Heat of Formation and the Stabilization Energy of the Cyclopentenyl Radical,"Int. J. Chem. Kinet. 1970, 2, 93-99. S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "cyclohexene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {6,S}
5   Cd u0 {3,D} {6,S}
6   C  u0 {4,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Alfassi, Z. B.; Feldman, L., "The Kinetics of Radiation-Induced Hydrogen Abstraction by Trichloromethyl Radicals in the Liquid Phase: Cyclohexene," Int. J. Chem. Kinet. 1981, 13, 771-783. S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 3033,
    label = "C=CCJC(O)C=C",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3   Cd u0 {1,S} {8,D}
4   Cd u0 {2,S} {7,D}
5   H  u0 {1,S}
6   O2s u0 {2,S}
7   C  u0 {4,D}
8   C  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.3,-4.5,-3,-2.8,-3.9,-5.6,-10.2],'J/(mol*K)'),
        H298 = (286.3,'kJ/mol'),
        S298 = (-9.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 27,
    label = "C=CCJC=C",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (76,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "cyclopropenyl-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (90.6,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""DeFrees, D. J.; McIver, R. T., Jr.; Hehre, W. J., "Heats of Formation of Gaseous Free Radicals via Ion Cyclotron Double Resonance Spectroscopy," J. Am. Chem. Soc. 1980, 102, 3334-3338, DOI: 10.1021/ja00530a005 S, Cp copied from C=CCJC=C""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "1,3-cyclopentadiene-allyl",
    group =
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.157, 0.892, -0.937, -2.776, -4.931, -3.793, -4.855],'cal/(mol*K)'),
        H298 = (84.912,'kcal/mol'),
        S298 = (-2.047,'cal/(mol*K)'),
    ),
    shortDesc = u"""Combined experimental and theoretical results of Tranter for 1,2-CPD'yl""",
    longDesc =
u"""
Absolute Enthalpy of formation at 298 K from experiment (1998 Kern and Tranter).
All other  values from theory (2001 Kiefer and Tranter).
""",
)

entry(
    index = 3081,
    label = "C=CCJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-3.8,-3.7,-4.3,-6.1,-8.1,-11.5],'J/(mol*K)'),
        H298 = (318,'kJ/mol'),
        S298 = (-22,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 28,
    label = "Sec_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.2,-1.75,-2.19,-2.91,-3.49,-3.49],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (-0.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 3013,
    label = "CCJCO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S} {5,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3028,
    label = "C=CCJCO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S} {5,S}
3   Cd u0 {1,S} {6,D}
4   H  u0 {1,S}
5   O2s u0 {2,S}
6   C  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,3.2,2.4,1,-1.8,-4.5,-9.8],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-19.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3040,
    label = "CCJC=O",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CO u0 {1,S} {5,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-3.4,-3.4,-4.2,-6.7,-9.2,-13.9],'J/(mol*K)'),
        H298 = (379.1,'kJ/mol'),
        S298 = (-5.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 26,
    label = "CCJCHO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CO u0 {1,S} {5,D} {6,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   O2d u0 {2,D}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36,-1.57,-1.73,-1.89,-2.66,-3.11,-3.5],'cal/(mol*K)'),
        H298 = (91.9,'kcal/mol'),
        S298 = (-2.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 3043,
    label = "C=OCJC=O",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CO u0 {1,S} {5,D}
3   CO u0 {1,S} {6,D}
4   H  u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.9,1.5,0.9,0,-2.5,-5.1,-10.2],'J/(mol*K)'),
        H298 = (382.7,'kJ/mol'),
        S298 = (-13,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3042,
    label = "CCJCC=O",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   C  u0 {1,S} {3,S}
3   CO u0 {2,S} {6,D}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3078,
    label = "CCJC(C)=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   C   u0 {1,S} {6,S}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,S}
7   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-4,-6.2,-7.9,-10.8,-12.9,-16.9],'J/(mol*K)'),
        H298 = (365.4,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 29,
    label = "Cs_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = u'Tertalkyl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Tertalkyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (96.5,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "bicyclo[1.1.0]butane-tertiary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * Cs u1 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (113.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "bicyclo[2.1.0]pentane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "bicyclo[1.1.1]pentane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (106.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C2CJCOOH",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.54,-4.16,-4.44,-4.58,-4.74,-4.88,-5.23],'cal/(mol*K)'),
        H298 = (97.2,'kcal/mol'),
        S298 = (7.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "bicyclo[3.1.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "bicyclo[2.2.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "bicyclo[2.1.1]hexane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "bridgehead_norbornyl",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (107.42,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "bicyclo[3.2.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "bicyclo[4.1.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "bicyclo[3.1.1]heptane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (103.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "octahydro-pentalene-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   C  u0 {4,S} {5,S}
8   C  u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (95.7,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "bicyclo[4.2.0]octane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {8,S}
7   C  u0 {5,S} {8,S}
8   C  u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "bicyclo[2.2.2]octane-C1",
    group = 
"""
1 * Cs u1 {3,S} {6,S} {8,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (101.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "Benzyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.27,-0.78,-1.54,-2.06,-2.74,-3.19,-3.19],'cal/(mol*K)'),
        H298 = (83.8,'kcal/mol'),
        S298 = (-5.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "Allyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   C u0 {1,S}
4   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79,-2.38,-2.74,-2.97,-3.28,-3.55,-3.55],'cal/(mol*K)'),
        H298 = (83.4,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "bicyclo[2.1.0]pent-2-ene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (112.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "bicyclo[2.1.1]hex-2-ene-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "Tert_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.01,-1.74,-2.41,-3.19,-3.65,-3.65],'cal/(mol*K)'),
        H298 = (84.5,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 501,
    label = "C2CJCO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CO u0 {1,S} {5,D} {6,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2d u0 {2,D}
6   R  u0 {2,S}
""",
    thermo = u'C2CJCHO',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C2CJCHO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CO u0 {1,S} {5,D} {6,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2d u0 {2,D}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.2,-1.23,-1.82,-2.87,-3.47,-3.47],'cal/(mol*K)'),
        H298 = (89.8,'kcal/mol'),
        S298 = (-1.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #. Value for Cp1500 taken as equal to Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index = 3016,
    label = "CCJ(C)CO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S} {5,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.8,-9.3,-10.3,-11,-12.4,-13.7,-16.1],'J/(mol*K)'),
        H298 = (369.4,'kJ/mol'),
        S298 = (-0.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3063,
    label = "C=CCJ(C)C=O",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   CO u0 {1,S} {6,D}
4   C  u0 {1,S}
5   C  u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.2,-10.5,-9.4,-9,-9.1,-9.7,-11.5],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-17.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3064,
    label = "C=CCJ(C=O)C=C",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   CO u0 {1,S} {7,D}
4   Cd u0 {1,S} {6,D}
5   C  u0 {2,D}
6   C  u0 {4,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10,-7.5,-6.1,-5.5,-5.6,-6.4,-8.5],'J/(mol*K)'),
        H298 = (307.4,'kJ/mol'),
        S298 = (-27.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3077,
    label = "CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.1,-10,-11.8,-12.9,-14.1,-15.1,-16.9],'J/(mol*K)'),
        H298 = (361.8,'kJ/mol'),
        S298 = (3.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3083,
    label = "C=CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.8,-8.2,-8.9,-9.3,-10.1,-11,-12.9],'J/(mol*K)'),
        H298 = (313.4,'kJ/mol'),
        S298 = (0.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3084,
    label = "C=CCJ(C=C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d  u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.7,-9.3,-8.1,-7.2,-6.8,-7.2,-8.8],'J/(mol*K)'),
        H298 = (287.1,'kJ/mol'),
        S298 = (-27.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 36,
    label = "CsJO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9,3.7,1.6,-0.9,-5.9,-10.3,-17.5],'J/(mol*K)'),
        H298 = (413.3,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 37,
    label = "CsJOH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.25,0.18,-0.26,-0.83,-1.95,-2.85,-4.22],'cal/(mol*K)'),
        H298 = (96.51,'kcal/mol'),
        S298 = (0.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "CsJOC",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   C  u0 {2,S}
""",
    thermo = u'CsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "CsJOCs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   Cs u0 {2,S}
""",
    thermo = u'CsJOCH3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "CsJOCH3",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {1,S}
7   H  u0 {2,S}
8   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16,-0.4,-0.82,-1.33,-2.32,-3.13,-4.37],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN #""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "CsJOCC",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {1,S}
7   H  u0 {2,S}
8   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-1.22,-1.4,-1.71,-3.5,-3.24,-4.42],'cal/(mol*K)'),
        H298 = (96.83,'kcal/mol'),
        S298 = (1.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from data in SUMATHI & GREEN. Values might have large error bars.""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "CsJOCC2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {1,S}
7   H  u0 {2,S}
8   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.75,0.23,-0.43,-1.71,-2.72,-4.19],'cal/(mol*K)'),
        H298 = (96.16,'kcal/mol'),
        S298 = (-0.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "CsJOCC3",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   C  u0 {1,S}
7   H  u0 {2,S}
8   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.08,-0.09,-0.52,-1.06,-2.11,-2.96,-4.27],'cal/(mol*K)'),
        H298 = (95.75,'kcal/mol'),
        S298 = (0.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s      u0 {1,S} {5,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = u'CsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "CsJOC(O)",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO u0 {2,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.91,0.89,0.42,-0.21,-1.5,-2.62,-4.43],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "CsJOC(O)H",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   CO u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.97,0.53,-0.12,-1.54,-2.76,-4.53],'cal/(mol*K)'),
        H298 = (100.88,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "CsJOC(O)C",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   CO u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   C  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.88,0.81,0.31,-0.3,-1.45,-2.47,-4.33],'cal/(mol*K)'),
        H298 = (100.48,'kcal/mol'),
        S298 = (-0.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 3027,
    label = "C=COCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   Cd u0 {2,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-7.2,-8.9,-10.6,-13.6,-15.9,-19.7],'J/(mol*K)'),
        H298 = (409.4,'kJ/mol'),
        S298 = (13.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 48,
    label = "CsJOO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.18,-0.42,-0.79,-1.2,-1.99,-2.63,-3.65],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol'),
        S298 = (-1.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "CsJOOH",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.06,-0.35,-0.76,-1.19,-1.99,-2.64,-3.68],'cal/(mol*K)'),
        H298 = (98.91,'kcal/mol'),
        S298 = (-1.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "CsJOOC",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.48,-0.82,-1.22,-1.99,-2.62,-3.63],'cal/(mol*K)'),
        H298 = (98.34,'kcal/mol'),
        S298 = (-1.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "CCsJO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.4,-1.5,-3.9,-8.6,-12.5,-18.7],'J/(mol*K)'),
        H298 = (402,'kJ/mol'),
        S298 = (3.9,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 52,
    label = "CCsJOH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.65,-0.01,-0.75,-1.43,-2.52,-3.31,-4.47],'cal/(mol*K)'),
        H298 = (95.39,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "CCsJOC",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   C  u0 {2,S}
""",
    thermo = u'CCsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "CCsJOCs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   Cs u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.82,0.53,-0.11,-0.86,-2.2,-3.18,-4.51],'cal/(mol*K)'),
        H298 = (95.41,'kcal/mol'),
        S298 = (0.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CCsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s      u0 {1,S} {5,S}
3   C       u0 {1,S}
4   H       u0 {1,S}
5   [CO,Cd] u0 {2,S}
""",
    thermo = u'CCsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "CCsJOC(O)",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO u0 {2,S} {6,D}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16,0.78,0.05,-0.73,-2.13,-3.24,-4.9],'cal/(mol*K)'),
        H298 = (98.7,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "CCsJOC(O)H",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   CO u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.88,0.16,-0.67,-2.22,-3.43,-5],'cal/(mol*K)'),
        H298 = (98.87,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CCsJOC(O)C",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   CO u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   C  u0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3030,
    label = "C=CCJ(O)C",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2s u0 {1,S} {6,S}
4   H  u0 {1,S}
5   C  u0 {2,D}
6   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.7,-8.4,-10,-11,-12.1,-13.1,-15.5],'J/(mol*K)'),
        H298 = (328.3,'kJ/mol'),
        S298 = (4.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 58,
    label = "CCsJOO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.48,-1.15,-1.68,-2.11,-2.77,-3.26,-4.02],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "CCsJOOH",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39,-1.08,-1.64,-2.08,-2.75,-3.26,-4.03],'cal/(mol*K)'),
        H298 = (97.19,'kcal/mol'),
        S298 = (0.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "CCsJOOC",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.58,-1.21,-1.73,-2.15,-2.8,-3.27,-4.01],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (0.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 3026,
    label = "C=CCJO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-3.9,-3,-3.2,-5.7,-8.6,-13.8],'J/(mol*K)'),
        H298 = (333.9,'kJ/mol'),
        S298 = (-7.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3041,
    label = "OCJC=O",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CO u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.3,-5.6,-7.4,-9.8,-11.2,-14],'J/(mol*K)'),
        H298 = (356.6,'kJ/mol'),
        S298 = (0.2,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 61,
    label = "C2CsJO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2,-7.1,-10.7,-13.4,-16.6,-18.5,-21.2],'J/(mol*K)'),
        H298 = (398.4,'kJ/mol'),
        S298 = (14.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 62,
    label = "C2CsJOH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31,-0.66,-1.54,-2.23,-3.17,-3.8,-4.72],'cal/(mol*K)'),
        H298 = (94.5,'kcal/mol'),
        S298 = (2.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C2CsJOC",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {2,S}
""",
    thermo = u'C2CsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C2CsJOCs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   Cs u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.09,-1.37,-2.49,-3.26,-4.15,-4.63,-5.23],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (3.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C2CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s      u0 {1,S} {5,S}
3   C       u0 {1,S}
4   C       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = u'C2CsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C2CsJOC(O)",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO u0 {2,S} {6,D}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.34,-2.3,-2.99,-3.99,-4.77,-5.98],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (4.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C2CsJOC(O)H",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   CO u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   O2d u0 {2,D}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.03,-1.28,-2.28,-3.1,-4.35,-5.19,-6.06],'cal/(mol*K)'),
        H298 = (99.97,'kcal/mol'),
        S298 = (4.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C2CsJOC(O)C",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   CO u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   O2d u0 {2,D}
7   C  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.4,-2.32,-2.89,-3.62,-4.36,-5.9],'cal/(mol*K)'),
        H298 = (100.25,'kcal/mol'),
        S298 = (4.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C2CsJOO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.89,-2.09,-2.81,-3.24,-3.69,-3.97,-4.43],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol'),
        S298 = (2.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C2CsJOOH",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-2.17,-2.87,-3.3,-3.77,-4.05,-4.49],'cal/(mol*K)'),
        H298 = (96.74,'kcal/mol'),
        S298 = (2.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C2CsJOOC",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.02,-2.75,-3.18,-3.62,-3.88,-4.37],'cal/(mol*K)'),
        H298 = (96.58,'kcal/mol'),
        S298 = (2.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S  ux {1,S}
3   R  ux {1,S}
4   R  ux {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "CsJ-SsHH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.07,-0.32,-0.73,-1.22,-2.18,-2.99,-4.27],'cal/(mol*K)'),
        H298 = (95.34,'kcal/mol'),
        S298 = (1.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "CsJ-SsOsH",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S  ux {1,S}
3   O  ux {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95,-2.60,-2.88,-2.90,-2.72,-2.63,-3.06],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (-0.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = -1,
    label = "CsJ-CSH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    label = "CsJ-CsSsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.79,-1.36,-1.9,-2.82,-3.53,-4.64],'cal/(mol*K)'),
        H298 = (92.87,'kcal/mol'),
        S298 = (1.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 247,
    label = "CsJ-CtSsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.26,-0.02,-0.47,-0.97,-1.95,-2.77,-4.12],'cal/(mol*K)'),
        H298 = (83.48,'kcal/mol'),
        S298 = (-0.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "CsJ-CbSsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32,-0.38,-0.65,-1.01,-1.75,-2.4,-3.57],'cal/(mol*K)'),
        H298 = (84.88,'kcal/mol'),
        S298 = (-0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    label = "CsJ-CdSsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21,-2.77,-2.39,-2.24,-2.39,-2.74,-3.56],'cal/(mol*K)'),
        H298 = (81.92,'kcal/mol'),
        S298 = (0.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "CsJ-C=SSsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CS u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.75,-2.93,-2.07,-1.54,-1.2,-1.31,-2.01],'cal/(mol*K)'),
        H298 = (71.51,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-CCS",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "CsJ-CsCsSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.72,-2.04,-2.88,-3.4,-3.99,-4.36,-4.96],'cal/(mol*K)'),
        H298 = (92.32,'kcal/mol'),
        S298 = (3.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "CsJ-CsCtSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.99,-1.64,-2.18,-2.62,-3.3,-3.82,-4.65],'cal/(mol*K)'),
        H298 = (81.17,'kcal/mol'),
        S298 = (3.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "CsJ-CsCbSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.26,-2.53,-2.75,-3.12,-3.49,-4.43],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "CsJ-CsCdSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4,-4.74,-4.81,-4.59,-4.17,-3.99,-4.12],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (2.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "CsJ-CsC=SSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CS u0 {1,S} {5,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.86,-3.83,-3.41,-2.93,-2.28,-2.07,-2.36],'cal/(mol*K)'),
        H298 = (69.17,'kcal/mol'),
        S298 = (-1.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-SS",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   R  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "CsJ-SsSsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52,-4,-3.64,-3.53,-3.68,-4,-4.72],'cal/(mol*K)'),
        H298 = (90.16,'kcal/mol'),
        S298 = (1.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-CSS",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "CsJ-CsSsSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.36,-4,-4.17,-4.24,-4.37,-4.55,-5],'cal/(mol*K)'),
        H298 = (89.98,'kcal/mol'),
        S298 = (5.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-CtSsSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-CbSsSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-CdSsSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-C=SSsSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   CS u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "CsJ-SsSsSs",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 264,
    label = "CCsJOS",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = u'CCsJOHSH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "CCsJOHSH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   S2s u0 {1,S} {6,S}
4   C  u0 {1,S}
5   H  u0 {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21,-2.38,-2.47,-2.55,-2.89,-3.33,-4.54],'cal/(mol*K)'),
        H298 = (92.6,'kcal/mol'),
        S298 = (1.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC CBS-QB3 1d-hr""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
    label = "CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'CCsJN',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "CCsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-1.4,-1.9,-2.8,-3.4,-4.5],'cal/(mol*K)'),
        H298 = (92.1,'kcal/mol'),
        S298 = (2.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "C2CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = u'CCsJN',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3012,
    label = "OCJO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-8.2,-14.4,-17.5,-19.4,-20.1,-21.5],'J/(mol*K)'),
        H298 = (408.4,'kJ/mol'),
        S298 = (15.1,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 72,
    label = "CdsJ",
    group = 
"""
1 * [Cd,CO] u1
""",
    thermo = u'Cds_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "CdsJO",
    group = 
"""
1 * CO u1 {2,D}
2   O2d u0 {1,D}
""",
    thermo = u'CCJ=O',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "HCdsJO",
    group = 
"""
1 * CO u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.65,-1.19,-1.73,-2.63,-3.32,-4.42],'cal/(mol*K)'),
        H298 = (88.45,'kcal/mol'),
        S298 = (-0.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to formaldehyde from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "CCJ=O",
    group = 
"""
1 * CO u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   C  u0 {1,S}
""",
    thermo = u'CsCJ=O',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "CsCJ=O",
    group = 
"""
1 * CO u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83,-1.43,-1.96,-2.42,-3.16,-3.73,-4.64],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.12,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 3057,
    label = "CC(C)CJ=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * CO u1 {1,S} {5,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1,-5.8,-7.9,-9.9,-13.5,-16.2,-20.3],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3058,
    label = "CC(C)2CJ=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * CO u1 {1,S} {6,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.7,-5,-7.4,-9.6,-13.1,-15.6,-19.9],'J/(mol*K)'),
        H298 = (373.3,'kJ/mol'),
        S298 = (7.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3060,
    label = "CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * CO u1 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.7,-4,-5.4,-7.2,-10.9,-13.9,-18.6],'J/(mol*K)'),
        H298 = (375.2,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3073,
    label = "C=CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * CO u1 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   C  u0 {1,S}
6   C  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.5,2.6,-2.4,-6.5,-12,-15.3,-19.7],'J/(mol*K)'),
        H298 = (373.6,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3071,
    label = "C=CC(C)2CJ=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * CO u1 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-4.2,-7,-9.3,-12.8,-15.4,-19.4],'J/(mol*K)'),
        H298 = (371.9,'kJ/mol'),
        S298 = (10.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3059,
    label = "CC(C)(O)CJ=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * CO u1 {1,S} {6,D}
3   C  u0 {1,S}
4   O2s u0 {1,S}
5   C  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.9,-2.6,-5.6,-8.1,-12,-14.9,-19.6],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (6.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3072,
    label = "C=CC(C)(O)CJ=O",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * CO u1 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   C  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1,-4.5,-7.4,-9.7,-12.7,-15.1,-19.5],'J/(mol*K)'),
        H298 = (375.3,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 83,
    label = "C=CCJ=O",
    group = 
"""
1 * CO u1 {2,S} {3,D}
2   Cd u0 {1,S} {4,D}
3   O2d u0 {1,D}
4   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,2.5,-1.1,-4.5,-9.9,-13.7,-18.9],'J/(mol*K)'),
        H298 = (379.9,'kJ/mol'),
        S298 = (7.2,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3052,
    label = "CCCJ=O",
    group = 
"""
1 * CO u1 {2,S} {4,D}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-3.9,-7,-9.9,-14.5,-17.5,-21.4],'J/(mol*K)'),
        H298 = (378,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3054,
    label = "C=OCCJ=O",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * CO u1 {1,S} {4,D}
3   CO u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2,1.4,-2.8,-6.4,-12,-15.8,-20.4],'J/(mol*K)'),
        H298 = (379.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3056,
    label = "C=OC=OCJ=O",
    group = 
"""
1   CO u0 {2,S} {3,S} {4,D}
2 * CO u1 {1,S} {5,D}
3   CO u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.2,-4.6,-4.4,-4.5,-4.9,-5.7,-7.8],'J/(mol*K)'),
        H298 = (330.2,'kJ/mol'),
        S298 = (-19.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3070,
    label = "C=C(C)CJ=O",
    group = 
"""
1   Cd u0 {2,S} {3,S} {4,D}
2 * CO u1 {1,S} {5,D}
3   C  u0 {1,S}
4   C  u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.8,-6.4,-8.8,-12.5,-15.3,-19.5],'J/(mol*K)'),
        H298 = (381.7,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3055,
    label = "OC=OCJ=O",
    group = 
"""
1   CO u0 {2,S} {3,S} {4,D}
2 * CO u1 {1,S} {5,D}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3,-4.7,-7,-9.5,-14,-17.2,-21.1],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (4.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 84,
    label = "(O)CJO",
    group = 
"""
1 * CO u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = u'(O)CJOC',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "SCJ=O",
    group =
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.30,-0.86,-1.50,-2.06,-2.99,-3.68,-4.70],'cal/(mol*K)'),
        H298 = (86.68,'kcal/mol'),
        S298 = (-1.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 85,
    label = "(O)CJOH",
    group = 
"""
1 * CO u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.02,-0.66,-1.4,-2.12,-3.41,-4.44,-5.79],'cal/(mol*K)'),
        H298 = (100.75,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN #""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "(O)CJOC",
    group = 
"""
1 * CO u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   C  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2,-0.2,-3.5,-6.5,-10.9,-13.6,-17],'J/(mol*K)'),
        H298 = (415.2,'kJ/mol'),
        S298 = (-4.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 87,
    label = "(O)CJOCH3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO u1 {2,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51,-0.11,-0.94,-1.8,-3.34,-4.48,-5.79],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (0.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "(O)CJOCC",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO u1 {2,S} {7,D}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45,-0.13,-0.98,-1.86,-3.43,-4.56,-5.79],'cal/(mol*K)'),
        H298 = (99.49,'kcal/mol'),
        S298 = (0.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOCH2CH3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "(O)CJOCC2",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO u1 {2,S} {7,D}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.74,-0.06,-1.04,-2.01,-3.6,-4.66,-5.77],'cal/(mol*K)'),
        H298 = (98.99,'kcal/mol'),
        S298 = (0.82,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOCH(CH3)2)""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "(O)CJOCC3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO u1 {2,S} {7,D}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   C  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.11,-0.79,-1.8,-2.73,-4.17,-5.06,-5.87],'cal/(mol*K)'),
        H298 = (97.98,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOC(CH3)3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "Cds_P",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.75,-1.36,-1.92,-2.82,-3.49,-4.53],'cal/(mol*K)'),
        H298 = (111.2,'kcal/mol'),
        S298 = (1.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C=C=CJ",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   Cdd u0 {1,D} {4,D}
3   H   u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.45,-1.05,-1.64,-2.15,-2.98,-3.6,-3.6],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "Cds_S",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C=CJC=C",
    group = 
"""
1 * Cd      u1 {2,D} {3,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.19,-0.76,-1.51,-2.01,-2.7,-3.17,-3.17],'cal/(mol*K)'),
        H298 = (99.8,'kcal/mol'),
        S298 = (0.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "cyclobutadiene-C1",
    group = 
"""
1 * Cd u1 {2,D} {4,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (104.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "bicyclo[2.2.0]hexa-1(4),2,5-triene-C2",
    group = 
"""
1   Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (102.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "1,3-cyclopentadiene-vinyl-2",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4 * Cd u1 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.2,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "cyclopropenyl-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fattahi, A.; McCarthy, R. E.; Ahmad, M. R.; Kass, S. R., "Why Does Cyclopropene Have the Acidity of an Acetylene but the Bond Energy of Methane?," J. Am. Chem. Soc. 2003, 125, 11746-11750, DOI: 10.1021/ja035725s. S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "cyclobutene-vinyl",
    group = 
"""
1   C  u0 {2,S} {4,S}
2   C  u0 {1,S} {3,S}
3 * Cd u1 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (112.5,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "bicyclo[2.1.0]pent-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   C  u0 {1,S} {2,S}
4 * Cd u1 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109.8,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (111.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "cyclopentene-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   C  u0 {1,S} {5,S}
3   C  u0 {1,S} {4,S}
4 * Cd u1 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (113.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "bicyclo[2.1.1]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (115.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "1,3-cyclopentadiene-vinyl-1",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index = 3061,
    label = "C=CJC=O",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   CO u0 {1,S} {4,D}
3   C  u0 {1,D}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.4,-2.2,-4.8,-7.2,-11.6,-15.5,-22],'J/(mol*K)'),
        H298 = (462.3,'kJ/mol'),
        S298 = (9.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3079,
    label = "CCCJ=C=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   C   u0 {1,S} {4,S}
3   Cdd u0 {1,D} {5,D}
4   C   u0 {2,S}
5   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6,-3,-4.9,-6.5,-9.4,-11.6,-15.1],'J/(mol*K)'),
        H298 = (420.2,'kJ/mol'),
        S298 = (-2.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3080,
    label = "CC(C)CJ=C=O",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.8,-3.6,-6,-7.8,-10.6,-12.6,-15.8],'J/(mol*K)'),
        H298 = (424,'kJ/mol'),
        S298 = (1.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3085,
    label = "C=C(C)CJ=C=O",
    group = 
"""
1   Cd  u0 {2,S} {4,D} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,D}
5   C   u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.5,-13.7,-14.6,-15,-15.7,-16.3,-17.8],'J/(mol*K)'),
        H298 = (404,'kJ/mol'),
        S298 = (5.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 257,
    label = "S2s-CJ=C",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   S2s u0 {1,S}
3   C  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.16,-0.48,-1.16,-1.76,-2.68,-3.35,-4.45],'cal/(mol*K)'),
        H298 = (104.73,'kcal/mol'),
        S298 = (0.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 3025,
    label = "C=CJO",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.1,-11.8,-15.2,-17.2,-19.2,-20.3,-22],'J/(mol*K)'),
        H298 = (457.4,'kJ/mol'),
        S298 = (26.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 91,
    label = "CtJ",
    group = 
"""
1 * Ct u1 {2,T}
2   Ct u0 {1,T}
""",
    thermo = u'Acetyl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "Acetyl",
    group = 
"""
1 * Ct u1 {2,T}
2   Ct u0 {1,T} {3,S}
3   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.56,-2.27,-2.78,-3.47,-3.97,-3.97],'cal/(mol*K)'),
        H298 = (132.7,'kcal/mol'),
        S298 = (2.11,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "CbJ",
    group = 
"""
1 * Cb u1 {2,B} {3,B}
2   C  u0 {1,B}
3   C  u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41,-1.18,-1.93,-2.69,-3.75,-4.48,-5.24],'cal/(mol*K)'),
        H298 = (113,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from TSANG, S and Cp from THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=SJ",
    group = 
"""
1 * CS u1 {2,D}
2   S2d u0 p2 {1,D}
""",
    thermo = u'C=SJ-H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=SJ-S2s",
    group = 
"""
1 * CS u1 {2,S} {3,D}
2   S2s u0 p2 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "C=SJ-H",
    group = 
"""
1 * CS u1 {2,S} {3,D}
2   H  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.88,-1.47,-1.99,-2.85,-3.49,-4.52],'cal/(mol*K)'),
        H298 = (92.39,'kcal/mol'),
        S298 = (-0.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=SJ-C",
    group = 
"""
1 * CS u1 {2,S} {3,D}
2   C  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "C=SJ-Cd",
    group = 
"""
1 * CS u1 {2,S} {3,D}
2   Cd u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21,-1.76,-2.24,-2.65,-3.3,-3.81,-4.67],'cal/(mol*K)'),
        H298 = (77.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "C=SJ-Cs",
    group = 
"""
1 * CS u1 {2,S} {3,D}
2   Cs u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.8,-2.25,-2.63,-3.24,-3.74,-4.64],'cal/(mol*K)'),
        H298 = (91.94,'kcal/mol'),
        S298 = (0.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "OJ",
    group = 
"""
1 * O u1
""",
    thermo = u'COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "HOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.87,-1.1,-1.36,-1.62,-2.11,-2.53,-3.38],'cal/(mol*K)'),
        H298 = (119.22,'kcal/mol'),
        S298 = (-2.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from NIST values for H2O, OH and H""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   C  ux {1,S}
""",
    thermo = u'CsOJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "CsOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.98,-1.3,-1.61,-1.89,-2.38,-2.8,-3.59],'cal/(mol*K)'),
        H298 = (104.06,'kcal/mol'),
        S298 = (-1.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI(ROJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "H3COJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11,-1.29,-1.62,-1.97,-2.59,-3.07,-3.84],'cal/(mol*K)'),
        H298 = (104.27,'kcal/mol'),
        S298 = (0.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Enthalpy HBI calculated from NIST values, entropy and Cp from B3LYP/6-31G* for CH3OH, CH3O and H""",
    longDesc = 
u"""

""",
)

entry(
    index = 3022,
    label = "CC(C)OJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * O2s u1 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.3,-6.3,-7.3,-8.3,-9.8,-11.2,-14.2],'J/(mol*K)'),
        H298 = (447.6,'kJ/mol'),
        S298 = (-6.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3023,
    label = "CC(C)2OJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-7.9,-9,-9.9,-10.7,-11.7,-14.6],'J/(mol*K)'),
        H298 = (446.1,'kJ/mol'),
        S298 = (-4.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3036,
    label = "C=CC(C)2OJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.9,-12.1,-12.9,-12.9,-12.6,-12.9,-14.8],'J/(mol*K)'),
        H298 = (445.9,'kJ/mol'),
        S298 = (2.7,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3068,
    label = "C=CC(C)(C=O)OJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4 * O2s u1 {1,S}
5   C  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-11.3,-14.6,-16.2,-17.2,-17.4,-18.4],'J/(mol*K)'),
        H298 = (462.1,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3051,
    label = "CC(C)(C=O)OJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.6,-13.9,-16.3,-17.5,-18.4,-18.8,-19.1],'J/(mol*K)'),
        H298 = (459.1,'kJ/mol'),
        S298 = (16.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3024,
    label = "CC(C)(O)OJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.8,-18.8,-22.1,-22.3,-19.5,-17.2,-16],'J/(mol*K)'),
        H298 = (449,'kJ/mol'),
        S298 = (8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3037,
    label = "C=CC(C)(O)OJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C  u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.2,-12.5,-16.7,-19.1,-20.1,-19.4,-18.2],'J/(mol*K)'),
        H298 = (450.7,'kJ/mol'),
        S298 = (8.5,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 98,
    label = "CdsOJ",
    group = 
"""
1 * O2s      u1 {2,S}
2   [Cd,CO] u0 {1,S}
""",
    thermo = u'RC=COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "RC=COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cd u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.99,-2.48,-2.79,-3.13,-3.33,-3.79],'cal/(mol*K)'),
        H298 = (88,'kcal/mol'),
        S298 = (-1.11,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 3034,
    label = "C=COJ",
    group = 
"""
1   Cd u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   C  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.1,-13.5,-14.6,-14.6,-14.3,-14.5,-16],'J/(mol*K)'),
        H298 = (358.1,'kJ/mol'),
        S298 = (3.3,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3035,
    label = "C=C(C)OJ",
    group = 
"""
1   Cd u0 {2,S} {3,D} {4,S}
2 * O2s u1 {1,S}
3   C  u0 {1,D}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.2,-13.1,-15.6,-17,-17.7,-17.6,-17.6],'J/(mol*K)'),
        H298 = (354.8,'kJ/mol'),
        S298 = (7.4,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 100,
    label = "OJC=O",
    group = 
"""
1   CO u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31,-1.87,-2.32,-2.69,-3.28,-3.74,-4.56],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 3049,
    label = "OC=OOJ",
    group = 
"""
1   CO u0 {2,S} {3,S} {4,D}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.5,-13.1,-16.3,-18.3,-20.4,-21.2,-21.4],'J/(mol*K)'),
        H298 = (460.9,'kJ/mol'),
        S298 = (6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3050,
    label = "C=OC=OOJ",
    group = 
"""
1   CO u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {5,D}
3 * O2s u1 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.1,-6.8,-10.1,-13,-17.5,-20.9,-25.9],'J/(mol*K)'),
        H298 = (479.5,'kJ/mol'),
        S298 = (16,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 217,
    label = "CbOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cb u0 {1,S}
""",
    thermo = u'RC=COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3020,
    label = "CCOJ",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.1,-12.2,-14.4,-15.1,-14.7,-14.5,-15.6],'J/(mol*K)'),
        H298 = (442.9,'kJ/mol'),
        S298 = (3.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3048,
    label = "C=OCOJ",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.6,-9.3,-11.5,-13.2,-15,-16,-17.5],'J/(mol*K)'),
        H298 = (461,'kJ/mol'),
        S298 = (2.6,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3021,
    label = "OCOJ",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.9,-17.5,-19.8,-19.3,-16.2,-14.3,-14.3],'J/(mol*K)'),
        H298 = (444.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 3021,
    label = "SCOJ",
    group =
"""
1   C  ux {2,S} {3,S}
2 * O2s u1 {1,S}
3   S   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.09,-4.17,-4.38,-4.16,-3.24,-2.43,-1.96],'cal/(mol*K)'),
        H298 = (104.33,'kcal/mol'),
        S298 = (1.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 101,
    label = "OOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   O2s u0 {1,S}
""",
    thermo = u'ROOJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "ROOJ",
    group = 
"""
1   O2s  u0 {2,S} {3,S}
2 * O2s  u1 {1,S}
3   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C(=O)OOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (98.33,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""HBI for enthalpy from CHEN & BOZZELLI. Cp and S values taken from ROOJ""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C3COOJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S} {6,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6 * O2s u1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (85.3,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "HOOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.68,-3.07,-3.3,-3.55,-3.66,-3.9],'cal/(mol*K)'),
        H298 = (85.13,'kcal/mol'),
        S298 = (-0.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from NIST values for H2O2, O2H and H""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "SOOJ",
    group =
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   S  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39,-2.62,-2.95,-3.22,-3.66,-3.98,-4.52],'cal/(mol*K)'),
        H298 = (91.79,'kcal/mol'),
        S298 = (1.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 110,
    label = "NJ",
    group = 
"""
1 * N u1
""",
    thermo = u'N3sJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "N3sJ",
    group = 
"""
1 * N3s u1 p1
""",
    thermo = u'NHJ_C',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "NH2J",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   H   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.43,-0.82,-1.27,-1.72,-2.48,-3.08,-4.1],'cal/(mol*K)'),
        H298 = (107.183,'kcal/mol'),
        S298 = (0.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to ammonia from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "NHJ_C",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79,-1.23,-1.64,-2.02,-2.66,-3.2,-4.16],'cal/(mol*K)'),
        H298 = (99.653,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to CH3NH2 from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "NHJ_O",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   O   u0 p2 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26,-1.89,-2.4,-2.79,-3.17,-3.37,-3.65],'cal/(mol*K)'),
        H298 = (85.023,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH2OH and [NH]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 115,
    label = "NHJ_N",
    group =
"""
1 * N3s u1 p1 {2,S} {3,S}
2   N   u0 px {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77,-2.62,-3.28,-3.79,-4.57,-5.11,-5.85],'cal/(mol*K)'),
        H298 = (82.283,'kcal/mol'),
        S298 = (-0.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH2NH2 and [NH]NH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 116,
    label = "NJ_CC",
    group =
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.46,3.70,3.86,3.95,3.73,3.16,1.98],'cal/(mol*K)'),
        H298 = (120.063,'kcal/mol'),
        S298 = (10.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t CH3NHCH3 and CH3[N]CH3, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 117,
    label = "N3dJ",
    group = 
"""
1 * N3d u1 p1
""",
    thermo = u'N3dJ_C',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "N3dJ_C",
    group =
"""
1 * N3d u1 p1 {2,D}
2   C   u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.2,-0.6,-1.07,-1.56,-2.44,-3.15,-4.26],'cal/(mol*K)'),
        H298 = (88.343,'kcal/mol'),
        S298 = (-0.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH=CH2 and [N]=CH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 119,
    label = "N3dJ_O",
    group =
"""
1 * N3d u1 p1 {2,D}
2   O   u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12,-1.36,-1.67,-2.0,-2.62,-3.11,-3.89],'cal/(mol*K)'),
        H298 = (48.613,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t HN=O and [N]=O, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 120,
    label = "N3dJ_N",
    group =
"""
1 * N3d u1 p1 {2,D}
2   N   u0 px {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14,-0.51,-0.97,-1.46,-2.33,-3.02,-4.16],'cal/(mol*K)'),
        H298 = (64.083,'kcal/mol'),
        S298 = (1.49,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t HN=NH and [N]=NH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 134,
    label = "SiJ",
    group = 
"""
1 * Si u1
""",
    thermo = u'CJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "SJ",
    group = 
"""
1 * S u1
""",
    thermo = u'S2J',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "S2J-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   H   u0    {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.52,-1.84,-2.17,-2.73,-3.2,-3.95],'cal/(mol*K)'),
        H298 = (91.82,'kcal/mol'),
        S298 = (-4.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "S2J-C",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   C   u0    {1,S}
""",
    thermo = u'S2J-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "S2J-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0    {1,S}
""",
    thermo = u'S2sJ-(CsHHH)',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 236,
    label = "S2sJ-(CsHHH)",
    group =
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0    {1,S} {3,S} {4,S} {5,S}
3   H   u0    {2,S}
4   H   u0    {2,S}
5   H   u0    {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35,-1.58,-1.87,-2.16,-2.66,-3.11,-3.95],'cal/(mol*K)'),
        H298 = (87.08,'kcal/mol'),
        S298 = (-3.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 236,
    label = "S2J-(Cs-Cb)",
    group =
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0    {1,S} {3,S}
3   Cb  u0    {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.29,-3.84,-4.16,-4.58,-5.31,-5.90,-6.84],'cal/(mol*K)'),
        H298 = (86.83,'kcal/mol'),
        S298 = (-4.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 238,
    label = "S2J-Ct",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Ct  u0    {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18,-2.05,-2.66,-3.12,-3.76,-4.24,-4.99],'cal/(mol*K)'),
        H298 = (77.56,'kcal/mol'),
        S298 = (-4.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "S2J-Cb",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cb  u0    {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92,-2.1,-2.3,-2.51,-2.93,-3.32,-3.96],'cal/(mol*K)'),
        H298 = (81.36,'kcal/mol'),
        S298 = (-3.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "S2J-Cd",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cd  u0    {1,S} {3,D}
3   C   u0    {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.29,-2.56,-2.72,-2.87,-3.19,-3.52,-4.13],'cal/(mol*K)'),
        H298 = (79.29,'kcal/mol'),
        S298 = (-1.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "S2J-C=S",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   CS  u0    {1,S} {3,D}
3   S2d u0 p2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.93,-3.56,-3.88,-4.08,-4.41,-4.74,-5.25],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (-0.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "S2J-CO",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   CO  u0    {1,S} {3,D}
3   O2d  u0    {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26,-2.82,-3.17,-3.44,-3.89,-4.29,-4.95],'cal/(mol*K)'),
        H298 = (89.6,'kcal/mol'),
        S298 = (-0.42,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 CAC""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "S2J-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S}
""",
    thermo = u'S2J-S2s-H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "S2J-S2s-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   H   u0    {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93,-2.7,-3.26,-3.67,-4.24,-4.59,-5],'cal/(mol*K)'),
        H298 = (73.97,'kcal/mol'),
        S298 = (-2.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "S2J-S2s-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   C   u0    {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.95,-3.43,-3.78,-4.06,-4.47,-4.74,-5.03],'cal/(mol*K)'),
        H298 = (71.05,'kcal/mol'),
        S298 = (-1.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "S2J-S2s-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   S2s u0 p2 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63,-4.32,-4.84,-5.26,-5.82,-6.07,-5.99],'cal/(mol*K)'),
        H298 = (72.74,'kcal/mol'),
        S298 = (0.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "RJ2_triplet",
    group = 
"""
1 * R!H u2
""",
    thermo = u'CJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "CJ2_triplet",
    group = 
"""
1 * C u2
""",
    thermo = u'CsJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "CsJ2_triplet",
    group = 
"""
1 * Cs u2
""",
    thermo = u'CH2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "CH2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],'cal/(mol*K)'),
        H298 = (214.44,'kcal/mol'),
        S298 = (-1.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for methylene in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "CsJ2_P_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = u'CsCsJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "CsCsJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = u'CCJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "CCJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
5   H  u0 {2,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.81,-1.74,-2.69,-3.61,-5.18,-6.42,-8.36],'cal/(mol*K)'),
        H298 = (211.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE and Cp calculated from data in KIM et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "PhCH_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (195,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from PUTSMA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "AllylJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (192.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from PUTSMA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "CsJ2_S_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = u'CsJ2_P_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "OsCsJ2H_triplet",
    group =
"""
1 * Cs u2 {2,S} {3,S}
2   H  u0 {1,S}
3   O  u0 p2 {1,S} {4,S}
4   H  u0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.444, -1.111, -1.988, -2.889, -4.529, -5.915, -8.422], 'cal/(mol*K)'),
        H298=(205.773, 'kcal/mol'),
        S298=(-2.011, 'cal/(mol*K)'),
    ),
    shortDesc = u"""Fittted to DFT_QCI_thermo library""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 124,
    label = "CdJ2_triplet",
    group = 
"""
1 * [Cd,CO] u2
""",
    thermo = u'CCdJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "CCdJ2_triplet",
    group = 
"""
1 * Cd u2 {2,D}
2   C  u0 {1,D}
""",
    thermo=u'CdCdJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "CdCdJ2_triplet",
    group =
"""
1 * Cd u2 {2,D}
2   Cd u0 {1,D} {3,S} {4,S}
3   H  u0 {2,S}
4   H  u0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.904, -2.152, -3.433, -4.583, -6.214, -7.197, -9.27], 'cal/(mol*K)'),
        H298=(237.632, 'kcal/mol'),
        S298=(1.79, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Fittted to DFT_QCI_thermo library""",
    longDesc=
    u"""
    Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
    """,
)

entry(
    index = 139,
    label = "(CO)CdJ2_triplet",
    group =
"""
1 * Cd u2 {2,D}
2   Cdd u0 {1,D} {3,D}
3   O u0 p2 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.763, -2.732, -3.654, -4.473, -5.712, -6.563, -8.315], 'cal/(mol*K)'),
        H298=(206.595, 'kcal/mol'),
        S298=(-1.634, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Fittted to DFT_QCI_thermo library""",
    longDesc=
    u"""
    Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
    """,
)

entry(
    index = 262,
    label = "CdJ2-Sd_triplet",
    group = 
"""
1 * CS u2 {2,D}
2   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-2.3,-3.22,-4.04,-5.42,-6.5,-8.29],'cal/(mol*K)'),
        H298 = (238.75,'kcal/mol'),
        S298 = (-3.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "NJ2_triplet",
    group = 
"""
1 * N u2 px
""",
    thermo = u'NJ2_C',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    label = "N3sJ2",
    group = 
"""
1 * N3s u2 p1
""",
    thermo = u'NJ2_C',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "NHJ2",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.1,-2.78,-3.47,-4.75,-5.77,-7.61],'cal/(mol*K)'),
        H298 = (200.636,'kcal/mol'),
        S298 = (-2.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH3 and [N], both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 273,
    label = "NJ2_C",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.36,-2.97,-3.51,-4.0,-5.0,-5.96,-7.75],'cal/(mol*K)'),
        H298 = (184.816,'kcal/mol'),
        S298 = (-3.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH2CH3 and [N]CH3, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 274,
    label = "NJ2_O",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   O   u0 p2 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-3.22,-4.34,-5.36,-6.88,-7.91,-9.25],'cal/(mol*K)'),
        H298 = (166.156,'kcal/mol'),
        S298 = (-0.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated w.r.t NH2OH and [N]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc =
u"""

""",
)

entry(
    index = 130,
    label = "Oa_triplet",
    group = 
"""
1 * O u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],'cal/(mol*K)'),
        H298 = (221.55,'kcal/mol'),
        S298 = (-8.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for atomic oxygen in relation to water from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "SiJ2_triplet",
    group = 
"""
1 * Si u2
""",
    thermo = u'CJ2_triplet',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    label = "SJ2_triplet",
    group = 
"""
1 * S u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19,-3.52,-3.89,-4.3,-5.12,-5.86,-7.14],'cal/(mol*K)'),
        H298 = (176.42,'kcal/mol'),
        S298 = (-12.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "RJ3",
    group = 
"""
1 * R!H u3
""",
    thermo = u'CJ3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "CJ3",
    group = 
"""
1 * Cs u3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57,-2.73,-4.11,-5.5,-7.92,-9.85,-12.95],'cal/(mol*K)'),
        H298 = (316.19,'kcal/mol'),
        S298 = (-5.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for methylidyene in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "SiJ3",
    group = 
"""
1 * Sis u3
""",
    thermo = u'CJ3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "OC=CJCb",
    group =
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D} {4,S}
3   Cb  u0 {1,S}
4   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.047, 0.607, 0.374, -0.3, -1.28, -1.972, -3.196],'cal/(mol*K)'),
        H298 = (123.797,'kcal/mol'),
        S298 = (2.661,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations""",
    longDesc =
u"""
Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations for OC=[C]c1ccccc1
""",
)

entry(
    index = 2001,
    label = "S4dJ-OdH",
    group =
"""
1   O2d  u0 p2 c0 {2,D}
2 * S4d u1 p1 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.510000,-1.200000,-1.930000,-2.590000,-3.600000,-4.270000,-5.100000],'cal/(mol*K)'),
        H298 = (58.000000,'kcal/mol'),
        S298 = (0.540000,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2002,
    label = "S2sJ-O",
    group =
"""
1 * S2s  u1 p2 c0 {2,S}
2   O2s   u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.159038,-4.009747,-4.361871,-4.910916,-5.320592,-5.530248,-5.757974],'cal/(mol*K)'),
        H298 = (108.577118,'kcal/mol'),
        S298 = (-7.477222,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2003,
    label = "S4dJ-OdO",
    group =
"""
1   O2d  u0 p2 c0 {2,D}
2 * S4d u1 p1 c0 {1,D} {3,S}
3   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.710000,-2.410000,-3.090000,-3.650000,-4.420000,-4.890000,-5.450000],'cal/(mol*K)'),
        H298 = (58.900000,'kcal/mol'),
        S298 = (0.140000,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2004,
    label = "S6ddJ-OdOdH",
    group =
"""
1   O2d   u0 p2 c0 {2,D}
2 * S6dd u1 p0 c0 {1,D} {3,D} {4,S}
3   O2d   u0 p2 c0 {2,D}
4   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.977000,0.640000,-0.027000,-0.741000,-1.913000,-2.873000,-4.269000],'cal/(mol*K)'),
        H298 = (75.948000,'kcal/mol'),
        S298 = (3.331000,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2005,
    label = "S6ddJ-OdOdO",
    group =
"""
1   O2d   u0 p2 c0 {2,D}
2 * S6dd u1 p0 c0 {1,D} {3,D} {4,S}
3   O2d   u0 p2 c0 {2,D}
4   O2s   u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.539000,-1.537000,-2.332000,-2.933000,-4.010000,-4.785000,-5.701000],'cal/(mol*K)'),
        H298 = (86.194000,'kcal/mol'),
        S298 = (4.146000,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2006,
    label = "O2sJ-S2s",
    group =
"""
1 * O2s    u1 p2 c0 {2,S}
2   S2s    u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.53,-0.81,-0.99,-1.17,-1.56,-1.88,-2.49],'cal/(mol*K)'),
        H298 = (79.78,'kcal/mol'),
        S298 = (1.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 2006,
    label = "O2sJ-S4d",
    group =
"""
1 * O2s    u1 p2 c0 {2,S}
2   S4d    u0 p1 c0 {1,S}
""",
    thermo = u'O2sJ-(S4d-OdO)',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value of 52.103 kcal/mol, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2006,
    label = "O2sJ-(S4d-OdO)",
    group =
"""
1 * O2s    u1 p2 c0 {2,S}
2   S4d    u0 p1 c0 {1,S} {3,D} {4,S}
3   O2d    u0 p2 c0 {2,D}
4   O      u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.07,-0.61,-0.93,-1.55,-2.00,-2.49],'cal/(mol*K)'),
        H298 = (28.13,'kcal/mol'),
        S298 = (2.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 2006,
    label = "O2sJ-S6d",
    group =
"""
1 * O2s    u1 p2 c0 {2,S}
2   S6d    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68,-2.09,-2.45,-2.77,-3.30,-3.71,-4.41],'cal/(mol*K)'),
        H298 = (106.21,'kcal/mol'),
        S298 = (-1.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 2006,
    label = "O2sJ-(S4d-OdC)",
    group =
"""
1 * O2s    u1 p2 c0 {2,S}
2   S4d    u0 p1 c0 {1,S} {3,D} {4,S}
3   O      u0 p2 c0 {2,D}
4   C      u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.33,-2.94,-3.19,-3.38,-3.72,-4.01,-4.59],'cal/(mol*K)'),
        H298 = (78.16,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 2006,
    label = "O2sJ-(S4d-CdC)",
    group =
"""
1 * O2s      u1 p2 c0 {2,S}
2   S4d    u0 p1 c0 {1,S} {3,D} {4,S}
3   C      u0 p0 c0 {2,D}
4   C      u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13,-1.86,-2.28,-2.63,-3.2,-3.64,-4.39],'cal/(mol*K)'),
        H298 = (74.659,'kcal/mol'),
        S298 = (0.698,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 2006,
    label = "O2sJ-(S4d-OdH)",
    group =
"""
1 * O2s      u1 p2 c0 {2,S}
2   S4d    u0 p1 c0 {1,S} {3,D} {4,S}
3   O      u0 p2 c0 {2,D}
4   H      u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.69,-3.3,-3.74,-4.07,-4.4,-4.54,-4.927],'cal/(mol*K)'),
        H298 = (79.582,'kcal/mol'),
        S298 = (-1.49,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 2007,
    label = "SOJ",
    group =
"""
1 * O   u1 p2 c0 {2,S}
2   S   ux px c0 {1,S}
""",
    thermo = u'O2sJ-S2s',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2007,
    label = "S2J",
    group =
"""
1 * S2s   u1 p2
""",
    thermo = u'S2J-C',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2007,
    label = "S4dJ",
    group =
"""
1 * S4d   u1 p1
""",
    thermo = u'S4dJ-OdO',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2007,
    label = "S6ddJ",
    group =
"""
1 * S6dd   u1 p0
""",
    thermo = u'S6ddJ-OdOdO',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2008,
    label = "S4sJ",
    group =
"""
1 * S4s   u1 p1
""",
    thermo = u'S4sJ-CCC',
    shortDesc = u"""Sulfur Oxygen Extension""",
    longDesc =
u""""
""",
)

entry(
    index = 2009,
    label = "S6sJ",
    group =
"""
1 * S6s   u1 p0
""",
    thermo = u'S6sJ-CCCCC',
    shortDesc = u"""Calculated at CBS-QB3""",
    longDesc =
u""""
""",
)

entry(
    index = 2050,
    label = "S6dJ",
    group =
"""
1 * S6d   u1 p0
""",
    thermo = u'S6dJ-OdOCC',
    shortDesc = u"""Calculated at CBS-QB3""",
    longDesc =
u""""
""",
)

entry(
    index = 2051,
    label = "S6dJ-OdOCC",
    group =
"""
1 * S6d    u1 p0 c0 {2,S} {3,S} {4,S} {5,D}
2   O      ux {1,S}
3   C      ux {1,S}
4   C      ux {1,S}
5   O      ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.35,1.6,-0.19,-0.45,-0.95,-1.42,-3.65],'cal/(mol*K)'),
        H298 = (56.531,'kcal/mol'),
        S298 = (3.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Based on radical calculations at CBS-QB3
""",
)

entry(
    index = 2010,
    label = "S4sJ-CCC",
    group =
"""
1 * S4s    u1 p1 c0 {2,S} {3,S} {4,S}
2   C      ux {1,S}
3   C      ux {1,S}
4   C      ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.055,-3.801,-4.696,-5.408,-6.524,-7.325,-8.52],'cal/(mol*K)'),
        H298 = (63.249,'kcal/mol'),
        S298 = (12.849,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Calculated at CBS-QB3
""",
)

entry(
    index = 2011,
    label = "S4sJ-OCC",
    group =
"""
1 * S4s    u1 p1 c0 {2,S} {3,S} {4,S}
2   O      ux {1,S}
3   C      ux {1,S}
4   C      ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.475,-.55,-2.75,-4.66,-7.27,-9.325,-8.64],'cal/(mol*K)'),
        H298 = (21.67,'kcal/mol'),
        S298 = (15.449,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Based on radical calculations at CBS-QB3
""",
)

entry(
    index = 2010,
    label = "S6sJ-CCCCC",
    group =
"""
1 * S6s    u1 p0 c0 {2,S} {3,S} {4,S} {5,S} {6,S}
2   C      ux {1,S}
3   C      ux {1,S}
4   C      ux {1,S}
5   C      ux {1,S}
6   C      ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.815,3.48,2.34,1.364,-0.161,-1.233,-2.644],'cal/(mol*K)'),
        H298 = (60.164,'kcal/mol'),
        S298 = (9.723,'cal/(mol*K)'),
    ),
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2011,
    label = "Benzyl_S_Fused5",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {6,[S,D,T]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {3,[S,D,T]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.054016,-0.574860,-1.161811,-1.586869,-2.403320,-3.150381,-4.416756],'cal/(mol*K)','+|-',[0.201190,0.201190,0.201190,0.201190,0.201190,0.201190,0.201190]),
        H298 = (88.503762,'kcal/mol','+|-',0.737851),
        S298 = (3.112531,'cal/(mol*K)','+|-',0.434935),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CC[CH]C2=C1
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 2012,
    label = "Benzyl_S_Fused6",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {6,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.881557,-1.191625,-1.649808,-2.003459,-2.505735,-3.094923,-4.341263],'cal/(mol*K)','+|-',[0.318445,0.318445,0.318445,0.318445,0.318445,0.318445,0.318445]),
        H298 = (86.379670,'kcal/mol','+|-',1.148432),
        S298 = (1.330626,'cal/(mol*K)','+|-',0.744626),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CCC[CH]C2=C1
CC1CC[CH]C2=CC=CC=C21
CCC1CC[CH]C2=CC=CC=C21
""",
)

entry(
    index = 2013,
    label = "Benzyl_T_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {6,[S,B,T]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {3,[S,B,T]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.457289,-1.562693,-2.227712,-2.429028,-2.809678,-3.487717,-4.252860],'cal/(mol*K)','+|-',[0.282803,0.282803,0.282803,0.282803,0.282803,0.282803,0.282803]),
        H298 = (85.449826,'kcal/mol','+|-',1.022623),
        S298 = (4.370664,'cal/(mol*K)','+|-',0.608769),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 2014,
    label = "Benzyl_T_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {6,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148032,-0.974235,-1.848643,-2.422838,-3.012068,-3.465264,-4.437082],'cal/(mol*K)','+|-',[0.514226,0.514226,0.514226,0.514226,0.514226,0.514226,0.514226]),
        H298 = (84.719974,'kcal/mol','+|-',1.823766),
        S298 = (1.702078,'cal/(mol*K)','+|-',1.175222),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[C]1CCCC2=CC=CC=C21
CC[C]1CCCC2=CC=CC=C21
""",
)

entry(
    index = 2015,
    label = "CJ-Cd-Benzene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S} {7,S}
4   H  u0 {1,S}
5   Cd u0 {2,D} {6,S}
6   Cb u0 {7,B} {5,S}
7   Cb u0 {6,B} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.038694,-0.486795,-1.266142,-1.943551,-2.846431,-3.509532,-4.609948],'cal/(mol*K)','+|-',[0.244001,0.244001,0.244001,0.244001,0.244001,0.244001,0.244001]),
        H298 = (80.055693,'kcal/mol','+|-',0.913362),
        S298 = (1.932508,'cal/(mol*K)','+|-',0.367823),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2C=C[CH]CC2=C1
CC1[CH]C=CC2=CC=CC=C12
CC1=C[CH]CC2=CC=CC=C12
CCC1[CH]C=CC2=CC=CC=C12
CCC1=C[CH]CC2=CC=CC=C12
""",
)

entry(
    index = 2020,
    label = "Benzyl_S_dihydronaphthalene",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   Cd  u0 {5,S} {7,D}
7   Cd  u0 {6,D} {3,[S,D,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.762975,-1.091932,-1.454467,-1.908359,-2.748445,-3.446538,-4.576528],'cal/(mol*K)','+|-',[0.226952,0.226952,0.226952,0.226952,0.226952,0.226952,0.226952]),
        H298 = (31.565243,'kcal/mol','+|-',0.869131),
        S298 = (1.433096,'cal/(mol*K)','+|-',0.350884),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2C=CC[CH]C2=C1
C[C]1CC=CC2=CC=CC=C12
CC[C]1CC=CC2=CC=CC=C12
""",
)

entry(
    index = 2021,
    label = "Benzyl_T_dihydronaphthalene",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   Cd  u0 {5,S} {7,D}
7   Cd  u0 {6,D} {3,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.264274,-0.237466,-0.864612,-1.638997,-2.840867,-3.590474,-4.678897],'cal/(mol*K)','+|-',[0.546927,0.546927,0.546927,0.546927,0.546927,0.546927,0.546927]),
        H298 = (83.336835,'kcal/mol','+|-',2.015630),
        S298 = (2.120448,'cal/(mol*K)','+|-',0.802466),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC[CH]C2=CC=CC=C12
CCC1=CC[CH]C2=CC=CC=C12
""",
)


entry(
    index = 2022,
    label = "Aromatic_pi_S_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S}
7   H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.013276,-1.289314,-2.312579,-2.921595,-3.398456,-3.676202,-4.864196],'cal/(mol*K)','+|-',[0.023461,0.023461,0.023461,0.023461,0.023461,0.023461,0.023461]),
        H298 = (75.469224,'kcal/mol','+|-',0.139824),
        S298 = (1.484606,'cal/(mol*K)','+|-',0.036353),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1
CC1[CH]CC=CC=1
CC1C=CC[CH]C=1
CC1[CH]C=CC=C1
""",
)

entry(
    index = 2023,
    label = "Aromatic_pi_S_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
""",
    thermo = u'Aromatic_pi_S_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 2024,
    label = "Aromatic_pi_T_1_3",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cs u0 {1,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {2,D}
""",
    thermo = u'Aromatic_pi_S_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 2025,
    label = "Aromatic_pi_T_1_4",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {6,S} {2,D}
""",
    thermo = u'Aromatic_pi_S_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 2026,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {5,S}
9   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.104911,-1.140650,-2.324049,-3.038951,-3.752012,-4.054814,-5.141931],'cal/(mol*K)','+|-',[0.061305,0.061305,0.061305,0.061305,0.061305,0.061305,0.061305]),
        H298 = (75.544685,'kcal/mol','+|-',0.399656),
        S298 = (2.790834,'cal/(mol*K)','+|-',0.079011),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1C
CC1[CH]C(C)C=CC=1
CC1C=CC(C)[CH]C=1
CC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 2027,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {3,S}
9   C u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2028,
    label = "Aromatic_pi_T_(CH3_CH3_Ortho)_1_3",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cs u0 {1,S} {5,S} {8,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {2,D}
8   C u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2029,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {2,S}
9   C u0 {6,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2030,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {2,S}
9   C u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2031,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {4,S}
9   C u0 {6,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2032,
    label = "Aromatic_pi_S_(CH3_CH3_Para)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {3,S}
9   C u0 {6,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2033,
    label = "Aromatic_pi_T_(CH3_CH3_Para)_1_4",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cd u0 {1,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {6,S} {2,D}
8   C u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2034,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S} {9,S}
7   H u0 {1,S}
8   C u0 {6,S}
9   C u0 {6,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2035,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {4,S}
9   C u0 {4,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 2036,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {5,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.453462,-1.202443,-2.436067,-2.956152,-3.471072,-3.948804,-5.034070],'cal/(mol*K)','+|-',[0.068504,0.068504,0.068504,0.068504,0.068504,0.068504,0.068504]),
        H298 = (74.981951,'kcal/mol','+|-',0.417781),
        S298 = (1.243621,'cal/(mol*K)','+|-',0.106961),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1[CH]C=CC=C1C
CCC1[CH]C(C)=CC=C1
CCC1[CH]C=C(C)C=C1
CCC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 2037,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {3,S}
9   C u0 {4,S} {10,S}
10  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2038,
    label = "Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cs u0 {1,S} {5,S} {8,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {2,D}
8   C u0 {4,S} {9,S}
9   C u0 {8,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2039,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {2,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2040,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {2,S}
9   C u0 {4,S} {10,S}
10  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2041,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {4,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2042,
    label = "Aromatic_pi_S_(CH3_C2H5_Para)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {3,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2043,
    label = "Aromatic_pi_T_(CH3_C2H5_Para)_1_4",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cd u0 {1,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {6,S} {2,D}
8   C u0 {4,S} {9,S}
9   C u0 {8,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2044,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S} {9,S}
7   H u0 {1,S}
8   C u0 {6,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2045,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {4,S}
9   C u0 {4,S} {10,S}
10  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 2046,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {5,S}
9   C u0 {6,S} {10,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.831072,-0.828879,-1.898878,-2.143234,-2.473595,-2.805725,-3.594795],'cal/(mol*K)','+|-',[0.208059,0.208059,0.208059,0.208059,0.208059,0.208059,0.208059]),
        H298 = (74.133127,'kcal/mol','+|-',0.742606),
        S298 = (-0.854817,'cal/(mol*K)','+|-',0.322012),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:

""",
)

entry(
    index = 2047,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {3,S}
9   C u0 {4,S} {10,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2048,
    label = "Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cs u0 {1,S} {5,S} {8,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {2,D}
8   C u0 {4,S} {9,S}
9   Cb u0 {8,S} {10,B} {14,B}
10  Cb u0 {9,B} {11,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {9,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2049,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {2,S}
9   C u0 {6,S} {10,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2050,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {2,S}
9   C u0 {4,S} {10,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2051,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {4,S}
9   C u0 {6,S} {10,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2052,
    label = "Aromatic_pi_S_(CH3_Benzyl_Para)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {3,S}
9   C u0 {6,S} {10,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2053,
    label = "Aromatic_pi_T_(CH3_Benzyl_Para)_1_4",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cd u0 {1,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {6,S} {2,D}
8   C u0 {4,S} {9,S}
9   Cb u0 {8,S} {10,B} {14,B}
10  Cb u0 {9,B} {11,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {9,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2054,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S} {9,S}
7   H u0 {1,S}
8   C u0 {6,S}
9   C u0 {6,S} {10,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2055,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {4,S}
9   C u0 {4,S} {10,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
""",
    thermo = u'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2056,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {5,S}
9   Cs u0 {6,S} {10,S} {16,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
16  C u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.677181,-0.360591,-1.618359,-2.065862,-2.453129,-2.747906,-3.506577],'cal/(mol*K)','+|-',[0.245046,0.245046,0.245046,0.245046,0.245046,0.245046,0.245046]),
        H298 = (74.329439,'kcal/mol','+|-',0.850906),
        S298 = (-3.587842,'cal/(mol*K)','+|-',0.338262),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:

""",
)

entry(
    index = 2057,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {3,S}
9   Cs u0 {4,S} {10,S} {16,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
16  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2058,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cs u0 {1,S} {5,S} {8,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {2,D}
8   Cs u0 {4,S} {9,S} {15,S}
9   Cb u0 {8,S} {10,B} {14,B}
10  Cb u0 {9,B} {11,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {9,B}
15  C u0 {8,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2059,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {2,S}
9   Cs u0 {6,S} {10,S} {16,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
16  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2060,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {2,S}
9   Cs u0 {4,S} {10,S} {16,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
16  C  u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2061,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {4,S}
9   Cs u0 {6,S} {10,S} {16,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
16  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2062,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {3,S}
9   Cs u0 {6,S} {10,S} {16,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
16  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2063,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C u0 {1,S}
4   Cd u0 {1,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {6,S} {2,D}
8   Cs u0 {4,S} {9,S} {15,S}
9   Cb u0 {8,S} {10,B} {14,B}
10  Cb u0 {9,B} {11,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {9,B}
15  C u0 {8,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2064,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S} {9,S}
7   H u0 {1,S}
8   C u0 {6,S}
9   Cs u0 {6,S} {10,S} {16,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
16  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2065,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {4,S}
9   Cs u0 {4,S} {10,S} {16,S}
10  Cb u0 {9,S} {11,B} {15,B}
11  Cb u0 {10,B} {12,B}
12  Cb u0 {11,B} {13,B}
13  Cb u0 {12,B} {14,B}
14  Cb u0 {13,B} {15,B}
15  Cb u0 {10,B} {14,B}
16  C u0 {9,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
""",
)

entry(
    index = 2066,
    label = "Aromatic_pi_S_(fused5)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {3,S} {10,S}
9   C u0 {4,S} {10,S}
10  C u0 {9,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.748775,0.045256,-0.710099,-1.361654,-2.512352,-3.305985,-4.570903],'cal/(mol*K)','+|-',[0.098378,0.098378,0.098378,0.098378,0.098378,0.098378,0.098378]),
        H298 = (74.482889,'kcal/mol','+|-',1.116279),
        S298 = (0.780097,'cal/(mol*K)','+|-',0.163349),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
""",
)

entry(
    index = 2067,
    label = "Aromatic_pi_S_(fused6)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {3,S} {11,S}
9   C u0 {4,S} {10,S}
10  C u0 {9,S} {11,S}
11  C u0 {10,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.012840,-0.508381,-1.059941,-1.550087,-2.565312,-3.360037,-4.585983],'cal/(mol*K)','+|-',[0.129371,0.129371,0.129371,0.129371,0.129371,0.129371,0.129371]),
        H298 = (73.734730,'kcal/mol','+|-',1.665621),
        S298 = (0.399676,'cal/(mol*K)','+|-',0.285184),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 2068,
    label = "Aromatic_pi_S_(fused5)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {5,S} {10,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S} {8,S}
""",
    thermo = u'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 2069,
    label = "Aromatic_pi_S_(fused6)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {5,S} {11,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S} {11,S}
11  C u0 {10,S} {8,S}
""",
    thermo = u'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 2070,
    label = "Aromatic_pi_T_(fused5)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S}
7   C u0 {1,S} {9,S}
8   C u0 {6,S} {9,S}
9   C u0 {8,S} {7,S}
""",
    thermo = u'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 2071,
    label = "Aromatic_pi_T_(fused6)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S}
7   C u0 {1,S} {10,S}
8   C u0 {6,S} {9,S}
9   C u0 {8,S} {10,S}
10  C u0 {9,S} {7,S}
""",
    thermo = u'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 2072,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S} {9,S}
7   H u0 {1,S}
8   C u0 {6,S} {9,S}
9   C u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.481918,0.127981,-0.882314,-1.471559,-2.216403,-3.231953,-4.401823],'cal/(mol*K)','+|-',[0.704900,0.704900,0.704900,0.704900,0.704900,0.704900,0.704900]),
        H298 = (70.660017,'kcal/mol','+|-',4.282018),
        S298 = (-1.779364,'cal/(mol*K)','+|-',1.914852),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCCC1CC12C=C[CH]C=C2
""",
)

entry(
    index = 2073,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {4,S} {9,S}
9   C u0 {4,S} {8,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
""",
)

entry(
    index = 2074,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S} {9,S}
7   H u0 {1,S}
8   C u0 {6,S} {10,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.850106,2.023060,1.417340,0.955199,-0.252841,-1.611607,-3.214279],'cal/(mol*K)','+|-',[0.733897,0.733897,0.733897,0.733897,0.733897,0.733897,0.733897]),
        H298 = (72.495609,'kcal/mol','+|-',4.455656),
        S298 = (2.720001,'cal/(mol*K)','+|-',2.010984),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCC1CCC12C=C[CH]C=C2
""",
)

entry(
    index = 2075,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {4,S} {10,S}
9   C u0 {4,S} {10,S}
10  C u0 {9,S} {8,S}
""",
    thermo = u'Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
""",
)

entry(
    index = 2076,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S} {9,S}
7   H u0 {1,S}
8   C u0 {6,S} {11,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S} {11,S}
11  C u0 {10,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.344733,-0.124290,-0.432103,-0.924571,-2.301224,-3.166951,-4.315021],'cal/(mol*K)','+|-',[0.781339,0.781339,0.781339,0.781339,0.781339,0.781339,0.781339]),
        H298 = (73.495960,'kcal/mol','+|-',4.739542),
        S298 = (-3.286795,'cal/(mol*K)','+|-',2.175866),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1CCCC12C=C[CH]C=C2
""",
)

entry(
    index = 2077,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {4,S} {11,S}
9   C u0 {4,S} {10,S}
10  C u0 {9,S} {11,S}
11  C u0 {10,S} {8,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
""",
)

entry(
    index = 2078,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {1,S} {8,S} {9,S}
7   H u0 {1,S}
8   C u0 {6,S} {12,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S} {11,S}
11  C u0 {10,S} {12,S}
12  C u0 {11,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.226242,-0.404788,-1.081768,-1.652370,-2.569590,-3.273215,-4.647702],'cal/(mol*K)','+|-',[0.872202,0.872202,0.872202,0.872202,0.872202,0.872202,0.872202]),
        H298 = (74.009743,'kcal/mol','+|-',5.285774),
        S298 = (-1.205848,'cal/(mol*K)','+|-',2.522100),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1CCCCC12C=C[CH]C=C2
""",
)

entry(
    index = 2079,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {1,S}
7   H u0 {1,S}
8   C u0 {4,S} {12,S}
9   C u0 {4,S} {10,S}
10  C u0 {9,S} {11,S}
11  C u0 {10,S} {12,S}
12  C u0 {11,S} {8,S}
""",
    thermo = u'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
See Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
""",
)

entry(
    index = 2080,
    label = "Benzyl_S_Fused7",
    group =
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {8,[S,D,T,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   C  u0 {7,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.420000,-1.640000,-1.860000,-2.180000,-2.740000,-3.340000,-4.500000],'cal/(mol*K)','+|-',[1.479200,1.479200,1.479200,1.479200,1.479200,1.479200,1.479200]),
        H298 = (92.100000,'kcal/mol','+|-',5.457800),
        S298 = (4.720000,'cal/(mol*K)','+|-',4.205000),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCC[CH]C2=C1
""",
)

entry(
    index = 2082,
    label = "Aromatic_pi_S_(fused7)_1_3",
    group =
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {5,S} {1,S} {9,S}
7   H u0 {1,S}
8   C u0 {5,S} {12,S}
9   C u0 {6,S} {10,S}
10  C u0 {9,S} {11,S}
11  C u0 {10,S} {12,S}
12  C u0 {11,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.084287,-0.439484,-1.009838,-1.616804,-2.484153,-3.292077,-4.579234],'cal/(mol*K)','+|-',[1.080010,1.080010,1.080010,1.080010,1.080010,1.080010,1.080010]),
        H298 = (76.425234,'kcal/mol','+|-',4.190161),
        S298 = (0.527688,'cal/(mol*K)','+|-',2.029750),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCCCC2[CH]1
C1=CC=C2CCCCC(C)C2[CH]1
""",
)

entry(
    index = 2082,
    label = "CJ-Cd-Benzene7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S} {8,S}
4   H  u0 {1,S}
5   Cd u0 {2,D} {6,S}
6   Cb u0 {7,B} {5,S}
7   Cb u0 {6,B} {8,S}
8   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.300000,-0.500000,-1.000000,-1.500000,-2.500000,-3.300000,-4.500000],'cal/(mol*K)','+|-',[2.464200,2.464200,2.464200,2.464200,2.464200,2.464200,2.464200]),
        H298 = (80.700000,'kcal/mol','+|-',7.325600),
        S298 = (1.000000,'cal/(mol*K)','+|-',3.864200),
    ),
    shortDesc = u"""Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc =
u""""
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CC[CH]C=CC2=C1
""",
)

tree(
"""
L1: Radical
    L2: RJ
        L3: CJ
            L4: CsJ
                L5: CH3
                L5: Cs_P
                    L6: CJCO
                        L7: C=C(O)CJ
                        L7: CJCOOH
                        L7: CJC(C)OC
                        L7: CJC(C)2O
                                L8: C=CC(C)(O)CJ
                                    L9: C=CC(O)(C=O)CJ
                                L8: CJC(C)(C=O)O
                        L7: CJC(O)2C
                            L8: C=CC(O)2CJ
                    L6: CJCC=O
                        L7: CJC(C)2C=O
                            L8: CJC(C=O)2C
                                L9: C=CC(C=O)2CJ
                            L8: C=CC(C)(C=O)CJ
                        L7: CJC(C)C=O
                        L7: C=C(C=O)CJ
                    L6: CJCC=C=O
                        L7: CJC(C)C=C=O
                        L7: C=C(CJ)C=C=O
                    L6: CsCsJ
                        L7: CCJ
                        L7: RCCJ
                        L7: Neopentyl
                        L7: Isobutyl
                    L6: Benzyl_P
                    L6: Allyl_P
                        L7: C=CC=CCJ
                        L7: CTCC=CCJ
                        L7: CJC=C=O
                    L6: Propargyl
                    L6: CJC=O
                        L7: C2JC=O
                L5: Cs_S
                    L6: CCJCO
                        L7: C=CCJCO
                            L8: C=CCJC(O)C=C
                        L7: CCJCOOH
                    L6: CCJCC=O
                    L6: CCJC(C)=C=O
                    L6: (Cs)2CsJ
                        L7: cyclopentene-4
                            L8: bicyclo[2.1.1]hex-2-ene-C5
                                L9: tricyclo[2.1.1.0(1,4)]hex-2-ene-C5
                            L8: bicyclo[2.1.0]pent-2-ene-C5
                        L7: bicyclo[1.1.1]pentane-C2
                            L8: tricyclo[1.1.1.0(1,3)]pentane-C2
                        L7: bicyclo[2.1.1]hexane-C5
                            L8: tricyclo[2.1.1.0(1,4)]hexane-C5
                        L7: cyclopropane
                            L8: spiro[2.2]pentane-secondary
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C7
                            L8: bicyclo[2.1.0]pentane-secondary-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C6
                            L8: bicyclo[1.1.0]butane-secondary
                            L8: bicyclo[3.1.0]hexane-C3
                            L8: bicyclo[4.1.0]heptane-C3-7
                            L8: bicyclo[4.1.0]heptane-C3-7
                        L7: tricyclo[2.1.1.0(1,4)]hexane-C2
                        L7: bicyclo[3.1.1]heptane-C6
                        L7: tricyclo[2.2.1.0(1,4)]heptane-C2
                        L7: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[2.2.2]octane-C2
                            L8: tricyclo[2.2.2.0(1,4)]octane-C2
                        L7: cyclobutane
                            L8: bicyclo[2.1.0]pentane-secondary-C4
                            L8: bicyclo[2.2.0]hexane-secondary
                            L8: bicyclo[3.2.0]heptane-C5-6
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C2
                            L8: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[3.1.1]heptane-C2
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C2
                        L7: bicyclo[3.1.0]hexane-C5-2
                        L7: bicyclo[3.1.0]hexane-C5-3
                        L7: bicyclo[2.1.1]hexane-C2
                        L7: 7-norbornyl
                        L7: 2-norbornyl
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: cycloheptane
                            L8: bicyclo[3.2.0]heptane-C5-2
                            L8: bicyclo[3.2.0]heptane-C5-3
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[3.1.1]heptane-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C3
                        L7: octahydro-pentalene-C5-2
                        L7: octahydro-pentalene-C5-3
                        L7: bicyclo[4.2.0]octane-C6-2
                        L7: bicyclo[4.2.0]octane-C6-3
                        L7: CCJC
                        L7: RCCJC
                        L7: RCCJCC
                            L8: cyclopentane
                            L8: cyclohexane
                    L6: Benzyl_S
                        L7: Indenyl
                        L7: Benzyl_S_Fused5
                        L7: Benzyl_S_Fused6
                            L8: Benzyl_S_dihydronaphthalene
                        L7: Benzyl_S_Fused7
                    L6: Allyl_S
                        L7: Aromatic_pi_S_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_S_(fused5)_1_3
                                    L10: Aromatic_pi_S_(fused6)_1_3
                                    L10: Aromatic_pi_S_(fused7)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2
                            L8: Aromatic_pi_S_(CH3_CH3_Para)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Para)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Para)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_3
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_3
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3
                        L7: CJ-Cd-Benzene
                        L7: CJ-Cd-Benzene7
                        L7: cyclobutene-allyl
                        L7: cyclopentene-allyl
                        L7: cyclohexene-allyl
                    L6: C=CCJC=C
                        L7: Aromatic_pi_S_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4
                                    L10: Aromatic_pi_S_(fused5)_1_4
                                    L10: Aromatic_pi_S_(fused6)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_4
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_4
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4
                        L7: cyclopropenyl-allyl
                        L7: 1,3-cyclopentadiene-allyl
                        L7: C=CCJC=C=O
                    L6: Sec_Propargyl
                    L6: CCJC=O
                        L7: CCJCHO
                        L7: C=OCJC=O
                L5: Cs_T
                    L6: CCJ(C)CO
                        L7: C2CJCOOH
                    L6: Tertalkyl
                        L7: bicyclo[1.1.0]butane-tertiary
                        L7: bicyclo[2.1.0]pentane-tertiary
                        L7: bicyclo[1.1.1]pentane-C1
                        L7: bicyclo[3.1.0]hexane-tertiary
                        L7: bicyclo[2.2.0]hexane-tertiary
                        L7: bicyclo[2.1.1]hexane-C1
                        L7: bridgehead_norbornyl
                        L7: bicyclo[3.2.0]heptane-tertiary
                        L7: bicyclo[4.1.0]heptane-tertiary
                        L7: bicyclo[3.1.1]heptane-C1
                        L7: octahydro-pentalene-tertiary
                        L7: bicyclo[4.2.0]octane-tertiary
                        L7: bicyclo[2.2.2]octane-C1
                    L6: Benzyl_T
                        L7: Benzyl_T_Fused5
                        L7: Benzyl_T_Fused6
                            L8: Benzyl_T_dihydronaphthalene
                    L6: CCJ(C)C=C=O
                        L7: C=CCJ(C)C=C=O
                            L8: C=CCJ(C=C=O)C=C
                    L6: Allyl_T
                        L7: Aromatic_pi_T_1_3
                            L8: Aromatic_pi_T_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_T_(fused5)_1_3
                                    L10: Aromatic_pi_T_(fused6)_1_3
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3
                        L7: Aromatic_pi_T_1_4
                            L8: Aromatic_pi_T_(CH3_CH3_Para)_1_4
                                L9: Aromatic_pi_T_(CH3_C2H5_Para)_1_4
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Para)_1_4
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4
                        L7: bicyclo[2.1.0]pent-2-ene-C1
                        L7: bicyclo[2.1.1]hex-2-ene-C1
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C1
                        L7: C=CCJ(C)C=O
                            L8: C=CCJ(C=O)C=C
                    L6: Tert_Propargyl
                    L6: C2CJCO
                        L7: C2CJCHO
                L5: CsJO
                    L6: CsJOH
                    L6: CsJOC
                        L7: CsJOCs
                            L8: CsJOCH3
                            L8: CsJOCC
                            L8: CsJOCC2
                            L8: CsJOCC3
                        L7: CsJOCds
                            L8: CsJOC(O)
                                L9: CsJOC(O)H
                                L9: CsJOC(O)C
                            L8: C=COCJ
                    L6: CsJOO
                        L7: CsJOOH
                        L7: CsJOOC
                L5: CCsJO
                    L6: CCsJOC
                        L7: C=CCJ(O)C
                        L7: CCsJOCs
                        L7: CCsJOCds
                            L8: CCsJOC(O)
                                L9: CCsJOC(O)H
                                L9: CCsJOC(O)C
                    L6: C=CCJO
                    L6: OCJC=O
                    L6: CCsJOH
                    L6: CCsJOO
                        L7: CCsJOOH
                        L7: CCsJOOC
                L5: C2CsJO
                    L6: C2CsJOH
                    L6: C2CsJOC
                        L7: C2CsJOCs
                        L7: C2CsJOCds
                            L8: C2CsJOC(O)
                                L9: C2CsJOC(O)H
                                L9: C2CsJOC(O)C
                    L6: C2CsJOO
                        L7: C2CsJOOH
                        L7: C2CsJOOC
                L5: CsJ-S
                    L6: CsJ-SsHH
                    L6: CsJ-CSH
                        L7: CsJ-CsSsH
                        L7: CsJ-CtSsH
                        L7: CsJ-CbSsH
                        L7: CsJ-CdSsH
                        L7: CsJ-C=SSsH
                    L6: CsJ-CCS
                        L7: CsJ-CsCsSs
                        L7: CsJ-CsCtSs
                        L7: CsJ-CsCbSs
                        L7: CsJ-CsCdSs
                        L7: CsJ-CsC=SSs
                    L6: CsJ-SS
                        L7: CsJ-SsSsH
                        L7: CsJ-CSS
                            L8: CsJ-CsSsSs
                            L8: CsJ-CtSsSs
                            L8: CsJ-CbSsSs
                            L8: CsJ-CdSsSs
                            L8: CsJ-C=SSsSs
                        L7: CsJ-SsSsSs
                    L6: CCsJOS
                        L7: CCsJOHSH
                    L6: CsJ-SsOsH
                L5: CsJN
                L5: CCsJN
                L5: C2CsJN
                L5: OCJO
            L4: CdsJ
                L5: CdsJO
                    L6: HCdsJO
                    L6: CCJ=O
                        L7: CC(C)CJ=O
                            L8: CC(C)2CJ=O
                                L9: CC(C)(C=O)CJ=O
                                    L10: C=CC(C)(C=O)CJ=O
                                L9: C=CC(C)2CJ=O
                            L8: CC(C)(O)CJ=O
                                L9: C=CC(C)(O)CJ=O
                        L7: CCCJ=O
                            L8: C=OCCJ=O
                                L9: C=OC=OCJ=O
                            L8: C=C(C)CJ=O
                        L7: CsCJ=O
                        L7: C=CCJ=O
                        L7: OC=OCJ=O
                    L6: (O)CJO
                        L7: (O)CJOH
                        L7: (O)CJOC
                            L8: (O)CJOCH3
                            L8: (O)CJOCC
                            L8: (O)CJOCC2
                            L8: (O)CJOCC3
                    L6: SCJ=O
                L5: Cds_P
                    L6: C=C=CJ
                L5: Cds_S
                    L6: C=CJC=O
                    L6: C=CJC=C
                        L7: cyclobutadiene-C1
                            L8: bicyclo[2.2.0]hexa-1(4),2,5-triene-C2
                        L7: 1,3-cyclopentadiene-vinyl-2
                    L6: cyclopropenyl-vinyl
                    L6: cyclobutene-vinyl
                        L7: bicyclo[2.1.0]pent-2-ene-C2
                            L8: tricyclo[2.1.1.0(1,4)]hex-2-ene-C2
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C2
                    L6: cyclopentene-vinyl
                        L7: bicyclo[2.1.1]hex-2-ene-C2
                    L6: 1,3-cyclopentadiene-vinyl-1
                    L6: CCCJ=C=O
                        L7: CC(C)CJ=C=O
                        L7: C=C(C)CJ=C=O
                    L6: OC=CJCb
                L5: S2s-CJ=C
                L5: C=CJO
            L4: CtJ
                L5: Acetyl
            L4: CbJ
            L4: C=SJ
                L5: C=SJ-S2s
                L5: C=SJ-H
                L5: C=SJ-C
                    L6: C=SJ-Cd
                    L6: C=SJ-Cs
        L3: OJ
            L4: HOJ
            L4: COJ
                L5: CCOJ
                    L6: C=OCOJ
                        L7: C=CC(C)(C=O)OJ
                        L7: CC(C)(C=O)OJ
                        L7: C=OC=OOJ
                    L6: CC(C)OJ
                        L7: CC(C)2OJ
                            L8: C=CC(C)2OJ
                        L7: CC(C)(O)OJ
                            L8: C=CC(C)(O)OJ
                    L6: C=C(C)OJ
                L5: CdsOJ
                    L6: RC=COJ
                        L7: C=COJ
                    L6: OJC=O
                        L7: OC=OOJ
                L5: OCOJ
                L5: SCOJ
                L5: CsOJ
                    L6: H3COJ
                L5: CbOJ
            L4: OOJ
                L5: ROOJ
                    L6: C(=O)OOJ
                    L6: C3COOJ
                    L6: SOOJ
                L5: HOOJ
            L4: SOJ
                L5:O2sJ-S2s
                L5:O2sJ-S4d
                    L6:O2sJ-(S4d-OdO)
                    L6:O2sJ-(S4d-OdC)
                    L6:O2sJ-(S4d-OdH)
                    L6:O2sJ-(S4d-CdC)
                L5:O2sJ-S6d
        L3: NJ
            L4: N3sJ
                L5: NH2J
                L5: NHJ_C
                L5: NHJ_O
                L5: NHJ_N
                L5: NJ_CC
            L4: N3dJ
                L5: N3dJ_C
                L5: N3dJ_O
                L5: N3dJ_N
        L3: SiJ
        L3: SJ
            L4:S2J
                L5: S2J-H
                L5: S2J-C
                    L6: S2J-Cs
                        L7: S2sJ-(CsHHH)
                        L7: S2J-(Cs-Cb)
                    L6: S2J-Ct
                    L6: S2J-Cb
                    L6: S2J-Cd
                    L6: S2J-C=S
                    L6: S2J-CO
                L5: S2J-S2s
                    L6: S2J-S2s-H
                    L6: S2J-S2s-Cs
                    L6: S2J-S2s-S2s
                L5: S2sJ-O
            L4:S4sJ
                L5: S4sJ-CCC
		L5: S4sJ-OCC
            L4:S4dJ
                L5: S4dJ-OdH
                L5: S4dJ-OdO
            L4:S6sJ
                L5: S6sJ-CCCCC
	    L4:S6dJ
                L5: S6dJ-OdOCC
            L4:S6ddJ
                L5: S6ddJ-OdOdH
                L5: S6ddJ-OdOdO
    L2: RJ2_triplet
        L3: CJ2_triplet
            L4: OsCsJ2H_triplet
            L4: CsJ2_triplet
                L5: CH2_triplet
                L5: CsJ2_P_triplet
                    L6: CsCsJ2_triplet
                        L7: CCJ2_triplet
                    L6: PhCH_triplet
                    L6: AllylJ2_triplet
                L5: CsJ2_S_triplet
            L4: CdJ2_triplet
                L5: CCdJ2_triplet
                    L6: CdCdJ2_triplet
                    L6: (CO)CdJ2_triplet
            L4: CdJ2-Sd_triplet
        L3: NJ2_triplet
            L4: N3sJ2
                L5: NHJ2
                L5: NJ2_C
                L5: NJ2_O
        L3: Oa_triplet
        L3: SiJ2_triplet
        L3: SJ2_triplet
    L2: RJ3
        L3: CJ3
        L3: SiJ3
"""
)


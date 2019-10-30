#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/rules"
shortDesc = u""
longDesc = u"""
First added by
Author: Belinda Slakman <slakman.b@husky.neu.edu>
Date:   Mon Sep 29 17:32:12 2014 -0700

    Added a silylene insertion reaction family.
    
    Created a recipe and some groups for silylene insertion,
    the insertion of a silylene (like a methylene, but ground
	state is a singlet), into either H2 or a silane.
"""
entry(
    index = 1,
    label = "Si2S;Si_H",
    kinetics = ArrheniusEP(
        A = (1.86E14, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (-1.9, 'kJ/mol'),
        Tmin = (295, 'K'),
        Tmax = (595, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Any silylene insertion into an Si-H bond""",
    longDesc =
u"""
Rate is from the reaction SiH2 + Si2H6 <-> Si3H8, from laser flash photolysis studies of Becerra et al., J. Organometal. Chem., 333-349, 1996.
""",
)

entry(
    index = 2,
    label = "Si2S;H_H",
    kinetics = ArrheniusEP(
        A = (1.05E6, 'cm^3/(mol*s)'),
        n = 1.97,
        alpha = 0,
        E0 = (-1.9, 'kJ/mol'),
        Tmin = (400, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Any silylene insertion into an H-H bond""",
    longDesc =
u"""
Rate is from the reaction SiH2 + H2 <-> SiH4, from high level calculations (see training reactions), from Walch and Dateo, J. Phys. Chem. A, 2001, 2015-2022.
""",
)

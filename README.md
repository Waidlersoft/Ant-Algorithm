# Ant-Algorithm
Self learning ant algorithm.

===Currently in development===

Written in Python 3.7
Needs matplotlib

Theoretic model:
==============

Ants are running randomly from a starting point to a food place and return to the nest. 
While they where running, they drop pheromons. The wind then takes the pheromons way. 
It drops much at the beginning, and while the run, the strength of pheromons decly.
After a while the ants follow only the strongest path of pheromons, which is theoretical the fastest.

Structure
========

Ants:
- Creation
- Moving
- Smelling
- Pheromons

Field:
- Start
- Target
- Borders/Obstacles
- Collecting pheromons
- Wind

Visualization:
- Drawing of field
- Dynamic displaying of ants

Common Functions:
- Some basic functions

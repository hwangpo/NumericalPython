"""
% Graphic method of characteristics for the 3 reservouir problem
%
%
|_____| H1
       \  |_______| H2
        \/
        /HD
       /
|______|H3

"""

import numpy as np
import pylab as p
# Given
no = np.array([1,2,3]) # pipe no.
L = np.array([3,1,5]) # L [km]
D = np.array([20,20,25]) # [cm]
C = np.array([120,110,125]) # Hazen Williams
H = np.array([100,80,20]) # heads, m 
n = 1.852

# Resistance according to Hazen Williams
R = L*1.526e7/((C**n)*(D**4.87)) # resistances


# Let's take HD from 10 to 80 m, every 1 m

HD = np.arange(10,80,0.1)

# for each pipeline:

# H(1) - HD = R(1)*Q(1)^n;
# H(2) - HD = R(2)*Q(2)^n;
# HD - H(3) = R(3)*Q(3)^n;

# estimate Q(i):

Q1 = ((H[0] - HD)/R[0])**(1/n);
Q2 = ((H[1] - HD)/R[1])**(1/n);
Q3 = ((-H[2] + HD)/R[2])**(1/n);

p.figure() 
p.hold(True) # plot all 3 on the same curve
p.plot(Q1,HD,'r-',Q2,HD,'g--',Q3,HD,'b-.')

# plot also the Q(1) + Q(2)
p.plot(Q1+Q2,HD,'k:')

ints = np.diff(np.sign(Q1+Q2-Q3)) < 0
p.plot(Q1[ints]+Q2[ints],HD[ints],'o')
p.plot([Q1[ints]+Q2[ints],Q1[ints]+Q2[ints]],[0,HD[ints]],':')
p.plot([0,Q1[ints]+Q2[ints]],[HD[ints],HD[ints]],':')


p.legend(('Pipe 1','Pipe 2','Pipe 3','Pipe 1+2'))
p.show()
p.savefig('.')

# The point of the intersection is the solution, 
# see the attached figure.

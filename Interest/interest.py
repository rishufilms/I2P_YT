# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:07:58 2020
@author: RishuFilms
"""

import numpy as np

percent=1/100

year=1
month=year/12

principal=1000
roi=10*percent
t=5*year

si=principal*roi*t

print('Simple interest on the stated amount is %.2f'\
      %(si))
    

ci=principal*(np.exp(roi*t)-1)

print('Contimous compound interest on the stated amount is %.2f'\
      %(ci))

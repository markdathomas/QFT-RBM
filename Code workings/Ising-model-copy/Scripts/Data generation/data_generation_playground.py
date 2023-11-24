# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:58:48 2021

@author: Mark Thomas
"""
import os
import sys
from generate_data import run



def repeat_elements(arr, N):
    return [elem for elem in arr for _ in range(N)]



alpha_size_list = [0.2*2**(-i) for i in range(4)]

#alpha_size_list = [1,0.1,0.01,0.001,0.0001,0.00001,0.000001]

N_repeats = 1
alpha_list = repeat_elements(alpha_size_list, N_repeats)

step_size_list = [int(3*10**3) for i in range(len(alpha_list))]

print()
print("SPECS:")
print()
print(step_size_list)
print(alpha_list)
print("Repeats: ", N_repeats)
print()

m_visible = 6
n_hidden = 6
k_steps_list = [5 for i in range(len(step_size_list))]
batch_size = 10
save = True

output_location = run(step_size_list, m_visible, n_hidden, alpha_list, k_steps_list, batch_size)
print("Location of output saved data is: ", output_location)
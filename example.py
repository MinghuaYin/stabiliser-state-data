import pickle
import numpy as np

with open('4_qubit_stab_states.data', 'rb') as file:
    stab_states = pickle.load(file)

example_stab = stab_states[420]
print(example_stab['vector'])
print()
print(example_stab['check_matrix'])

import numpy as np

def calculate(given_list):
    if len(given_list) < 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(given_list).reshape((3, 3))
    calculations = {
        'mean': [list(array.mean(axis=0)), list(array.mean(axis=1)), array.mean()],
        'variance': [list(array.var(axis=0)), list(array.var(axis=1)), array.var()],
        'standard deviation': [list(array.std(axis=0)), list(array.std(axis=1)), array.std()],
        'max': [list(array.max(axis=0)), list(array.max(axis=1)), array.max()],
        'min': [list(array.min(axis=0)), list(array.min(axis=1)), array.min()],
        'sum': [list(array.sum(axis=0)), list(array.sum(axis=1)), array.sum()]
    }

    return calculations

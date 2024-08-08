# Creating tensors from np arrays

import tensorflow as tf
import numpy as np

def all_ones(shape):
    '''
    Creates a tensor
    
    Args:
        - Shape: Is the shape of the tensor
        
    Retursn: tf object'''
    
    if not isinstance(shape, list):
        raise ValueError(f'Shape must be a list')
    
    for item in shape:
        if type(item) != int:
            raise ValueError(f'All list elements must be integers')
        
    return tf.ones(shape=shape)


if __name__ == '__main__':
    print(all_ones([4, 3]))
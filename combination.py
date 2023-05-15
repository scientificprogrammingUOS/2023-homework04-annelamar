import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array_one, array_two, axis=0):
    array_one = np.squeeze(array_one)
    array_two = np.squeeze (array_two)
    """try:
        array = np.concatenate((array_one, array_two), axis=axis)
        return array
    except ValueError as e:
        raise ValueError("Arrays could not be combined along the given axis") from e"""
    for i in range(array_one.ndim):
        if i != axis:
            if array_one.shape[i] != array_two.shape[i]:
                raise ValueError("axes are not matching!")
            
    for i in range (array_two.ndim):
        if i != axis:
            if array_one.shape[i] != array_two.shape[i]:
                raise ValueError("axes are not matching!")
            
    arr = np.concatenate([array_one, array_two], axis)
    return arr



if __name__ == "__main__":
    arr1 = np.array([[1,2],[3,4]])
    arr2 = np.array([[5,6],[7,8]])
    print(combination(arr1, arr2))

    pass

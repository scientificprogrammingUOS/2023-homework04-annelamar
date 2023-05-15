import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    (m,n) = shape
    arrange = np.full(shape, False, dtype=bool)

    arrange[0:m+1:3, 0:n+1:3] = True
    arrange[1:m+1:3, 2:n+1:3] = True
    arrange[2:m+1:3, 1:n+1:3] = True
    
    return arrange


if __name__ == "__main__":
    print(strange_pattern((7,5)))

    pass

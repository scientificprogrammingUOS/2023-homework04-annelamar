import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
        if not isinstance(loc, (int, float)):
               loc = float(loc)
        if not isinstance(scale, (int, float)):
               scale = float(scale)
        if not isinstance(lower_bound,(int, float)):
              lower_bound = float(lower_bound)
        if not isinstance(upper_bound, (int, float)):
              upper_bound = float(upper_bound)
        
        if lower_bound >= upper_bound:
              raise ValueError("lower_bound must be smaller than upper_bound")
        samples = np.random.normal(loc, scale, size=100)

        mask = np.logical_and (samples <= upper_bound, samples >= lower_bound)
        samples = samples[mask]
        mean = np.mean(samples)
        std = np.std(samples)
        return mean, std



if __name__ == "__main__":
    gaussian_analysis(0,1,3,4)

    pass

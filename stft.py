from scipy.signal import stft
from scipy.stats import skew, kurtosis
import numpy as nm

def convertMappingToSTFT(array):
    f, t, zxx = stft(array)

    # flatten the array
    flat = zxx.flatten()
    real = [ele.real for ele in flat]
    imag = [ele.imag for ele in flat]

    # calculate features
    # 1. sum
    # 2. mean
    # 3. variance
    # 4. standard deviation
    # 5. skewness
    # 6. kurtosis
    data = [nm.sum(real), nm.sum(imag), nm.mean(real), nm.mean(imag), nm.std(real), nm.std(imag), nm.var(real),
            nm.var(imag), skew(real), skew(imag), kurtosis(real), kurtosis(imag)]
    return data

import numpy as np
from scipy.stats import skew, kurtosis

def main():
    # Sample dataset
    data = np.array([2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8])

    # Calculate skewness and kurtosis
    skewness_value = skew(data)
    kurtosis_value = kurtosis(data)

    # Display the results
    print("Dataset:", data)
    print("Skewness:", skewness_value)
    print("Kurtosis:", kurtosis_value)

    # Interpretation of skewness and kurtosis
    interpret_skewness(skewness_value)
    interpret_kurtosis(kurtosis_value)

def interpret_skewness(skewness):
    if skewness > 0:
        print("The distribution is positively skewed.")
    elif skewness < 0:
        print("The distribution is negatively skewed.")
    else:
        print("The distribution is symmetric.")

def interpret_kurtosis(kurtosis):
    if kurtosis > 3:
        print("The distribution is leptokurtic (heavy-tailed).")
    elif kurtosis < 3:
        print("The distribution is platykurtic (light-tailed).")
    else:
        print("The distribution has a normal kurtosis.")

if __name__ == "__main__":
    main()

import numpy as np

def coeff_error(params:np.ndarray, true_betas:np.ndarray)-> float:
    """
    Calculates the mean absolute error between the estimated coefficients and the true coefficients.
    Args:
      params (np.ndarray): the estimated coefficients
      true_betas (np.ndarray): the true coefficients
    Returns:
      float: the mean absolute error between the estimated coefficients and the true coefficients
    """
    return np.abs(params-true_betas).mean()

def coeff_flip_signs(params: np.ndarray, true_betas: np.ndarray)-> int:
    """
    Count the number of times the estimated coefficients have the opposite sign of the true coefficients.

    Args:
      params (np.ndarray): the estimated coefficients
      true_betas (np.ndarray): the true coefficients

    Returns:
      int: the number of times the estimated coefficients have the opposite sign of the true coefficients
    """
    
    return np.sum((np.sign(params)!=np.sign(true_betas)) & (true_betas!=0))
  
def significance_error(p_values: np.ndarray, true_betas: np.ndarray, threshold:float=.05)-> int:
    """Count the numbe of p-values that are significant when the true coefficient is zero and vice versa.

    Args:
      p_values (np.ndarray): p-values from the estimated coefficients
      true_betas (np.ndarray): the true coefficients
      threshold (float, optional): p-value threshold for significance. Defaults to .05.

    Returns:
      int: the number of p-values that are significant when the true coefficient is zero and vice versa.
    """
    return np.sum(p_values[true_betas==0]<threshold) + np.sum(p_values[true_betas!=0]>threshold)
  

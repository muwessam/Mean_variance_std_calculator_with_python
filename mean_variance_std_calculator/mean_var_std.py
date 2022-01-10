import numpy as np

def calculate(list1):
  
  if len(list1) != 9:
    raise ValueError("List must contain nine numbers.")
  arr = np.array(list1).reshape(3,3)
  mean = [[np.mean(arr[:,i]) for i in range(3)], [np.mean(arr[i]) for i in range(3)], np.mean(list1)]
  variance = [[np.var(arr[:,i]) for i in range(3)], [np.var(arr[i]) for i in range(3)], np.var(list1)]
  standard_deviation = [[np.std(arr[:,i]) for i in range(3)], [np.std(arr[i]) for i in range(3)], np.std(list1)]
  maximum = [[np.max(arr[:,i]) for i in range(3)], [np.max(arr[i, :]) for i in range(3)], np.max(list1)]
  minimum = [[np.min(arr[:,i]) for i in range(3)], [np.min(arr[i]) for i in range(3)], np.min(list1)]
  summation = [[np.sum(arr[:,i]) for i in range(3)], [np.sum(arr[i]) for i in range(3)], np.sum(list1)]
  calculations = {
    'mean': mean,
    'variance': variance,
    'standard deviation': standard_deviation,
    'max': maximum,
    'min': minimum,
    'sum': summation
}

  return calculations
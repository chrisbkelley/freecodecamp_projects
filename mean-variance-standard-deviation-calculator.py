import numpy as np

def calculate(input_list):
  # validates that input is a list of 9 values
  if len(input_list) != 9 or isinstance(input_list,list) != True:
      raise ValueError("List must contain nine numbers.")
  else:
    # converts list to a 3x3 numpy array
    reshaped_list = np.asarray(input_list)
    reshaped_list = reshaped_list.reshape(3,3)

    #creates lists of mean, variance, standard dev, max, min and sum of each dimesion and flattened value
    #TODO: write a function to eliminate the code reuse
    mean_list = [np.mean(reshaped_list, axis=0).tolist(),np.mean(reshaped_list, axis=1).tolist(),np.mean(reshaped_list).tolist()]

    var_list = [np.var(reshaped_list, axis=0).tolist(),np.var(reshaped_list, axis=1).tolist(),np.var(reshaped_list).tolist()]

    std_list = [np.std(reshaped_list, axis=0).tolist(), np.std(reshaped_list, axis=1).tolist(), np.std(reshaped_list).tolist()]

    max_list = [np.amax(reshaped_list, axis=0).tolist(),np.amax(reshaped_list, axis=1).tolist(),np.amax(reshaped_list).tolist()]

    min_list = [np.amin(reshaped_list, axis=0).tolist(),np.amin(reshaped_list, axis=1).tolist(),np.amin(reshaped_list).tolist()]

    sum_list = [np.sum(reshaped_list, axis=0).tolist(),np.sum(reshaped_list, axis=1).tolist(),np.sum(reshaped_list).tolist()]

    # make a dictionary of lists
    calculations = dict({'mean':mean_list, 'variance':var_list, 'standard deviation':std_list, 'max':max_list, 'min':min_list, 'sum':sum_list}) 

  return calculations

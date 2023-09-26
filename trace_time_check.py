import numpy as np
import time
import matplotlib.pyplot as plt

mat = [[2,1,1,1],[1,3,1,1],[1,1,4,1],[1,1,1,5]] # Insert a square matrix


rows,columns = np.shape(mat) # Save the number of rows and columns

def recursive_trace(matrix): # Defining a Function that calculates Trace using Recursion
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    else:
        return matrix[0][0] + recursive_trace([matrix[i][1:] for i in range(1, n)])

if  rows == columns:

  t0 = time.time()
  trace = np.einsum('ii', mat) # Calculating Trace Using EinSum
  print("Trace Using EinSum = ", trace)
  t1 = time.time()

  t2 = time.time()
  trace = np.trace(mat) # Calculating Trace Using NumPy
  print("Trace Using NumPy = ", trace)
  t3 = time.time()

  t4 = time.time()
  trace = sum(mat[i][i] for i in range(len(mat))) # Calculating Trace Using List Comprehension
  print("Trace Using List Comprehension = ", trace)
  t5 = time.time()


  #Calculating Trace using For Loop
  t6 = time.time()
  trace = 0
  for j in range(len(mat)):
    trace = trace + mat[j][j]
  print("Trace Using For Loop = ", trace)
  t7 = time.time()


  #Calculating Trace using While Loop

  t8 = time.time()
  trace = 0
  i=0

  while i < len(mat):
    trace = trace + mat[i][i]
    i=i+1

  print("Trace Using While Loop = ", trace)
  t9 = time.time()


  # Calculating Trace using SymPy

  from sympy import Matrix

  t10 = time.time()
  matrix = Matrix(mat)

  trace = matrix.trace()

  print("Trace Using SymPy = ", trace)
  t11 = time.time()

  # Calculating Trace Using Recursion
  t12 = time.time()
  trace = recursive_trace(mat)
  t13 = time.time()
  print("Trace Using Recursion = ", trace)

  # Plotting Results

  # Lists of what will be plotted
  method = ["EinSum","NumPy","List\nComprehension",
          "For Loop", "While Loop","SymPy"] # List of Methods Used

  dt = [t1-t0, t3-t2, t5-t4, t7-t6, t9-t8, t11-t10] # Time it took for each method


  # Create a bar graph
  plt.figure(figsize=(8, 6))  # Optional: Set the figure size
  plt.bar(method, dt)

  # Adding labels and title
  plt.xlabel('Method')
  plt.ylabel('Time (s)')
  plt.title('Execution Time of a Program Calculating Trace of a {}x{} Matrix'.format(rows,rows))

  # Display the plot
  plt.show()

else:
    print("The Matrix You Inserted Is Not Square. The Trace Operator is Only Defined For Square Matrices. Please Insert A Square Matrix")

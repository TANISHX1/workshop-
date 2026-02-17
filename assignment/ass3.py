import numpy as np

arr = np.arange(1,17).reshape(4,4)
print("Original :\n",arr)

arr_br = arr[2:,2:]
print("Bottom Right [2x2] : \n",arr_br)
print("*"*60)
# ------------------------------------

# Q2
print("Q2\n")
arr = np.random.randint(1,10,9).reshape(3,3)
print("Original :\n",arr)
# arr = arr.reshape(1,-1)
arr = arr.flatten()
print("1D :\n",arr)
print("*"*60)
# ------------------------------------

# Q3
print("Q3")
arr = np.random.randint(1,21,10)
arr_cum_sum = arr.cumsum()
arr_cum_pro = arr.cumprod()
print("Original :\n",arr)
print(f"\n CumSum : {arr_cum_sum}\n Cumprod : {arr_cum_pro}")
print("*"*60)
# ------------------------------------

# Q5
print("Q5")
arr = np.random.randint(1,200,10)
print("Original : ",arr)
arrs = np.sort(arr)
arrs = np.flip(arrs)
print("Sorted : ",arrs)
print(f"Max Value index : {arr.argmax()}")
print("*"*60)
# ------------------------------------

# Q6
print("Q6")
arr = np.random.randint(1,100,9).reshape(3,3)
determinent = np.linalg.det(arr)
inverse = np.linalg.inv(arr)
print("Original :\n",arr)
print(f"Determinant : {determinent}\n Inverse :\n{inverse}")

import numpy as np

# Q1
arr = np.arange(1,13)

arr = arr.reshape(3,4)
print(f"original : \n{arr}")
arr = arr.reshape(2,6)
print(f"Reshaped : \n{arr}")
print("*"*60)
# ------------------------------------

# Q2
rand_arr = np.random.randint(0,50,20)
print(f"Original :\n{rand_arr}")
print(f"Mean: {np.mean(rand_arr)}")
print(f"std deviation: {np.std(rand_arr)}")
print(f"Median : {np.median(rand_arr)}")
print("*"*60)
# ------------------------------------

# Q3
arr= np.eye(3,3)
arr_n = np.array([1,2,3]).reshape(-1,1) # 1 means , i want exactly one column ans -1 means automatically calculate the rows
arr_final = arr*arr_n

row_mean = np.mean(arr_final,axis=1,keepdims=True)
arr_final = arr_final - row_mean
print(arr_final) 
print("*"*60)
# ------------------------------------

# Q4
arr = np.array([1,2,3,4,5,6,7,8,3])
mean_value  = np.mean(arr)
mask = arr>mean_value
print(f"Mean : {mean_value}")
print(mask)
print(arr[mask])
print("*"*60)
# ------------------------------------

# Q5
arr1 = np.array([[1,2,3,4,5],[6,7,8,9,0]])
arr2 = np.array([[10,20,30,40,50],[60,70,80,90,100]])
arrv12 = np.vstack([arr1,arr2])
print(arrv12)

result = np.vsplit(arrv12,2)
print(f"Arr1 : \n{result[0]}")
print(f"Arr2 : \n{result[1]}")
print("*"*60)
# ------------------------------------

# Q6
rand_arr = np.random.randint(0,11,6)
print(f"Original : {rand_arr}")

rand_arr[rand_arr >5]  = 0
print(rand_arr)
print("*"*60)
# ------------------------------------

# Q7
arr = np.random.randint(0,20,6)
arr = np.reshape(arr,(2,3))
print(f"Original : \n{arr}")
arr = np.transpose(arr)
print(arr)
print("*"*60)
# ------------------------------------

# Q8
arr = (np.random.randint(0,100,16)).reshape(4,4)
print(f"Original : \n{arr}")
arr_new = arr[1:3,(0,2)]
print("\n",arr_new)
print("*"*60)
# ------------------------------------

# Q9
arr = np.random.randint(1,11,8).reshape(2,4)
mask_even = arr %2 ==0
mask_odd = arr%2 !=0
print(f"Original : \n{arr}\n")
arr[mask_even] += 5
arr[mask_odd] -= 3
print(arr)

print("*"*60)
# ------------------------------------

# Q10
arr1 = np.random.randint(1,20,16).reshape(4,4)
arr2 = np.random.randint(1,20,16).reshape(4,4)

arr12m = arr1 @ arr2
print(f"Original : \n{arr12m}")
# arr12m = np.eye(4,4)* arr12m
dignam_sum = np.trace(arr12m)

print(f"final matrix :\n",arr12m,"\n")
print(f"Sum is {dignam_sum}")
from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(size):
        min_ = i
        for j in range(ind + 1, size):
            if array[j] < array[min_]:
                min_ = j
         # swapping the elements to sort the array
        (array[i], array[min_]) = (array[min_], array[i])

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))

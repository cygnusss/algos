''' 
Bubble Sort algorithm for each iteration finds the greatest value and bubbles it up to the last index of the array
Every next iteration will have one less item since the last item becomes sorted
'''

def bubbleSort(list):
  for i in range (0, len(list) - 1):
    for j in range (0, len(list) - 1 - i):
      if list[j] > list[j + 1]:
        # if current element is greater than its right neighbor
        # swap the two elements
        list[j], list[j + 1] = list[j + 1], list[j]
  return list

example = [1, 2, 3, 4, 5]
print(bubbleSort(example))
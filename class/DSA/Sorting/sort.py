#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:39:24 2024

@author: sevak
"""



def quick_sort(arr, low=0, high=None):

  if high is None:
    high = len(arr) - 1

  if low < high:
    pivot_index = partition(arr, low, high)
    quick_sort(arr, low, pivot_index - 1)  # Sort left sub-array
    quick_sort(arr, pivot_index + 1, high)  # Sort right sub-array

  return arr
def partition(arr, p, high):
 
  pivot = arr[high]  # Now the pivot is the last element
  i = p - 1  # Index for elements less than pivot

  for j in range(p, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]  #swapping
      
  # Swap pivot to its final position 
  arr[high], arr[i + 1] = arr[i + 1], arr[high]
  return i + 1


def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        index = int(num * len(arr))
        buckets[index].append(num)
    
    for bucket in buckets:
        bucket.sort()
    
    sorted_arr = [num for bucket in buckets for num in bucket]
    
    return sorted_arr

def shell_sort(arr):

  # Choose an appropriate increment sequence like Knuth's sequence
  h = 1
  while(h < len(arr)/3):
      h = 3*h + 1
        
  while h > 0:
    for i in range(h, len(arr)):
      current = arr[i]
      j = i - h
      while j >= 0 and arr[j] > current:
        arr[j + h] = arr[j]
        j -= h
      arr[j + h] = current
      
    # print(arr)  
    h //= 3  # Reduce the increment size for the next iteration


  return arr


def insertion_sort(arr):

 for k in range(1, len(arr)): # from 1 to n-1
  
  cur = arr[k] # current element to be inserted
  j = k # ﬁnd correct index j for current
  while j > 0 and arr[j-1] > cur: # element A[j-1] must be after current
    arr[j] = arr[j-1]
    j -= 1
    
  arr[j] = cur #final position for the current value
 
 return arr
 

def bubble_sort(arr):

  n = len(arr)

  for i in range(n - 1):
    swap = False  
    
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swap = True
    
    if not swap:
        break
    
  return arr

def selection_sort(arr):

  for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr



def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage
# arr = [18, 72, 23, 41, 13, 9, 6, 1, 5, 11]
arr = [1, 5, 6, 9, 11, 13, 18, 23, 41, 72]
arr = [72, 50, 48, 41,33, 23, 20, 19, 18,16, 14, 13, 11, 9, 6, 5, 1]

sorted_arr = insertion_sort(arr.copy())  # Use copy to avoid modifying original list
print("Insertion Sort:", sorted_arr)

sorted_arr = bubble_sort(arr.copy())
print("Bubble Sort:", sorted_arr)

sorted_arr = selection_sort(arr.copy())
print("Selection Sort:", sorted_arr)

sorted_arr = quick_sort(arr.copy())
print("Quick Sort:", sorted_arr)

arr=[72, 50, 48, 41,33, 23, 20, 19, 18,16, 14, 13, 11, 9, 6, 5, 1]
sorted_arr = shell_sort(arr.copy())
print("Shell Sort:", sorted_arr)

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_arr = bucket_sort(arr)
print("Bucket Sort:", sorted_arr)

arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr =radix_sort(arr)
print("Radix Sort:", sorted_arr)
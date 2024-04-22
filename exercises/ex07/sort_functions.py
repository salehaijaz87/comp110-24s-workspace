"""Functions that implement sorting algorithms."""

__author__ = "730664950"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.

    Insert into an already sorted list.
    """
    for sorted_idx in range(len(x) - 1): 
        unsorted_idx = sorted_idx + 1
        current_elem = x[unsorted_idx]  # stores the current element
        while unsorted_idx > 0 and current_elem < x[unsorted_idx - 1]:  # Swap the elements
            x[unsorted_idx - 1], x[unsorted_idx] = x[unsorted_idx], x[unsorted_idx - 1]
            unsorted_idx -= 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    
    Repeatedly find the minimum and swap it.
    """
    idx_counter = 0  # Tracking the variables
    while idx_counter < len(x): 
        idx1_counter = idx_counter  # This will go through the unsorted numbers
        min_idx = idx_counter
        while idx1_counter < len(x):  # This will find the minimum elem in the unosorted part
            if x[idx1_counter] < x[min_idx]:  
                min_idx = idx1_counter
            idx1_counter += 1
        if x[min_idx] < x[idx_counter]:  # if min_idx is smaller than idx_counter, they will swap
            a: int = x[idx_counter]  # Temporary int variable
            x[idx_counter] = x[min_idx]
            x[min_idx] = a
        idx_counter += 1  
    return None
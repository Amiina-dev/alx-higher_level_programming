"""
Contains the function find_peak to find the peak
"""

def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers
    """
    list = list_of_integers
    l = len(list)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or list[m] >= list[m + 1]) and (m == 0 or list[m] >= list[m - 1]):
        return list[m]
    if m != l - 1 and list[m + 1] > list[m]:
        return find_peak(list[m + 1:])
     return find_peak(list[:m])

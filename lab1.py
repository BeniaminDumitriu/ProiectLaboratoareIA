def max_list(lst):
    """Returnează elementul maxim din lista de numere întregi."""
    return max(lst)

def min_list(lst):
    """Returnează elementul minim din lista de numere întregi."""
    return min(lst)

def sum_list(lst):
    """Returnează suma elementelor din lista de numere întregi."""
    return sum(lst)

def avg_list(lst):
    """Returnează media elementelor din lista de numere întregi."""
    return sum(lst) / len(lst)

myList = [14, 80, 75, 85, 90, 95]

print(max_list(myList))  # output: 95
print(min_list(myList))  # output: 14
print(sum_list(myList))  # output: 439
print(avg_list(myList))  # output: 73.16666666666667

print(round(avg_list(myList)))  # output: 73
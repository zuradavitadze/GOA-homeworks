import math

def find_next_square(sq):
    root = math.sqrt(sq)
    if int(root + 0.5) ** 2 == sq:  # Check if it's a perfect square
        next_root = root + 1
        return int(next_root ** 2) 
    else:
        return -1
    


    def min_max(lst):
  return [min(lst), max(lst)]



def series_sum(n):
    if n == 0:
        return "0.00"
    
    total = 0
    denominator = 1
    
    for _ in range(n):
        total += 1 / denominator
        denominator += 3
        
    return "{:.2f}".format(total)
from collections import Counter
  
n_num = [1,3,4,2,1,4,6]
n = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode :" + ', '.join(map(str, mode))
      
print(get_mode)
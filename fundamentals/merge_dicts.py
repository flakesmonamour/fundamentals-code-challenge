def merge_dicts(dict1, dict2):
    merged=dict1.copy()
    for key,value in dict2.items():
        if key in merged:
          merged[key] += value
    else:
        merged[key] = value
    return merged

dict1 = {'a': 30, 'b': 26, 'c':45}
dict2 = {'a': 8, 'c': 20, 'd':10}

merge_dict = merge_dicts(dict1, dict2)

print (merge_dict)
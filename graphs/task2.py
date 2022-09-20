n, m = 3, 3

input_lines = [
    [1, 2],
    [2, 3],
    [1, 2]
]

def check_if_loop(lines: list) -> bool:
    """ Returns True if loop was detected """
    
    for pair in lines:
        if pair[0] == pair[1]:
            return True
        
    return False


def check_if_multiple_edges(lines: list) -> bool:
    """ Returns True if multiple edges were detected """
    
    unique_list = []
    for pair in lines:
        if pair not in unique_list:
            unique_list.append(pair)
        else:
            return True
        
    return False


loop_res = check_if_loop(input_lines)
edges_res = check_if_multiple_edges(input_lines)

# just a graph?
if edges_res is False and loop_res is False:
    print("Yes")
else:
    print("No")
    
    
# multigraph
if not loop_res:
    print("Yes")
else:
    print("No")



# pseudograph
print("Yes")





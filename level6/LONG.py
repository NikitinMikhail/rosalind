import common

'''
Too straight solution, but it should work as intended with 50 strings.

'''


def get_superstrings(adj_list):
    superstrings = [list(item) for item in adj_list]
    #    print(superstrings)
    for _ in adj_list:
        for item in adj_list:
            for inner_item in superstrings:
                if item[1] == inner_item[0] and item[0] not in inner_item and [item[0]] + inner_item not in superstrings:
                    superstrings.append([item[0]] + inner_item)
                    if len(inner_item) == len(fasta_dict) - 1:
                        return superstrings
                if item[0] == inner_item[len(inner_item) - 1] and item[1] not in inner_item and inner_item + [
                    item[1]] not in superstrings:
                    superstrings.append(inner_item + [item[1]])
                    if len(inner_item) == len(fasta_dict) - 1:
                        return superstrings


def build_superstring(fasta_dict, keys_list):
    overlap_len = len(fasta_dict[keys_list[0]]) // 2
    superstring = fasta_dict[keys_list[0]]
    for index in range(1, len(keys_list)):
        new_string = fasta_dict[keys_list[index]]
        overlap_start = common.substring_positions(new_string, superstring[-overlap_len:])[0]
        superstring += new_string[overlap_start + overlap_len:]
    return superstring


fasta_dict = common.fasta_parser('LONG.txt')
adj_list = list()

for key in fasta_dict.keys():
    for inner_key in fasta_dict.keys():
        if common.overlapping(fasta_dict[key], fasta_dict[inner_key]) and key != inner_key:
            adj_list.append((key, inner_key))
print(len(adj_list))
longest_path = sorted(get_superstrings(adj_list), key=len)[-1]
print(longest_path)
print(build_superstring(fasta_dict, longest_path))
def strcodes(s):
    return [ord(c) for c in s]


def strsum(s):
    return sum(strcodes(s))


def print_dict(d):
    print('\n'.join([f'{k}\t{v}' for (k, v) in sorted(d.items())]))


def add_dict(d1, d2):
    return {**d2, **d1}


def union(l1, l2):
    return list(set().union(l1, l2))


def diff(l1, l2):
    return list(set(l1) - set(l2))


def flatten(nested_list):
    return [item for sublist in nested_list for item in flatten(sublist)] \
        if type(nested_list) in [list, tuple] else [nested_list]

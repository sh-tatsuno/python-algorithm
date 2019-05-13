import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system

    Returns:
        a list of paths
    """

    if suffix[0] != ".":
        raise "suffix should be start '.'"

    ret = []

    files = os.listdir(path)
    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            ret += find_files(suffix, full_path)
        else:
            if full_path[-len(suffix):] == suffix:
                ret.append(full_path)

    return ret

def assertion(v1, v2):
    assert set(v1) == set(v2), "actual: {0}, expected: {1}".format(v1, v2)

# .c
c_list = ['testdir/t1.c', 'testdir/subdir1/a.c', 'testdir/subdir5/a.c', 'testdir/subdir3/subsubdir1/b.c']
assertion(find_files(".c", "testdir"), c_list)

# .h
h_list = ['testdir/t1.h', 'testdir/subdir1/a.h', 'testdir/subdir5/a.h', 'testdir/subdir3/subsubdir1/b.h']
assertion(find_files(".h", "testdir"), h_list)

# .py
py_list = []
assertion(find_files(".py", "testdir"), py_list)
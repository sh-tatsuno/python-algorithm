class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    """

    '''
    Solution:
        1. Input root group.
        2. Search a user in a node.
        3. If there is not the user in the group, move next group deeper. 
            -> depth first search 
    '''

    if user in group.get_users():
        return True
    for child_group in group.get_groups():
        ret = is_user_in_group(user, child_group)
        if ret: return True
    return False

def assertion(case, user, group, ret):
    assert ret == is_user_in_group(user, group), "The result is different as expected."
    print("test case: {0} Passed!\n".format(case))

if __name__ == "__main__":

    # data for test 1, 2
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # test 1
    assertion("normal & sub child", "sub_child_user", parent, True)

    # test 2
    assertion("normal & False", "sub_child_user2", parent, False)

    user = "user2"
    parent.add_user(user)
    child = Group("child2")
    user = "child_user3"
    child.add_user(user)
    user = "child_user4"
    child.add_user(user)
    sub_child = Group("subchild2")
    sub_child_user = "sub_child_user5"
    sub_child.add_user(sub_child_user)
    sub_child_user = "sub_child_user6"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # test 3, more complicated case
    assertion("normal & parent", "user2", parent, True)
    assertion("normal & child", "child_user4", parent, True)
    assertion("normal & sub child", "sub_child_user6", parent, True)
    assertion("normal & False", "sub_child_user7", parent, False)

    # test 4, empty case
    parent = Group("parent")
    assertion("empty", "user", parent, False)
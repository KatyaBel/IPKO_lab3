from my_lib import bubble_sort


def test1():
    my_list1 = [1, -5, 7]
    my_list2 = [-5, 1, 7]
    assert bubble_sort(my_list1) == my_list2


def test2():
    my_list1 = [63, 80, 62, 69, 71, 37, 12, 90, 19, 67]
    my_list2 = [12, 19, 37, 62, 63, 67, 69, 71, 80, 90]
    assert bubble_sort(my_list1) == my_list2


def test3():
    my_list1 = [12, 7.2, 4]
    my_list2 = [4, 7.2, 12]
    assert bubble_sort(my_list1) == my_list2


def test4():
    my_list1 = []
    my_list2 = []
    assert bubble_sort(my_list1) == my_list2
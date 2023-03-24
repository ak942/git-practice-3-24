def most_common_value(number_list):
    """ returns the most common element of the list
    """
    common_numbers = {}
    for nums in number_list:
        if nums in common_numbers:
            common_numbers[nums] +=1
        else:
            common_numbers[nums] = 1
    highest_number = 0
    highest_count = 0
    for key, value in common_numbers.items():
        if value > highest_count:
            highest_count = value
            highest_number = key
    return highest_number


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")

def merge_lists(list_a, list_b):
    """ Returns a new list which is
        a combination of list_a and list_b
        without any duplicate elements.
    """
    return list(set(list_a) | set(list_b))

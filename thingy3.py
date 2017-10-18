"""Subsequence."""


def create_substrings(string):
    """Create list of substrings of string1."""
    substring_list = []
    for i in range(len(string)):
        substring_list.append(string[0:i])
    return substring_list


def find_substrings(substring_list, other_string):
    largest_string = ""
    for substring in substring_list:
        if other_string.find(substring) != -1:
            if len(largest_string) < len(substring):
                largest_string = substring
    return len(largest_string)

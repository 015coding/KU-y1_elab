def merge(a, b):
    i = 0
    j = 0
    len_a = len(a)
    len_b = len(b)
    merge_lst = []

    # Helper function to convert a string to a list of ASCII values
    def to_ascii_list(s):
        return [ord(char) for char in s]

    # Convert all strings in both lists to their ASCII representations
    ord_a = [to_ascii_list(item) for item in a]
    ord_b = [to_ascii_list(item) for item in b]

    # Merge the two lists based on their ASCII values
    while i < len_a and j < len_b:
        # Compare two lists of ASCII values
        if ord_a[i] < ord_b[j]:
            merge_lst.append(a[i])
            i += 1
        else:
            merge_lst.append(b[j])
            j += 1

    # Append any remaining elements from list a
    while i < len_a:
        merge_lst.append(a[i])
        i += 1

    # Append any remaining elements from list b
    while j < len_b:
        merge_lst.append(b[j])
        j += 1

    return merge_lst

# Example usage with strings
str_list1 = ["apple", "banana", "cherry"]
str_list2 = ["avocado", "blueberry", "date"]

print(merge(str_list1, str_list2))
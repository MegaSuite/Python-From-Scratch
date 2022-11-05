nums = [1,6,4,3,5,2]
def get_max(list):
    max_value = list[0]
    for i in range(1, len(list)):
        if max_value < list[i]:
            max_value = list[i]
    print(max_value)
get_max(nums)

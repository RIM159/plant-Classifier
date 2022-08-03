"""
27.移除元素
step
    設定快指針與慢指針
    快指針(fast)：尋找新數組的元素，新數組就是不含有目標數組的位置
    慢指針(slow)：指向更新，新數組下標的位置
    在無調用移除的函數下，選擇了用覆蓋的方式進行循環


"""


def def_number(nums, target):
    """

    :param nums: 指定數組
    :param target: 目標數
    :return: 返回最後快指針的下標位
    """
    slow = 0
    fast = 0
    while slow < len(nums):
        if nums[slow] != target:
            nums[fast] = nums[slow]  # 覆蓋
            fast += 1
        slow += 1
    return fast


def def_number2(nums, target):
    if nums is None or len(nums) == 0:
        return 0
    l = 0
    r = len(nums) - 1
    while l < r:
        while (l < r and nums[l] != target):
            l += 1
        while (l < r and nums[r] == target):
            r -= 1
        nums[l], nums[r] = nums[r], nums[l]  # 左右轉置，讓搜索範圍縮小
    print(nums)
    if nums[l] == target:
        return l
    else:
        return l + 1


a = def_number([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(a)

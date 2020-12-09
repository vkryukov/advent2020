from utils import *

nums = read_integers(9)


def not_a_sum(numbers, a):
    for x, y in combinations(numbers, 2):
        if x + y == a:
            return False
    return True


def find_invalid():
    for i in range(25,len(nums)):
        if not_a_sum(nums[i-25:i], nums[i]):
            return nums[i]


def test_part1():
    assert find_invalid() == 14360655


def find_weakness(target):
    for i in range(len(nums)):
        current = nums[i]
        for j in range(i+1, len(nums)):
            current += nums[j]
            if current == target:
                return min(nums[i:j+1]) + max(nums[i:j+1])
            elif current > target:
                break


def test_part2():
    assert find_weakness(14360655) == 1962331


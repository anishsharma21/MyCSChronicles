import math

class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
            else:
                return False
        return True

    # print(canConstruct('ab', 'aa'))


    def timeConversion(s):
        first = s[:2]
        part = s[len(s) - 2:]
        s = s.replace(part, '')
        if part == 'PM' and first != '12':
            s = s.removeprefix(str(first))
            s = str(int(first) + 12) + s
        elif part == 'AM' and first == '12':
            s = s.removeprefix(str(first))
            s = '0' + str(int(first) - 12) + s
        return s

    # print(timeConversion('12:05:45AM'))


    def gradingStudents(grades):
        for grade in grades:
            if grade < 38:
                continue
            elif 5*math.ceil(grade/5) - grade < 3:
                grades[grades.index(grade)] = 5*math.ceil(grade/5)
        return grades

    # print(gradingStudents([37, 38, 39, 45, 99]))


    def countApplesAndOranges(s, t, a, b, apples, oranges):
        apples = list(map(lambda apple: apple + a, apples))
        oranges = list(map(lambda orange: orange + b, oranges))
        apples = len(list(filter(lambda apple_pos: apple_pos >= s and apple_pos <= t, apples)))
        oranges = len(list(filter(lambda orange_pos: orange_pos >= s and orange_pos <= t, oranges)))
        print(apples)
        print(oranges)

    # countApplesAndOranges(5, 9, 2, 12, [3, 6, -2], [4, 5, -5])


    def bubble_sort(arr: list):
        checks = 0
        for j in range(len(arr)-1, 0, -1):
            mod = 0
            for i in range(j):
                checks += 1
                value = arr[i]
                if value > arr[i+1]:
                    arr[i] = arr[i+1]
                    arr[i+1] = value
                    if (i != 0 or i == j - 1) and mod == 0:
                        return arr, checks
                    mod+=1
            if mod == 0:
                return arr, checks
        return arr, checks
    # sorted_arr, checks = bubble_sort([1, 2, 3, 5, 4])
    # print()
    # print(f"Checks: {checks}")
    # print(sorted_arr)
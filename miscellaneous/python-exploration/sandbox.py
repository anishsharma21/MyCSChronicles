def canConstruct(ransomNote: str, magazine: str) -> bool:
    for c in ransomNote:
        if c in magazine:
            magazine = magazine.replace(c, '', 1)
        else:
            return False
    return True

print(canConstruct('ab', 'aa'))
def check_string(st1, st2, st3):
    if st3.startswith(st1) or st3.endswith(st2):
        return True
    else:
        return False

# Ví dụ sử dụng
st1 = "abc"
st2 = "xyz"
st3 = "abcdef"
result = check_string(st1, st2, st3)
print(result)  # Output: True

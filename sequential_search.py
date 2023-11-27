def sequential_search(target, lst):
    for i, value in enumerate(lst):
        if value == target:
            return i  # 찾은 경우 해당 인덱스 반환
    return -1  # 찾지 못한 경우 -1 반환
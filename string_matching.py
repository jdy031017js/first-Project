def string_matching(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)

    for i in range(text_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            return i  # 매칭된 부분의 시작 인덱스 반환

    return -1  # 매칭되는 부분이 없을 경우 -1 반환
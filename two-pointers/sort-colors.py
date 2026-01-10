def sort_colors(colors):
    start, current = 0, 0
    end = len(colors)-1

    while current <= end:
        if colors[current] == 0:
            aux = colors[current]
            colors[current] = colors[start]
            colors[start] = aux
            current += 1
            start += 1

        elif colors[current] == 1:  
            current += 1

        else:
            aux = colors[current]
            colors[current] = colors[end]
            colors[end] = aux
            end -= 1

    return colors

def main():
    test_cases = [
        [0, 1, 1, 0, 2, 2, 0, 0],
        [1, 0, 2, 1, 2, 2],
        [2, 2, 1, 1, 0],
        [0, 0, 0, 0],
        [2, 1, 0],
        [2, 0, 1, 2, 0, 1, 2, 0, 1],
        [0, 0, 0],
        [1, 1, 1, 1, 1],
        [2, 2]
    ]

    for i, colors in enumerate(test_cases):
        sorted_colors = sort_colors(colors.copy())
        print(f"Test Case {i + 1}: Input: {colors} -> Output: {sorted_colors}")


if __name__ == "__main__":
    main()
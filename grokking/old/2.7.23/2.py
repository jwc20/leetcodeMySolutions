def insert(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1

    # skip (and add to output) all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        print(merged)
        i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        # while i < len(intervals) and intervals[i][end] >= new_interval[start]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    # insert the new_interval
    merged.append(new_interval)
    print(merged)

    # add all the remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])
        print(merged)
        i += 1
    return merged


def main():
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6]))
    )
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10]))
    )
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[2, 3], [5, 7]], [1, 4]))
    )


main()

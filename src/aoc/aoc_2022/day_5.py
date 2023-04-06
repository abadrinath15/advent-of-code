def row_to_cols(row: str) -> list[int]:
    return [int(num) for num in row.split()]


def row_to_stack(row: str) -> list[str | None]:
    res = []
    while True:
        if len(row) == 0:
            return res

        first_take = row[:3]
        row = row[3:]
        if first_take[0] == "[":
            res.append(first_take[1])
            if len(row) == 0:
                return res

        else:
            res.append(None)

        row = row[1:]

import random
from typing import List


class RandomGenerator:

    def rand(self, series: int, start_range: int, end_range: int, number: int) -> List[List[int]]:

        result = []
        for i in range(series):
            row = []
            index = 0
            while index != number:
                current = random.randrange(start_range, end_range,1)
                if current not in row:
                    row.append(current)
                    index += 1
            result.append(row)
            print(row)

        return result


if __name__ == "__main__":
    RandomGenerator().rand(6, 1, 50, 7)

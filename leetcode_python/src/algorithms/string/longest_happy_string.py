import heapq


class LongestHappyString:

    def get_longest_happy_string(self, a: int, b: int, c: int) -> str:
        result = ""
        max_heap = []
        for count, character in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(max_heap, (count, character))

        while max_heap:
            count, character = heapq.heappop(max_heap)
            if len(result) > 1 and result[-1] == result[-2] == character:
                if not max_heap:
                    break

                count_next, character_next = heapq.heappop(max_heap)
                result += character_next
                count_next += 1
                if count_next:
                    heapq.heappush(max_heap, (count_next, character_next))
            else:
                result += character
                count += 1
            if count:
                heapq.heappush(max_heap, (count, character))
        return result

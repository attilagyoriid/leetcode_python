import collections
from typing import List


class SlidingWindowMaximum:

    def calculate(self, items: List[int], window_size: int) -> List[int]:

        output = []  # hold indexes
        queue = collections.deque()  # from both end access O(1)

        left = right = 0

        while right < len(items):  # till right index in bound

            while queue and items[right] > items[queue[-1]]:
                # if queue has item and right item in the list which is the upcoming next item in the window
                # is greater than the right most item in the queue
                # we remove items from queue, we need the max item in the current window only
                # these items mut not be visited anymore cause we know that the current right item is greater

                queue.pop()

            queue.append(right)

            # if left index is greater than the left most index in the queue
            # the item in the queue is not part of the window anymore
            # remove item from left
            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= window_size:
                # if rigth index is greater than window size we must move left index to the right by one
                output.append(items[queue[0]])  # the right most index in the deque is the actual max, so we store it
                left += 1  # move left index to keep the window size
            right += 1  # increment right

        return output

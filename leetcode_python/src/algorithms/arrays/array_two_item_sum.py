class ArrayTwoItemsSum:
    @staticmethod
    def find_two_items_to_sum_up_to_value_with_backing_array(array: [], value_to_sum_ip_to: int) -> bool:
        i = 0
        complements = [None] * value_to_sum_ip_to
        for item in array:
            for j in range(len(complements)):
                if complements[j] is not None and j is item:
                    print(complements[item], i)
                    return True

            complements[value_to_sum_ip_to-item] = i
            i += 1
        return False

    @staticmethod
    def find_two_items_to_sum_up_to_value_with_backing_hashmap(array: [], value_to_sum_ip_to: int) -> bool:

        i = 0
        complements = {}
        for item in array:
            if item in complements.keys():
                print(complements[item], i)
                return True
            else:
                complements[value_to_sum_ip_to - item] = i
            i += 1
        return False

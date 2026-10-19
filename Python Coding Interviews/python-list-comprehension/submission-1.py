from typing import List


def create_list_of_odds(n: int) -> List[int]:
    num_list = [n for n in range(n+1) if n % 2 != 0]
    return num_list
    pass


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))

# author: DMH 9/26/21

free_throws = input("How many free throws were made?")

regular_baskets = input("How many regular baskets were made?")

three_pointers = input("How many three pointers were made?")

total_points = int(free_throws) + (int(regular_baskets) * 2) + (int(three_pointers) * 3)
print(total_points)
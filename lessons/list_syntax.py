"""Demonstrate Basic List Syntax"""

# Create an empty list
grocery_list: list[str] = list() # <- constructor
grocery_list: list[str] = [] # <- literal; does the same as line 4
print("Empty list:")
print(grocery_list)

# Add to a list
grocery_list.append("frosted flackes")
grocery_list.append("milk")
grocery_list.append("Pizza")
grocery_list.append("Pizza")
print("After adding things: ")
print(grocery_list)

# Making a list with the things already inside:
grocery_list2: list[str] = ["frosted flakes, milk, pizza"]
print("Already populated list")
print(grocery_list2)

print("Add another thing: ")
grocery_list2.append("whipped cream")
print(grocery_list2)

#Indexing
print("Printing one item:")
print(grocery_list[2])
# the 2 is the index of the grocery list; frosted flakes(0), milk(1), pizza(2)

# Modifying by Index
x: list[str] = ["c", "a", "r", "s"]
x[2] = "t"
print(x)

grocery_list[0] = "Cinnamon Toast Crunch"
print("Modifying: ")
print(grocery_list)

#Length of a list
print("Length: ")
print(len(grocery_list))

# Pop: Removing item from a list
grocery_list.pop(1)
print("Remove an item: ")
print(grocery_list)

print("Functions: ")
def display(my_list: list[str]) -> None:
    print(my_list)

display(grocery_list)
x = display(["Anusha", "Jack", "Vrinda"])
print(x)

def create(word1: str, word2: str) -> list[str]:
    new_list: list[str] = [word1, word2]
    return new_list

print(create("Hello", "World"))





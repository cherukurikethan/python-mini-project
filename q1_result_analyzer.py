def analyze_result(name, roll, marks):
    

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total:.1f}, Average: {average:.1f}")
    print(f"Grade: {grade}")

    below_40 = []

    for i, mark in enumerate(marks, start=1):
        if mark < 40:
            below_40.append(f"Subject {i}")

    if below_40:
        print("Subjects below 40:", ", ".join(below_40))
    else:
        print("Subjects below 40: None")



name = "Aarav"
roll = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

analyze_result(name, roll, marks)


#Discussion points answer

# discount=0 is safe because 0 is an integer, and integers are immutable in Python. This means the value 0 cannot be changed or modified in place, so using it as a default parameter does not cause the same sharing problem as a mutable object like cart=[]. Each time the function uses discount=0, it simply refers to the immutable value 0, making it safe to use as a default parameter.

#Rebinding means changing what a variable refers to by assigning it to a new object, while mutating means changing the existing object itself. For example, cart = [] is rebinding because the variable cart is made to refer to a new list, whereas cart.append("Apple") is mutation because the existing list is modified. This difference is important when working with mutable objects such as lists and dictionaries.

#Among these data types, list, dict, and set are mutable because their contents can be changed after creation. tuple, str, and int are immutable because their values cannot be changed after they are created. If we need to change an immutable object, Python creates a new object instead of modifying the existing one.

#Yes, changes to a list made inside a function can be reflected outside the function because Python passes references to objects. When a list is passed to a function, both the original variable and the function parameter refer to the same list object. Therefore, operations such as append(), remove(), or sort() modify the original list, and those changes can be seen outside the function.
# set_operations.py

def demonstrate_set_operations():
    """აჩვენებს set-ებთან მუშაობის ძირითად ოპერაციებს."""

    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}

    print("Set 1:", set1)
    print("Set 2:", set2)

    # .add() - ელემენტის დამატება
    set1.add(6)
    print(".add(6) Set 1:", set1)

    # .remove() - ელემენტის წაშლა (თუ არ არსებობს, გამოიწვევს KeyError-ს)
    set1.remove(1)
    print(".remove(1) Set 1:", set1)

    # .discard() - ელემენტის წაშლა (თუ არ არსებობს, არაფერს აკეთებს)
    set2.discard(8)  # არაფერს არ გააკეთებს, რადგან 8 არ არის set2-ში
    print(".discard(8) Set 2:", set2)
    set2.discard(7)
    print(".discard(7) Set 2:", set2)


    # .pop() - შემთხვევითი ელემენტის წაშლა და დაბრუნება (ცარიელ set-ზე გამოიწვევს KeyError-ს)
    popped_element = set1.pop()
    print(".pop() Set 1:", set1, "წაშლილი ელემენტი:", popped_element)

    # .clear() - set-ის გასუფთავება
    set2.clear()
    print(".clear() Set 2:", set2)

    # .union() - გაერთიანება
    union_set = set1.union(set2)
    print(".union() Set 1 და Set 2 (ახლა ცარიელია):", union_set)
    set2 = {3,4,5,6,7}
    union_set = set1.union(set2)
    print(".union() Set 1 და Set 2:", union_set)


    # .intersection() - თანაკვეთა
    intersection_set = set1.intersection(set2)
    print(".intersection() Set 1 და Set 2:", intersection_set)

    # .difference() - განსხვავება
    difference_set = set1.difference(set2)
    print(".difference() Set 1 და Set 2:", difference_set)

    # .symmetric_difference() - სიმეტრიული განსხვავება
    symmetric_difference_set = set1.symmetric_difference(set2)
    print(".symmetric_difference() Set 1 და Set 2:", symmetric_difference_set)

    #update() - ამატებს ელემენტებს სხვა ნაკრებიდან
    set1.update(set2)
    print(".update() set1:",set1)

    set3 = frozenset([1,2,3,4])
    print("frozenset:",set3)

if __name__ == "__main__":
    demonstrate_set_operations()
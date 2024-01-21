# Задача №1:
from pprint import pprint

with open("recipes.txt") as f:
    cook_book={}
    for i in f:
        dish_name=i.strip()
        ingredients_count=f.readline()
        dish_ingredients=[]
        for n in range(int(ingredients_count)):
            recepie=f.readline().strip().split(" | ")
            # print(recepie)
            ingedient_name=recepie[0]
            quantity=recepie[1]
            measure=recepie[2]
            dish_ingredients.append({"ingredient_name": ingedient_name, "quantity": quantity, "measure": measure})
        f.readline()
        cook_book[dish_name]=dish_ingredients
    pprint(cook_book)


    # Задача №2:
    def get_shop_list_by_dishes(dishes, person_count):
        result = {}
        for dish in dishes:
            for res in cook_book[dish]:
                if res["ingredient_name"] in result:
                    result[res["ingredient_name"]]["quantity"] += int(res["quantity"]) * person_count
                else:
                    result[res["ingredient_name"]] = {"measure": res["measure"],
                                                      "quantity": (int(res["quantity"]) * person_count)}
        pprint(result)

    get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
    get_shop_list_by_dishes(["Фахитос"], 5)  # проверка


    # Задача №3:
    with open("1.txt") as f1, open("2.txt") as f2, open("3.txt") as f3:
        f1_key = len(f1.readlines())
        f2_key = len(f2.readlines())
        f3_key = len(f3.readlines())

    with open("1.txt") as f1, open("2.txt") as f2, open("3.txt") as f3:
        f1_value = "\n".join(["1.txt", str(f1_key), f1.read()])
        f2_value = "\n".join(["2.txt", str(f2_key), f2.read()])
        f3_value = "\n".join(["3.txt", str(f3_key), f3.read()])

        file_dict = {f1_key: f1_value, f2_key: f2_value, f3_key: f3_value}
        file_dict_sorted = dict(sorted(file_dict.items()))
        file_result = "\n".join(file_dict_sorted.values())

    with open("file_result.txt", "w") as f4:
        f4.write(file_result)

    with open("file_result.txt") as f4:
        print(f4.read())

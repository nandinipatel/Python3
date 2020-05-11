menu = []
menu.append(["eggs", "spam", "bacon"])
menu.append(["eggs", "sausage", "bacon"])
menu.append(["eggs", "spam"])
menu.append(["eggs", "bacon", "spam"])
menu.append(["eggs", "bacon", "sausage", "spam"])

#print(menu)

for meal in menu:
    if not "spam" in meal:
        print(meal)

        for ingredient in meal:
            print(ingredient)
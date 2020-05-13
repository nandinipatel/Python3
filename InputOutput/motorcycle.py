import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"

    for key in bike:
        print(key)
    print('=' * 40)

    print(bike["model"])
    print(bike["color"])
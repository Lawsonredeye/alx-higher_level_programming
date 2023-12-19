#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lenght = []
    for i in range(list_length):
        try:
            lenght.append(my_list_1[i] / my_list_2[i])
        except (IndexError):
            print("out of range")
            lenght.append(0)
        except (ZeroDivisionError):
            print("division by 0")
            lenght.append(0)
        except (TypeError):
            print("wrong type")
            lenght.append(0)
        finally:
            pass
    return lenght

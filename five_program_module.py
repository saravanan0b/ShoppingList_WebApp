
USER_DATA_PATH = "shopping_list.txt"

def get_shopping_list():
    with open(USER_DATA_PATH, "r") as file_local:
        shopping_list_local = file_local.readlines()
    return shopping_list_local


def write_shopping_list(shopping_list_arg):
    with open(USER_DATA_PATH, "w") as file_local:
        file_local.writelines(shopping_list_arg)


if __name__ == "__main__":
    print("hello dev!!")
    print(get_shopping_list())


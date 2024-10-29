from core import AT


def print_item_is_list(list, pref):
    for item in list:
        print(f"{pref}{str(item)}")
        if len(item.Childs) > 0:
            print_item_is_list(item.Childs, (pref + '\t'))


if __name__ == "__main__":
    at = AT()
    login_ans = at.Login("Hronos.Black@gmail.com", "Rtu87qw1")
    print_item_is_list(at.AllGenres, '')
    print('\n')
    print('\n'.join(str(access) for access in at.AllAccesses))

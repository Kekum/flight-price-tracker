from search import build_search_list


def main():

    searches = build_search_list()

    print()

    print("Toplam Arama Sayısı :", len(searches))

    print()

    print("İlk 10 Arama")

    print("----------------")

    for search in searches[:10]:

        print(search)


if __name__ == "__main__":
    main()

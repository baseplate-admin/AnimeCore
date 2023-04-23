from shinobi.builder.genre import GenreBuilder


def test_genre_sitemap_parser():
    parser = GenreBuilder()
    dictionary = parser.build_dictionary()
    assert list(dictionary.keys()) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
    ]
    assert list(dictionary.values()) == [
        "https://myanimelist.net/anime/genre/1",
        "https://myanimelist.net/anime/genre/2",
        "https://myanimelist.net/anime/genre/3",
        "https://myanimelist.net/anime/genre/4",
        "https://myanimelist.net/anime/genre/5",
        "https://myanimelist.net/anime/genre/6",
        "https://myanimelist.net/anime/genre/7",
        "https://myanimelist.net/anime/genre/8",
        "https://myanimelist.net/anime/genre/9",
        "https://myanimelist.net/anime/genre/10",
        "https://myanimelist.net/anime/genre/11",
        "https://myanimelist.net/anime/genre/12",
        "https://myanimelist.net/anime/genre/13",
        "https://myanimelist.net/anime/genre/14",
        "https://myanimelist.net/anime/genre/15",
        "https://myanimelist.net/anime/genre/17",
        "https://myanimelist.net/anime/genre/18",
        "https://myanimelist.net/anime/genre/19",
        "https://myanimelist.net/anime/genre/20",
        "https://myanimelist.net/anime/genre/21",
        "https://myanimelist.net/anime/genre/22",
        "https://myanimelist.net/anime/genre/23",
        "https://myanimelist.net/anime/genre/24",
        "https://myanimelist.net/anime/genre/25",
        "https://myanimelist.net/anime/genre/26",
        "https://myanimelist.net/anime/genre/27",
        "https://myanimelist.net/anime/genre/28",
        "https://myanimelist.net/anime/genre/29",
        "https://myanimelist.net/anime/genre/30",
        "https://myanimelist.net/anime/genre/31",
        "https://myanimelist.net/anime/genre/32",
        "https://myanimelist.net/anime/genre/35",
        "https://myanimelist.net/anime/genre/36",
        "https://myanimelist.net/anime/genre/37",
        "https://myanimelist.net/anime/genre/38",
        "https://myanimelist.net/anime/genre/39",
        "https://myanimelist.net/anime/genre/40",
        "https://myanimelist.net/anime/genre/41",
        "https://myanimelist.net/anime/genre/42",
        "https://myanimelist.net/anime/genre/43",
        "https://myanimelist.net/anime/genre/46",
        "https://myanimelist.net/anime/genre/47",
        "https://myanimelist.net/anime/genre/48",
        "https://myanimelist.net/anime/genre/49",
        "https://myanimelist.net/anime/genre/50",
        "https://myanimelist.net/anime/genre/51",
        "https://myanimelist.net/anime/genre/52",
        "https://myanimelist.net/anime/genre/53",
        "https://myanimelist.net/anime/genre/54",
        "https://myanimelist.net/anime/genre/55",
        "https://myanimelist.net/anime/genre/56",
        "https://myanimelist.net/anime/genre/57",
        "https://myanimelist.net/anime/genre/58",
        "https://myanimelist.net/anime/genre/59",
        "https://myanimelist.net/anime/genre/60",
        "https://myanimelist.net/anime/genre/61",
        "https://myanimelist.net/anime/genre/62",
        "https://myanimelist.net/anime/genre/63",
        "https://myanimelist.net/anime/genre/64",
        "https://myanimelist.net/anime/genre/65",
        "https://myanimelist.net/anime/genre/66",
        "https://myanimelist.net/anime/genre/67",
        "https://myanimelist.net/anime/genre/68",
        "https://myanimelist.net/anime/genre/69",
        "https://myanimelist.net/anime/genre/70",
        "https://myanimelist.net/anime/genre/71",
        "https://myanimelist.net/anime/genre/72",
        "https://myanimelist.net/anime/genre/73",
        "https://myanimelist.net/anime/genre/74",
        "https://myanimelist.net/anime/genre/75",
        "https://myanimelist.net/anime/genre/76",
        "https://myanimelist.net/anime/genre/77",
        "https://myanimelist.net/anime/genre/78",
        "https://myanimelist.net/anime/genre/79",
        "https://myanimelist.net/anime/genre/80",
        "https://myanimelist.net/anime/genre/81",
    ]
    # Check if list is sorted
    # https://stackoverflow.com/a/3755251
    assert all(
        list(dictionary.keys())[i] <= list(dictionary.keys())[i + 1]
        for i in range(len(dictionary.keys()) - 1)
    )

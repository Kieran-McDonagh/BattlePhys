from bson import ObjectId

workouts_data = [
    {
        "id": ObjectId("65fedb7a8433a888c1aca57a"),
        "type": "individual",
        "title": "title 1",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "author_id": "75fedb7a8433a888c1aca57d",
        "date_created": "2024-04-05T21:00:00.000000",
    },
    {
        "id": ObjectId("65fedb7a8433a888c1aca57b"),
        "type": "individual",
        "title": "title 2",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "author_id": "75fedb7a8433a888c1aca57d",
        "date_created": "2024-04-05T21:00:00.000000",
    },
    {
        "id": ObjectId("65fedb7a8433a888c1aca57c"),
        "type": "battlephys",
        "title": "title 3",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "author_id": "85fedb7a8433a888c1aca57e",
        "date_created": "2024-04-05T21:00:00.000000",
    },
]

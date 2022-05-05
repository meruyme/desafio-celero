def get_id(class_name, name):
    if name:
        dict_season = dict(class_name.CHOICES)
        ids = [id for id, value in dict_season.items() if value == name]
        if ids:
            return ids[0]

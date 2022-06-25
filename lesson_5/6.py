color_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}


def delete_none_in_dict(dict_):
    to_delete = []
    for key, value in dict_.items():
        if value is None:
            to_delete.append(key)

    for key in to_delete:
        dict_.pop(key)


delete_none_in_dict(color_dict)
print(color_dict)

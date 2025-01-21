def string_parse():
    encoded_string = input("Enter encoded string: ")
    string_parts = [part for part in encoded_string.split('0') if part]
    first_name = string_parts[0]
    last_name = string_parts[1]
    id_value = string_parts[2]

    return {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_value
    }
result = string_parse()
print(result)




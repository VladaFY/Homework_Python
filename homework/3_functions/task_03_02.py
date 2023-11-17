from typing import List, Dict, Any, Callable


def select(*field_names: str) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
    """Return a function that selects fields from a dictionary.

    Args:
        *field_names: Variable number of field names to be selected.

    Returns:
        A function that takes a dictionary as input and returns a new dictionary
        containing only the selected fields.

    Example:
        >>> data = {'name': 'John', 'age': 25, 'city': 'New York'}
        >>> select_fields = select('name', 'age')
        >>> select_fields(data)
        {'name': 'John', 'age': 25}
    """
    def select_fields(row: Dict[str, Any]) -> Dict[str, Any]:
        friends_actual_fields = {}
        for field in field_names:
            friends_actual_fields[field] = row[field]

        return friends_actual_fields
    return select_fields


def field_filter(field_name: str, values: List[Any]) -> Callable[[Dict[str, Any]], bool]:
    """Return a function that checks if a dictionary's field is in a list of values.

    Args:
        field_name (str): The name of the field to check in the dictionary.
        values (List[Any]): The list of values to compare the field against.

    Returns:
        Callable[[Dict[str, Any]], bool]: A function that takes a dictionary and returns True if the field value is in the list of values, False otherwise.
    """
    def filter_field(dic: Dict[str, Any]) -> bool:
        return dic[field_name] in values
    return filter_field


def query(collection: List[Dict[str, Any]], *funcs: Callable[[Dict[str, Any]], Any]) -> List[Dict[str, Any]]:
    """
    Apply a series of functions to a collection of dictionaries.

    Args:
        collection (List[Dict[str, Any]]): The collection of dictionaries to apply the functions to.
        *funcs (Callable[[Dict[str, Any]], Any]): The functions to apply to each dictionary in the collection.

    Returns:
        List[Dict[str, Any]]: The modified collection of dictionaries after applying the functions.
    """
    for func in funcs:
        mapped_collection = []
        if isinstance(func(collection[0]), Dict):
            for item in collection:
                mapped_collection.append(func(item))   
            collection = mapped_collection
        else:
            for item in collection:
                if func(item):
                    mapped_collection.append(item)
            collection = mapped_collection
    return collection


friends = [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
           {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'}]


result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', ['Баскетбол', 'Волейбол']),
    field_filter('gender', ['Мужской']),
)
print(result)  # [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'}, ]

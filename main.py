def introspection_info(obj):
    """
    Функция для проведения интроспекции объекта.
    Возвращает словарь с информацией о типе, атрибутах, методах и других свойствах объекта.
    """
    # Получаем тип объекта
    obj_type = type(obj)

    # Получаем атрибуты и методы объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Получаем модуль, к которому принадлежит объект
    module = getattr(obj, "__module__", "Built-in (no module)")

    # Получаем документацию объекта (если есть)
    doc = getattr(obj, "__doc__", "No documentation available")

    # Формируем результат в виде словаря
    info = {
        "Тип объекта": obj_type,
        "Модуль": module,
        "Атрибуты": attributes,
        "Методы": methods,
        "Документация": doc.strip() if doc else "No documentation available",
    }

    return info


if __name__ == '__main__':

    for k, v in introspection_info([1, 2, 3]).items():

        print(f'{k}: {v}')

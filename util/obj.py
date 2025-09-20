def executeFunctions(cls, function_names, parameters_list):
    if not function_names or not parameters_list:
        return []
    if cls.__name__ != function_names[0]:
        raise Exception("The first function name is not equal to the class name")

    obj = cls(*parameters_list[0])

    results = [None]

    for i in range(1, len(function_names)):
        method_name = function_names[i]
        args = parameters_list[i]
        method = getattr(obj, method_name)
        result = method(*args)
        results.append(result)

    return results

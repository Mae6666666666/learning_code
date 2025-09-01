import inspect


def print_var(var):
    frame = inspect.currentframe().f_back
    var_names = [name for name, val in frame.f_locals.items() if val is var]
    name = var_names[0] if var_names else "<?>"
    print(f"{name} = {var}")
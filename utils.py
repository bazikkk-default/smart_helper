def exist_method(class_inst, comment):
    methods = [func for func in dir(class_inst) if callable(getattr(class_inst, func)) and not func.startswith('_')]
    return comment in [getattr(class_inst, func).__doc__ for func in methods]


def get_method_by_comment(class_inst, comment):
    methods = [func for func in dir(class_inst) if callable(getattr(class_inst, func)) and not func.startswith('_')]
    return next(getattr(class_inst, func) for func in methods if getattr(class_inst, func).__doc__ == comment)

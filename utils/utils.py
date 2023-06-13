class Utils:
    @staticmethod
    def print_params(func):
        """
        Print function parameters
        """
        def wrapper(*args, **kwargs):
            print(f'{func.__name__:=^40}')
            print(f'Parameters: {args}, {kwargs}')
            res = func(*args, **kwargs)
            print(f'Result: {res}')
            print(f'-' * 40 + '\n')
            return res
        return wrapper
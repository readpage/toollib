"""
@author axiner
@version v1.0.0
@created 2021/12/14 20:28
@abstract
@description
@history
"""
import time
import traceback
from functools import wraps

_flwidth = 66
_flchar = "-"


class DecoratorUtils(object):

    @staticmethod
    def print_return(func):
        """
        print return
        :param func:
        :return:
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("func: '{0}', return: {1}\t@type: {2}".format(
                func.__name__, result, type(result)).center(_flwidth, _flchar))
            return result
        return wrapper

    @staticmethod
    def catch_exception(is_raise: bool = True):
        """
        catch exception
        :param is_raise:
        :return:
        """
        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwargs):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as ex:
                    if is_raise is True:
                        traceback.print_exc()
                    print("Error: {}".format(str(ex)))
            return inner
        return wrapper

    @staticmethod
    def timer(func):
        """
        timer
        :param func:
        :return:
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("func: '{0}', start.....".format(func.__name__).center(_flwidth, _flchar))
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print("func: '{0}' finished, spent time: {1:.2f}s".format(
                func.__name__, end_time - start_time).center(_flwidth, _flchar))
            return result
        return wrapper

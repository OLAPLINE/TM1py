import functools

from TM1py.Utils.Utils import verify_version


def skip_if_no_pandas(func):
    """ 
    Checks whether pandas is installed and skips the test if not
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        Wrap the wrapped function.

        Args:
            self: (todo): write your description
        """
        try:
            import pandas

            return func(self, *args, **kwargs)
        except:
            return self.skipTest(f"Test '{func.__name__}' requires pandas")

    return wrapper


def skip_if_insufficient_version(version):
    """ 
    Checks whether TM1 version is high enough and skips the test if not
    """

    def wrap(func):
        """
        Wrap the wrapped function as a decorator.

        Args:
            func: (callable): write your description
        """
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            """
            Decorator to ensure that the version is_version

            Args:
                self: (todo): write your description
            """
            if not verify_version(required_version=version, version=self.tm1.version):
                return self.skipTest(
                    f"Function '{ func.__name__, }' requires TM1 server version >= '{ version }'"
                )
            else:
                return func(self, *args, **kwargs)

        return wrapper

    return wrap

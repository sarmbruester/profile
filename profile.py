
"""
A profiling decorator pointed out by Sebastiaan Mathot in one of his videos: https://www.youtube.com/watch?v=8qEnExGLZfY
"""

import cProfile
import pstats
import io


def profile(fnc):
    """A decorator that uses cProfile to profile a function."""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

# A collection of useful functions
import time
import warnings
from functools import wraps
from itertools import chain, repeat
from typing import Any, Callable, List, Optional


def timeit(fn_identifier: Optional[str] = None) -> Callable:
    """Decorates a function such that its execution time is printed.
    Parameters
    ----------
    fn_identifier
        An optional string to print along with the execution time to make
        the association simpler between function and time. Defaults to
        the name of the decorated function.
    Returns
    -------
    Callable
        The decorated function that will track the execution time.
    """

    def decorator(func: Callable):
        # Default to the name of the function if no identifier is supplied
        fn_identifier = func.__name__ if fn_identifier is None else fn_identifier

        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()

            print(f"Elapsed time ({fn_identifier}): {end - start}")
            return result

        return inner

    return decorator


def ozip(list_to_zip: List[Any], groups: int, pad: bool = False) -> List[tuple]:
    """Zips adjacent elements of list ``list_to_zip`` into groupings of a given size.

    Parameters
    ----------
    list_to_zip
        The input list whose elements to group-wise zip.
    group
        The size of each group in the resulting zip.
    pad
        A flag whether to pad with ``None`` any ungrouped straggling
        elements of ``list_to_zip`` to form one final group. When left
        as `False`, then if ``len(list_to_zip) % groups != 0``,
        the remaining elements are omitted.

    Returns
    -------
    list[tuple]
        The resulting list of groupings as tuples.
    """
    pad_len = groups - len(list_to_zip) % groups

    if not pad and pad_len != 0:
        n_trim = groups - pad_len
        warnings.warn(
            f"This part of passed list will be shaved off: {list_to_zip[-1 * n_trim:]}"
        )

    # Pad with `None` if requested
    iterator = chain(list_to_zip, repeat(None, pad_len if pad else 0))
    return list(zip(*[iterator] * groups))

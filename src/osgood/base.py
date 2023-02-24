# A collection of useful functions
import warnings
import time
from itertools import repeat, chain
from typing import Any



































def ozip(list_to_zip: list[Any], groups: int, pad: bool = False) -> list[tuple]:
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
        the remaining elements are ommitted.

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

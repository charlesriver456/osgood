# A collection of useful functions
import warnings
from typing import Any


def ozip(list_to_zip: list[Any], groups: int) -> list[tuple]:
    """Zips adjacent elements of list ``list_to_zip`` into groupings of a given size.

    If len(list_to_zip) % groups != 0, the remaining elements are ommitted.
    If groups is larger than len(list_to_zip), then an empty list is returned.

    Parameters
    ----------
    list_to_zip
        The input list whose elements to group-wise zip.
    group
        The size of each group in the resulting zip.

    Returns
    -------
    list[tuple]
        The resulting list of groupings as tuples.
    """
    if len(list_to_zip) % groups != 0:
        remainder = len(list_to_zip) % groups
        warnings.warn(
            f"This part of passed list will be shaved off: {list_to_zip[-1 * remainder:]}"
        )

    return list(zip(*[iter(list_to_zip)] * groups))


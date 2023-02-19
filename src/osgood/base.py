# A collection of useful functions
import warnings
from typing import List, Tuple


def ozip(list_to_zip: list, groups: int) -> List[Tuple]:
    """Zips passed list [list_to_zip] into number of groups passed as a param
    If len(list_to_zip) % groups != 0, the remaining elements are ommitted.
    If groups is larger than len(list_to_zip), then an empty list is returned."""
    if groups > len(list_to_zip):
        warnings.warn(
            "Groups larger than length of list passed, empty list will be returned"
        )
        return list(zip(*[iter(list_to_zip)] * groups))
    if len(list_to_zip) % groups != 0:
        remainder = len(list_to_zip) % groups
        warnings.warn(
            f"This part of passed list will be shaved off: {str(list_to_zip[len(list_to_zip)-remainder:])}"
        )
        return list(zip(*[iter(list_to_zip)] * groups))
    else:
        list(zip(*[iter(list_to_zip)] * groups))

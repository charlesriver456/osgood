#A collection of useful functions
   



def ozip(list_to_zip: list, groups: int) -> list:
		return list(zip(*[iter(list_to_zip)] * groups))


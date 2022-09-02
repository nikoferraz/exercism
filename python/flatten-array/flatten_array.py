"""Functions for flattening a list."""


def flatten_recursively(iterable: list) -> list:
    """Yield a flattened list.
    :param iterable: list - a list of nested lists
    :yield: list - a flattened list
    """
    for item in iterable:
        if isinstance(item, list):
            yield from flatten_recursively(item)
        elif item is not None:
            yield item


def flatten(iterable: list) -> list:
    """Return a flattened list.
    :param iterable: list - a list of nested lists
    :return: list - a flattened list
    """
    return list(flatten_recursively(iterable))

import pyshorteners


def shorten_url(url : str) -> str:
    """_summary_ : This function shortens the url.

    Args:
        url (str): The url to be shortened.

    Returns:
        _type_: str
    """
    type_tiny = pyshorteners.Shortener()
    return str(type_tiny.tinyurl.short(url))
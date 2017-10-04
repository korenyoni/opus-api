class InvalidLangException(Exception):
    """
    Base invalid language exception
    """

    def __init__(self, lang):
        self.lang = lang.encode('utf-8')

    def __str__(self):
        return repr(self.lang)


class InvalidSrcException(InvalidLangException):
    """
    Raised when src is not in available langs
    """


class InvalidTrgException(InvalidLangException):
    """
    Raised when trg is not in available langs
    """

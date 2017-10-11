class InvalidLangException(Exception):
    """
    Base invalid language exception
    """

    def __init__(self, lang):
        self.lang = lang.encode('utf-8')

    def __str__(self):
        return repr(self.lang)

class InvalidFormException(Exception):
    """
    Raised when form is invalid
    """

    def __init__(self, form):
        self.form = form

    def __str__(self):
        return repr(self.form)

class InvalidSrcException(InvalidLangException):
    """
    Raised when src is not in available langs
    """


class InvalidTrgException(InvalidLangException):
    """
    Raised when trg is not in available langs
    """

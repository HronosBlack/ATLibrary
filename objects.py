class ATObject(object):
    """
    Класс обего представления объектв онлайн библиотеки Author.Today
    """
    
    _NAME_: str
    _URL_KEY_: str
    _URL_PREFIX_: str
    
    def __init__(self, name: str = "", key: str = "") -> None:
        self.Name = name
        self.UrlKey = key
        self.UrlPreix = ""
    
    @property
    def Name(self) -> str:
        return self._NAME_
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._NAME_ = value
    
    @property
    def UrlKey(self) -> str:
        return self._URL_KEY_
    
    @UrlKey.setter
    def UrlKey(self, value: str) -> None:
        self._URL_KEY_ = value
    
    @property
    def UrlPrefix(self) -> str:
        return self._URL_PREFIX_
    
    @UrlPrefix.setter
    def UrlPrefix(self, value: str) -> None:
        self._URL_PREFIX_ = value
    
    def __str__(self) -> str:
        return self.Name
    
    def __eq__(self, value: object) -> bool:
        if type(value) != 'ATObject':
            return False
        return ((self.Name == value.Name) and 
                (self.UrlKey == value.UrlKey) and
                (self.UrlPrefix == value.UrlPrefix))
    
    @property
    def UrlQuery(self) -> str:
        return f"{self.UrlPrefix}={self.UrlKey}"
    
    
class Author(ATObject):
    
    def __init__(self, name: str = "", key: str = "") -> None:
        super().__init__(name, key)
        self.UrlPrefix = "author"

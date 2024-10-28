class ATObject(object):
    """
    Класс общего представления объектов онлайн библиотеки Author.Today
    """
    
    _NAME_: str
    _URL_KEY_: str
    _URL_PREFIX_: str
    
    def __init__(self, name: str = "", key: str = "") -> None:
        """Инициализатор объекта класса

        Args:
            name (str, не обязателен): Наименование объекта. По умолчанию "".
            key (str, не обязателен): URL ключ объекта для запроса. По умолчанию "".
        """
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
        if type(value) != type(self):
            return False
        return ((self.Name == value.Name) and 
                (self.UrlKey == value.UrlKey) and
                (self.UrlPrefix == value.UrlPrefix))
    
    @property
    def UrlQuery(self) -> str:
        return f"{self.UrlPrefix}={self.UrlKey}"
    
    
class Author(ATObject):
    """
    Класс представления автора произведения оналйн библиотеки Author.Today
    """
    
    def __init__(self, name: str = "", key: str = "") -> None:
        super().__init__(name, key)
        self.UrlPrefix = "author"
        
    def __eq__(self, value: object) -> bool:
        if type(value) != type(self):
            return False
        return super().__eq__(value)
        
        
class Series(ATObject):
    """
    Класс представления серии произведений онлайн библиотеки AuthorToday
    """
    
    def __init__(self, name: str = "", key: str = "") -> None:
        super().__init__(name, key)
        self.UrlPrefix = "series"
        
    def __eq__(self, value: object) -> bool:
        if type(value) != type(self):
            return False
        return super().__eq__(value)


class Genre(ATObject):
    """
    Класс представления жанра произведения онлайн библиотеки Author.Today
    """
    
    _CHILDS_: list['Genre'] = None
    
    def __init__(self, name: str = "", key: str = "", childs: list['Genre'] = None) -> None:
        super().__init__(name, key)
        self.UrlPrefix = "genre"
        self.Childs = childs
    
    @property
    def Childs(self) -> list['Genre']:
        return self._CHILDS_
    
    @Childs.setter
    def Childs(self, value: list['Genre']) -> None:
        self._CHILDS_ = value
        
    def __eq__(self, value: object) -> bool:
        if type(value) != type(self):
            return False
        return super().__eq__(value) and (self.Childs == value.Childs)

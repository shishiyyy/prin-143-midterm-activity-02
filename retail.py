import py_serializable

@py_serializable.serializable_class
class Retail:
  def __init__(self, *, item: str, price: str, grams: str, quantity: str, stock: str) -> None:
    self._item = item
    self._price = price
    self._grams = grams
    self._quantity = quantity
    self._stock = stock

  @property
  def item(self) -> str:
    return self._item
  
  @property
  def price(self) -> str:
    return self._price
  
  @property
  def grams(self) -> str:
    return self._grams
  
  @property
  def quantity(self) -> str:
    return self._quantity
  
  @property
  def stock(self) -> str:
    return self._stock
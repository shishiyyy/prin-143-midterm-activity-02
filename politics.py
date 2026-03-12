import py_serializable

@py_serializable.serializable_class
class PoliticianProfile:
  def __init__(self, *, name: str, age: str, politicalParty: str, position: str, candidateNumber: str) -> None:
    self._name = name
    self._age = age
    self._politicalParty = politicalParty
    self._position = position
    self._candidateNumber = candidateNumber

  @property
  def name(self) -> str:
    return self._name
  
  @property
  def age(self) -> str:
    return self._age
  
  @property
  def politicalParty(self) -> str:
    return self._politicalParty
  
  @property
  def position(self) -> str:
    return self._position
  
  @property
  def candidateNumber(self) -> str:
    return self._candidateNumber
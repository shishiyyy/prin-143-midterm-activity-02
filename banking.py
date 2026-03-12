import py_serializable

@py_serializable.serializable_class
class Banking:
    def __init__(self, *, bankName: str, accountHolder: str, acoountNumber: str, balance: str, branchLocation: str) -> None:
        self._bankName = bankName
        self._accountHolder = accountHolder
        self._acoountNumber = acoountNumber
        self._balance = balance
        self._branchLocation = branchLocation

    @property
    def bankName(self) -> str:
        return self._bankName

    @property
    def accountHolder(self) -> str:
        return self._accountHolder

    @property
    def acoountNumber(self) -> str:
        return self._acoountNumber

    @property
    def balance(self) -> str:
        return self._balance

    @property
    def branchLocation(self) -> str:
        return self._branchLocation
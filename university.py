import py_serializable

@py_serializable.serializable_class
class university:

    def __init__(self, *, name: str, course: str, department: str, organization: str, loc: str):
        self._name = name
        self._course = course
        self._department = department
        self._organization = organization
        self._loc = loc

    @property
    def name(self) -> str:
        return self._name

    @property
    def course(self) -> str:
        return self._course

    @property
    def department(self) -> str:
        return self._department

    @property
    def organization(self) -> str:
        return self._organization

    @property
    def loc(self) -> str:
        return self._loc
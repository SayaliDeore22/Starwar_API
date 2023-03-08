from pydantic import BaseModel

class Foo(BaseModel):
    id: int
    name: float
data = {"id": 123, "name":5.6}
foo = Foo(**data)
print(foo)
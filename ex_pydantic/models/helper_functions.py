from pydantic import BaseModel, ConfigDict


def test_revalidate_instance_config():
    class Model1(BaseModel):
        a: int
        model_config = ConfigDict(revalidate_instance="always")

    m = Model1(a=10)
    m.a = "not an int"
    m = Model1.model_validate(m)

    class Model2(BaseModel):
        a: int

    m2 = Model2(a=10)
    m2.a = "not an int"
    m2 = Model2.model_validate(m2)

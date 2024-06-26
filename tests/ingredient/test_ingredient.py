from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo")
    ingredient2 = Ingredient("queijo")
    ingredient3 = Ingredient("carne")
    ingredient4 = Ingredient("bacon")
    ingredient5 = Ingredient("salada")

    assert ingredient1.__hash__() == ingredient2.__hash__()
    assert ingredient1.__hash__() != ingredient3.__hash__()
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
    assert ingredient1.__repr__() == "Ingredient('queijo')"
    assert ingredient1.name == "queijo"
    assert len(ingredient4.restrictions) > 0
    assert len(ingredient5.restrictions) == 0

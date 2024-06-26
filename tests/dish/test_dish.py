import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 2
def test_dish():
    parmegiana = Dish("parmegiana", 34.99)
    carne = Ingredient("carne")
    parmegiana.add_ingredient_dependency(carne, 2)
    parmegiana2 = Dish("parmegiana", 34.99)
    file_com_fritas = Dish("file com fritas", 29.99)

    assert parmegiana.name == "parmegiana"
    assert parmegiana.__hash__() == parmegiana2.__hash__()
    assert parmegiana.__hash__() != file_com_fritas.__hash__()
    assert parmegiana == parmegiana2
    assert parmegiana != file_com_fritas
    assert parmegiana.__repr__() == "Dish('parmegiana', R$34.99)"
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("polenta", "14.99")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("polenta", -14.99)
    assert len(parmegiana.recipe.values()) == 1
    assert len(parmegiana.get_restrictions()) == 2
    assert len(parmegiana.get_ingredients()) == 1

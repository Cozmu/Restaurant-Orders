from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest # mudar interpretador > python CTRL + SHIFT + P > python: select interpreter

def test_dish():
    with pytest.raises(TypeError):
        Dish('prato', 'invalid_price')

    with pytest.raises(ValueError):
        Dish('prato', -10.5)

    instance_ingredient_x = Dish('prato', 10.5)

    assert isinstance(instance_ingredient_x, Dish)
    assert instance_ingredient_x.name == 'prato'
    assert instance_ingredient_x.__repr__() == "Dish('prato', R$10.50)"
    assert instance_ingredient_x.__eq__(Dish('prato', 10.5)) == True
    assert instance_ingredient_x.__eq__(Dish('prato123', 5.5)) == False
    assert instance_ingredient_x.__hash__() != Dish('prato123', 5.5).__hash__()
    assert instance_ingredient_x.__hash__() == Dish('prato', 10.5).__hash__()

    instance_ingredient_x.add_ingredient_dependency(Ingredient('salmão'), 2.5)

    assert instance_ingredient_x.get_restrictions() == {Restriction.ANIMAL_MEAT, Restriction.SEAFOOD, Restriction.ANIMAL_DERIVED}
    assert instance_ingredient_x.get_ingredients() == {Ingredient('salmão')}



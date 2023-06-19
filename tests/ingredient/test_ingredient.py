from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501

def test_ingredient():
    instance_ingredient_x = Ingredient('farinha')

    assert isinstance(instance_ingredient_x, Ingredient)
    assert instance_ingredient_x.name == 'farinha'
    assert instance_ingredient_x.__repr__() == "Ingredient('farinha')"
    assert instance_ingredient_x.__eq__(Ingredient('farinha')) == True
    assert instance_ingredient_x.__eq__(Ingredient('ovo')) == False
    assert instance_ingredient_x.__hash__() != Ingredient('ovo').__hash__()
    assert instance_ingredient_x.__hash__() == Ingredient('farinha').__hash__()
    assert instance_ingredient_x.restrictions == {Restriction.GLUTEN}

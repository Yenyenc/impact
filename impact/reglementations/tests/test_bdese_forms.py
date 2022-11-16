from django import forms
import pytest

from reglementations.forms import bdese_form_factory
from reglementations.models import BDESE_300, BDESE_50_300


@pytest.fixture
def bdese_300(entreprise_factory):
    entreprise = entreprise_factory(effectif="grand")
    return BDESE_300.objects.create(entreprise=entreprise)


@pytest.fixture
def bdese_50_300(entreprise_factory):
    entreprise = entreprise_factory(effectif="moyen")
    return BDESE_50_300.objects.create(entreprise=entreprise)


def test_bdese_form_step_1_with_new_bdese_300_instance(bdese_300):
    categories_professionnelles = ["catégorie 1", "catégorie 2", "catégorie 3"]
    form = bdese_form_factory(1, categories_professionnelles, bdese_300)

    assert form.instance == bdese_300
    assert len(form.fields) == 102
    assert "annee" not in form.fields
    assert "entreprise" not in form.fields
    assert "effectif_total" in form.fields
    assert "evolution_amortissement" not in form.fields

    for field in [
        field for field in form.fields if field in bdese_300.category_fields()
    ]:
        assert isinstance(form.fields[field], forms.MultiValueField)

    for field in form.fields:
        if field == "unite_absenteisme":
            assert form[field].value() == "J"
        else:
            assert not form[field].value()

    bound_form = bdese_form_factory(
        1, categories_professionnelles, bdese_300, data={"unite_absenteisme": "J"}
    )

    assert bound_form.is_valid()


def test_fields_of_complete_step_are_disabled(bdese_300):
    bdese_300.mark_step_as_complete(1)

    categories_professionnelles = ["catégorie 1", "catégorie 2", "catégorie 3"]
    form = bdese_form_factory(1, categories_professionnelles, bdese_300)

    for field in form.fields:
        assert form.fields[field].disabled


def test_form_is_initialized_with_fetched_data(bdese_300):
    categories_professionnelles = ["catégorie 1", "catégorie 2", "catégorie 3"]
    form = bdese_form_factory(3, categories_professionnelles, bdese_300)

    assert not form["nombre_femmes_plus_hautes_remunerations"].value()

    fetched_data = {"nombre_femmes_plus_hautes_remunerations": 10}
    form = bdese_form_factory(
        3, categories_professionnelles, bdese_300, fetched_data=fetched_data
    )

    assert form["nombre_femmes_plus_hautes_remunerations"].value() == 10


def test_bdese_form_with_new_bdese_50_300_instance(bdese_50_300):
    categories_professionnelles = ["catégorie 1", "catégorie 2", "catégorie 3"]
    form = bdese_form_factory(1, categories_professionnelles, bdese_50_300)

    assert form.instance == bdese_50_300
    assert len(form.fields) == 85
    assert "annee" not in form.fields
    assert "entreprise" not in form.fields
    assert "effectif_mensuel" in form.fields

    for field in [
        field for field in form.fields if field in bdese_50_300.category_fields()
    ]:
        assert isinstance(form.fields[field], forms.MultiValueField)

    for field in form.fields:
        assert not form[field].value()

    bound_form = bdese_form_factory(
        1, categories_professionnelles, bdese_50_300, data={}
    )

    assert bound_form.is_valid()
import pytest

from api.tests.fixtures import mock_api_recherche_entreprise
from entreprises.models import Entreprise
from entreprises.tests.conftest import unqualified_entreprise
from habilitations.models import add_entreprise_to_user
from reglementations.views import BDESEReglementation
from reglementations.views import IndexEgaproReglementation


def test_public_reglementations(client):
    response = client.get("/reglementations")

    assert response.status_code == 200

    content = response.content.decode("utf-8")
    assert "<!-- page reglementations -->" in content
    assert "BDESE" in content
    assert "Index de l’égalité professionnelle" in content

    context = response.context
    assert context["entreprise"] is None
    assert context["reglementations"][0]["info"] == BDESEReglementation.info()
    assert context["reglementations"][0]["status"] is None
    assert context["reglementations"][1]["info"] == IndexEgaproReglementation.info()
    assert context["reglementations"][1]["status"] is None


@pytest.mark.parametrize("status_is_soumis", [True, False])
@pytest.mark.django_db
def test_public_reglementations_with_entreprise_data(status_is_soumis, client, mocker):
    data = {
        "effectif": "petit",
        "bdese_accord": False,
        "raison_sociale": "Entreprise SAS",
        "siren": "000000001",
    }

    mocker.patch(
        "reglementations.views.ReglementationStatus.is_soumis",
        return_value=status_is_soumis,
        new_callable=mocker.PropertyMock,
    )
    response = client.get("/reglementations", data=data)

    content = response.content.decode("utf-8")
    assert "Entreprise SAS" in content

    # entreprise has been created
    entreprise = Entreprise.objects.get(siren="000000001")
    assert entreprise.raison_sociale == "Entreprise SAS"
    assert not entreprise.bdese_accord
    assert entreprise.effectif == "petit"

    # reglementations for this entreprise are anonymously displayed
    context = response.context
    assert context["entreprise"] == entreprise
    reglementations = context["reglementations"]
    assert reglementations[0]["status"] == BDESEReglementation.calculate_status(
        entreprise, 2022
    )
    assert reglementations[1]["status"] == IndexEgaproReglementation.calculate_status(
        entreprise, 2022
    )

    if status_is_soumis:
        assert '<p class="fr-badge">soumis</p>' in content
        anonymous_status_detail = "Vous êtes soumis à cette réglementation. Connectez-vous pour en savoir plus."
        assert anonymous_status_detail in content
    else:
        assert '<p class="fr-badge">non soumis</p>' in content
        anonymous_status_detail = "Vous n'êtes pas soumis à cette réglementation."
        assert anonymous_status_detail in content


@pytest.fixture
def entreprise(db, alice):
    entreprise = Entreprise.objects.create(
        siren="000000001",
        effectif="petit",
        bdese_accord=False,
        raison_sociale="Entreprise SAS",
    )
    add_entreprise_to_user(entreprise, alice, "Présidente")
    return entreprise


def test_reglementations_with_authenticated_user(client, entreprise):
    client.force_login(entreprise.users.first())

    response = client.get("/reglementations")

    assert response.status_code == 200

    context = response.context
    assert context["entreprise"] is None
    assert context["reglementations"][0]["status"] is None
    assert context["reglementations"][1]["status"] is None


@pytest.mark.parametrize("status_is_soumis", [True, False])
def test_reglementations_with_authenticated_user_and_another_entreprise_data(
    status_is_soumis, client, entreprise, mocker
):
    """
    Ce cas est encore accessible mais ne correspond pas à un parcours utilisateur normal
    """
    client.force_login(entreprise.users.first())

    data = {
        "effectif": "grand",
        "bdese_accord": False,
        "raison_sociale": "Une autre entreprise SAS",
        "siren": "000000002",
    }

    mocker.patch(
        "reglementations.views.ReglementationStatus.is_soumis",
        return_value=status_is_soumis,
        new_callable=mocker.PropertyMock,
    )
    response = client.get("/reglementations", data=data)

    content = response.content.decode("utf-8")
    assert "Une autre entreprise SAS" in content

    reglementations = response.context["reglementations"]
    for reglementation in reglementations:
        assert not reglementation["status"].status_detail in content
    if status_is_soumis:
        assert '<p class="fr-badge">soumis</p>' in content
        anonymous_status_detail = "L'entreprise est soumise à cette réglementation."
        assert anonymous_status_detail in content
    else:
        assert '<p class="fr-badge">non soumis</p>' in content
        anonymous_status_detail = (
            "L'entreprise n'est pas soumise à cette réglementation."
        )
        assert anonymous_status_detail in content


def test_entreprise_data_are_saved_only_when_entreprise_user_is_autenticated(
    client, entreprise
):
    """
    Ce cas est encore accessible mais ne correspond pas à un parcours utilisateur normal
    """
    data = {
        "effectif": "grand",
        "bdese_accord": False,
        "raison_sociale": "Entreprise SAS",
        "siren": "000000001",
    }

    client.get("/reglementations", data=data)

    entreprise = Entreprise.objects.get(siren="000000001")
    assert entreprise.effectif == "petit"

    client.force_login(entreprise.users.first())
    client.get("/reglementations", data=data)

    entreprise = Entreprise.objects.get(siren="000000001")
    assert entreprise.effectif == "grand"


def test_reglementation_with_authenticated_user(client, entreprise):
    client.force_login(entreprise.users.first())

    response = client.get(f"/reglementation/{entreprise.siren}")

    assert response.status_code == 200

    content = response.content.decode("utf-8")
    context = response.context
    assert context["entreprise"] == entreprise
    reglementations = context["reglementations"]
    assert reglementations[0]["status"] == BDESEReglementation.calculate_status(
        entreprise, 2022
    )
    assert reglementations[1]["status"] == IndexEgaproReglementation.calculate_status(
        entreprise, 2022
    )
    for reglementation in reglementations:
        assert reglementation["status"].status_detail in content


def test_reglementation_with_authenticated_user_and_multiple_entreprises(
    client, entreprise_factory, alice
):
    entreprise1 = entreprise_factory(siren="000000001")
    entreprise2 = entreprise_factory(siren="000000002")
    entreprise1.users.add(alice)
    entreprise2.users.add(alice)
    client.force_login(alice)

    response = client.get(f"/reglementation/{entreprise1.siren}")

    assert response.status_code == 200

    content = response.content.decode("utf-8")
    context = response.context
    assert context["entreprise"] == entreprise1
    reglementations = context["reglementations"]
    assert reglementations[0]["status"] == BDESEReglementation.calculate_status(
        entreprise1, 2022
    )
    assert reglementations[1]["status"] == IndexEgaproReglementation.calculate_status(
        entreprise1, 2022
    )
    for reglementation in reglementations:
        assert reglementation["status"].status_detail in content

    response = client.get(f"/reglementation/{entreprise2.siren}")

    assert response.status_code == 200

    content = response.content.decode("utf-8")
    context = response.context
    assert context["entreprise"] == entreprise2
    reglementations = context["reglementations"]
    assert reglementations[0]["status"] == BDESEReglementation.calculate_status(
        entreprise1, 2022
    )
    assert reglementations[1]["status"] == IndexEgaproReglementation.calculate_status(
        entreprise1, 2022
    )
    for reglementation in reglementations:
        assert reglementation["status"].status_detail in content


def test_reglementation_with_unqualified_entreprise_redirect_to_qualification_page(
    client, alice, unqualified_entreprise, mock_api_recherche_entreprise
):
    add_entreprise_to_user(unqualified_entreprise, alice, "Présidente")
    client.force_login(alice)

    response = client.get(
        f"/reglementation/{unqualified_entreprise.siren}", follow=True
    )

    assert response.status_code == 200
    url = f"/entreprises/{unqualified_entreprise.siren}"
    assert response.redirect_chain == [(url, 302)]

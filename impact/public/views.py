import time

import requests
from django.conf import settings
from django.shortcuts import render

from .forms import EligibiliteForm, SirenForm
from entreprises.models import Entreprise


def index(request):
    return render(request, "public/index.html", {"form": SirenForm()})


def siren(request):
    form = SirenForm(request.GET)
    errors = []
    if form.is_valid():
        siren = form.cleaned_data["siren"]
        # documentation api recherche d'entreprises 1.0.0 https://api.gouv.fr/documentation/api-recherche-entreprises
        url = f"https://recherche-entreprises.api.gouv.fr/search?q={siren}&page=1&per_page=1"
        response = requests.get(url)
        if response.status_code == 200 and response.json()["total_results"]:
            data = response.json()["results"][0]
            raison_sociale = data["nom_raison_sociale"]
            try:
                # les tranches d'effectif correspondent à celles de l'API Sirene de l'Insee
                # https://www.sirene.fr/sirene/public/variable/tefen
                tranche_effectif = int(data["tranche_effectif_salarie"])
            except ValueError:
                tranche_effectif = 0
            if tranche_effectif < 21:  # moins de 50 salariés
                taille = "petit"
            elif tranche_effectif < 32:  # moins de 250 salariés
                taille = "moyen"
            elif tranche_effectif < 41:  # moins de 500 salariés
                taille = "grand"
            else:
                taille = "sup500"
            form = EligibiliteForm(
                initial={
                    "siren": siren,
                    "effectif": taille,
                    "raison_sociale": raison_sociale,
                }
            )
            return render(
                request,
                "public/siren.html",
                {
                    "raison_sociale": raison_sociale,
                    "form": form,
                },
            )
        else:
            errors = (
                "L'entreprise n'a pas été trouvée. Vérifiez que le SIREN est correct."
            )
    else:
        errors = form.errors

    return render(request, "public/index.html", {"form": form, "errors": errors})

import requests
import os

# API_URL = os.environ.get("ENSEMBLE_API_URL")
API_URL = "https://rest.ensembl.org/xrefs/symbol"


class EnsemblAPI:
    def __init__(self) -> None:
        self.API_URL = os.getenv("ENSEMBLE_API_URL")

    @staticmethod
    def getEnsembleId(specie, target) -> None:
        result = requests.get(
            API_URL + f"/{specie}/{target}?content-type=application/json"
        )
        return result.json()

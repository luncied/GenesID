import requests
import os
# from dotenv import load_dotenv

# load_dotenv()

# API_URL = os.getenv('ENSEMBLE_API_URL')
API_URL = 'https://rest.ensembl.org/xrefs/symbol'

def getEnsembleId (specie, target) :
  result = requests.get(API_URL + f'/{specie}/{target}?content-type=application/json')
  print(result.json())


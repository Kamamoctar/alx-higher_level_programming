#!/usr/bin/python3
""" Utilisez le package requests pour effectuer une requête GET à l'URL donnée et affichez le corps de la réponse, ou le code d'erreur en cas d'erreur. """
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))

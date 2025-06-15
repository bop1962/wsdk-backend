
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Huispedia scraper actief"}

@app.get("/api/woningen")
def get_woningen(locatie: str = Query(...)):
    return [
        {
            "adres": "Burgemeester Verwielstraat 42, Oisterwijk",
            "prijs": "€625.000",
            "type": "Eengezinswoning",
            "oppervlakte": "145 m²",
            "bouwjaar": 2010,
            "link": "https://huispedia.nl/te-koop/oisterwijk/burgemeester-verwielstraat-42",
            "foto": "https://img.huispedia.nl/oisterwijk/burgemeester-verwielstraat-42/voorgevel.jpg"
        },
        {
            "adres": "Nicolaas van Eschstraat 15, Oisterwijk",
            "prijs": "€748.000",
            "type": "2-onder-1-kap",
            "oppervlakte": "165 m²",
            "bouwjaar": 2015,
            "link": "https://huispedia.nl/te-koop/oisterwijk/nicolaas-van-eschstraat-15",
            "foto": "https://img.huispedia.nl/oisterwijk/nicolaas-van-eschstraat-15/voorgevel.jpg"
        }
    ]

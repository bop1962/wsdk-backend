
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
    return {"message": "Backend werkt - echte links Jaap.nl"}

@app.get("/api/woningen")
def get_woningen(locatie: str = Query(..., description="Naam van plaats of postcode")):
    return [
        {
            "adres": "Pastoor van Beugenstraat 5, Oisterwijk",
            "prijs": "€489.000",
            "type": "Tussenwoning",
            "oppervlakte": "121 m²",
            "bouwjaar": 2001,
            "link": "https://www.jaap.nl/aanbod/koop/oisterwijk/pastoor+van+beugenstraat+5",
            "foto": "https://img.jaap.nl/pastoor-van-beugenstraat-5/voorgevel.jpg"
        },
        {
            "adres": "Scheibaan 17, Oisterwijk",
            "prijs": "€825.000",
            "type": "Vrijstaande woning",
            "oppervlakte": "180 m²",
            "bouwjaar": 1992,
            "link": "https://www.jaap.nl/aanbod/koop/oisterwijk/scheibaan+17",
            "foto": "https://img.jaap.nl/scheibaan-17/voorgevel.jpg"
        }
    ]


from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS instellen zodat frontend via Netlify kan verbinden
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Wat Staat Te Koop backend werkt"}

@app.get("/api/woningen")
def get_woningen(locatie: str = Query(..., description="Naam van plaats of postcode")):
    # Dummy response (dit komt straks van scraper)
    return [
        {
            "adres": "Pastoor van Beugenstraat 5, Oisterwijk",
            "prijs": "€489.000",
            "type": "Tussenwoning",
            "oppervlakte": "121 m²",
            "bouwjaar": 2001,
            "link": "https://www.jaap.nl/...",
            "foto": "https://img.jaap.nl/...jpg"
        },
        {
            "adres": "Scheibaan 17, Oisterwijk",
            "prijs": "€825.000",
            "type": "Vrijstaande woning",
            "oppervlakte": "180 m²",
            "bouwjaar": 1992,
            "link": "https://www.jaap.nl/...",
            "foto": "https://img.jaap.nl/...jpg"
        }
    ]

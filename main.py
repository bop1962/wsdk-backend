from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/huizen/oisterwijk")
def huizen_oisterwijk():
    dummy_data = [
        {
            "adres": "Posthoornseweg 12",
            "prijs": "€ 645.000",
            "type": "Vrijstaande woning"
        },
        {
            "adres": "Scheibaan 17",
            "prijs": "€ 289.000",
            "type": "Recreatiewoning"
        },
        {
            "adres": "Peperstraat 8",
            "prijs": "€ 419.000",
            "type": "Tussenwoning"
        }
    ]
    return JSONResponse(content=dummy_data)
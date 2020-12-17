from fastapi import FastAPI, HTTPException
import db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
 "https://docs-ui.herokuapp.com/"
]
app.add_middleware(
CORSMiddleware, 
allow_origins=origins,
allow_credentials=True, 
allow_methods=["*"], 
allow_headers=["*"],
)

@app.get("/documentos/")
async def obtener_docs():
    doc = db.obtenet_docs()
    return doc

@app.post("/documentos/nuevo/")
async def crear_doc(doc: db.Documento):
    ok = db.crear_docs(doc)
    if ok:
        return {'mensaje':'Documento creado'}
    else:
        raise HTTPException(status_code=400, detail="Documento existente")

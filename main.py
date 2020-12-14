from fastapi import FastAPI, HTTPException
import db

app = FastAPI()

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
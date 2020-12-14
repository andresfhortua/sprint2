from fastapi import FastAPI, HTTPException
import db

api = FastAPI()

@api.get("/documentos/")
async def obtener_docs():
    doc = db.obtenet_docs()
    return doc

@api.post("/documentos/nuevo/")
async def crear_doc(doc: db.Documento):
    ok = db.crear_docs(doc)
    if ok:
        return {'mensaje':'Documento creado'}
    else:
        raise HTTPException(status_code=400, detail="Documento existente")

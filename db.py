from pydantic import BaseModel

class Documento(BaseModel):
    id_documento: int
    nombre:str
    id_dependencia: int
    prioridad: int
    fecha_venc: str    

documentos = {
    1: Documento(id_documento=1, nombre="cotizacion_1", id_dependencia=2, prioridad= 1, fecha_venc="10-10-2020"),
    2: Documento(id_documento=2, nombre="cuenta_cobro_1", id_dependencia=2, prioridad= 2, fecha_venc="25-11-2020"),
    3: Documento(id_documento=3, nombre="citacion_1", id_dependencia=1, prioridad= 3, fecha_venc="15-12-2020")
}

def obtenet_docs():
    lista_docs = []
    for d in documentos:
        lista_docs.append(documentos[d])
    return lista_docs

def crear_docs(doc: Documento):
    if doc.id_documento in documentos:
        return False
    else:
        documentos[doc.id_documento]=doc
        return True
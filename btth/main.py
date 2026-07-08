from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session
from typing import List
from database import Base, engine, get_db
from schemas import DocumentCreate, DocumentResponse
import services

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/documents", response_model=List[DocumentResponse], status_code=status.HTTP_200_OK)
def show_all_documents(db: Session = Depends(get_db)):
    return services.get_all_documents(db)


@app.post("/documents", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
def add_new_document(new_document: DocumentCreate, db: Session = Depends(get_db)):
    return services.add_document(db=db, new_document=new_document)


@app.delete("/documents/{document_id}", response_model=DocumentResponse, status_code=status.HTTP_200_OK)
def remove_document(document_id: int, db: Session = Depends(get_db)):
    return services.delete_document(db=db, document_id=document_id)
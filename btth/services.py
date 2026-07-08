from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas import DocumentCreate
from models import DocumentModel


def get_all_documents(db: Session):
    return db.query(DocumentModel).all()


def add_document(db: Session, new_document: DocumentCreate):
    new_doc = DocumentModel(
        title=new_document.title,
        subject=new_document.subject,
        document_type=new_document.document_type,
        file_url=new_document.file_url
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc


def delete_document(db: Session, document_id: int):
    doc = db.query(DocumentModel).filter(DocumentModel.id == document_id).first()

    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Không tìm thấy tài liệu với id = {document_id}"
        )

    db.delete(doc)
    db.commit()
    return doc
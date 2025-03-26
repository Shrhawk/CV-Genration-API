import os
from datetime import datetime
from typing import Any

from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse

from app.models.schemas import CVData
from app.services.cv_generator import CVGenerator
from app.services.storage import StorageService


router = APIRouter(prefix="/api", tags=["cv"])

# Initialize services
cv_generator = CVGenerator()
storage_service = StorageService()

async def generate_cv_background_task(
    cv_id: str, cv_data: dict[str, Any]
)-> dict[str, Any]:
    """
    Background task to generate CV.

    Args:
        cv_id (str): The unique identifier for the CV.
        cv_data (dict[str, Any]): The CV data to generate.

    Returns:
        dict[str, Any]: A dictionary containing the status and file path.
    """
    try:
        # Update status to processing
        storage_service.update_cv_status(cv_id, "processing")

        # Generate PDF
        pdf_content = cv_generator.generate_pdf(cv_data)

        # Save PDF
        file_path = cv_generator.save_pdf(cv_id, pdf_content)

        # Update storage with file path
        storage_service.set_cv_path(cv_id, file_path)

        # Update status to completed
        storage_service.update_cv_status(cv_id, "completed")

        return {"status": "success", "file_path": file_path}

    except Exception as e:
        # Update status to failed
        storage_service.update_cv_status(cv_id, "failed")
        raise e

@router.post("/generate-cv/")
async def generate_cv(
    cv_data: CVData, background_tasks: BackgroundTasks
)-> dict[str, Any]:
    """
    Generate a new CV asynchronously.

    Args:
        cv_data (CVData): The CV data to generate.
        background_tasks (BackgroundTasks): FastAPI background tasks handler.

    Returns:
        dict[str, Any]: A dictionary containing the CV ID and status.
    """
    try:
        # Generate a unique ID for this CV
        cv_id = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{
        cv_data.full_name.lower().replace(' ', '_')}"

        # Start background task for CV generation
        background_tasks.add_task(
            generate_cv_background_task,
            cv_id=cv_id,
            cv_data=cv_data.dict()
        )

        return {
            "status": "processing",
            "cv_id": cv_id,
            "message": "CV generation started"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/cv-status/{cv_id}")
async def get_cv_status(cv_id: str) -> dict[str, Any]:
    """
    Get the status of a CV generation.

    Args:
        cv_id (str): The unique identifier for the CV.

    Returns:
        dict[str, Any]: A dictionary containing the CV status.
    """
    try:
        status = storage_service.get_cv_status(cv_id)
        return {"status": status}
    except Exception:
        raise HTTPException(status_code=404, detail="CV not found")

@router.get("/download-cv/{cv_id}")
async def download_cv(cv_id: str) -> FileResponse:
    """
    Download a generated CV.

    Args:
        cv_id (str): The unique identifier for the CV.

    Returns:
        FileResponse: The CV file as a downloadable response.
    """
    try:
        file_path = storage_service.get_cv_path(cv_id)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="CV not found")
        return FileResponse(
            file_path,
            media_type="application/pdf",
            filename=f"cv_{cv_id}.pdf"
        )
    except Exception:
        raise HTTPException(status_code=404, detail="CV not found")

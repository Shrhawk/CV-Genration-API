import os

import redis

from app.core.config import get_settings


class StorageService:
    def __init__(self):
        settings = get_settings()
        self.redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port=int(settings.REDIS_PORT),
            db=0
        )
        self.output_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'output')
        os.makedirs(self.output_dir, exist_ok=True)

    def get_cv_path(self, cv_id: str) -> str:
        """
        Get the file path for a CV.

        Args:
            cv_id (str): The unique identifier for the CV.

        Returns:
            str: The complete file path for the CV PDF.
        """
        return os.path.join(self.output_dir, f"cv_{cv_id}.pdf")

    def get_cv_status(self, cv_id: str) -> str:
        """
        Get the status of a CV generation.

        Args:
            cv_id (str): The unique identifier for the CV.

        Returns:
            str: The current status of the CV generation.
        """
        status = self.redis_client.get(f"cv_status_{cv_id}")
        return status.decode('utf-8') if status else "not_found"

    def update_cv_status(self, cv_id: str, status: str) -> None:
        """
        Update the status of a CV generation.

        Args:
            cv_id (str): The unique identifier for the CV.
            status (str): The new status to set.

        Returns:
            None
        """
        self.redis_client.set(f"cv_status_{cv_id}", status)

    def set_cv_path(self, cv_id: str, file_path: str) -> None:
        """
        Store the file path for a CV.

        Args:
            cv_id (str): The unique identifier for the CV.
            file_path (str): The path where the CV is stored.

        Returns:
            None
        """
        self.redis_client.set(f"cv_path_{cv_id}", file_path)

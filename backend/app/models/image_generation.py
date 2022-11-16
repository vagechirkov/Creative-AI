from typing import Optional, List
from pydantic import BaseModel
import uuid


class Image(BaseModel):
    url: str


class GeneratedImagesResponse(BaseModel):
    requestId: str
    images: List[Image]
    celery_task_id: Optional[str]


class GenerateImagesRequest(BaseModel):
    requestId: str = str(uuid.uuid4())
    prompt: str
    vector: Optional[List[float]]
    guidance_scale: Optional[float]
    inference_steps: Optional[int]
    num_images: Optional[int]
    seed: Optional[int]

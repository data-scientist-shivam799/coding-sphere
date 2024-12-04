from fastapi import APIRouter, Depends
from app.models import Project
from app.utils import require_role

router = APIRouter()

@router.get("/projects")
def get_projects():
    """
    Get all projects.
    
    Returns:
        list[Project]: A list of all projects.
    """
    return list(Project.objects())

@router.post("/projects", dependencies=[Depends(require_role("admin"))])
def create_project(name: str, description: str):
    """
    Create a new project.
    
    Args:
        name (str): The name of the project.
        description (str): A description of the project.
    
    Returns:
        dict: A dictionary containing a success message and the id of the created project.
    """
    project = Project(name=name, description=description)
    project.save()
    return {"message": "Project created", "id": str(project.id)}

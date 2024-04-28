# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Criar tabelas no banco de dados, se ainda não existirem
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas para CRUD de tarefas
@app.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    if tasks is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks

@app.post("/tasks/")
def create_task(task: models.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: models.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

@app.get("/status/")
def read_all_status(db: Session = Depends(get_db)):
    status = db.query(models.Status).all()
    return status

@app.post("/status/")
def create_status(status: models.StatusCreate, db: Session = Depends(get_db)):
    db_status = models.Status(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

@app.get("/status/{status_id}")
def read_status(status_id: int, db: Session = Depends(get_db)):
    status = db.query(models.Status).filter(models.Status.status_id == status_id).first()
    if status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return status


@app.put("/status/{status_id}")
def update_status(status_id: int, status: models.StatusUpdate, db: Session = Depends(get_db)):
    db_status = db.query(models.Status).filter(models.Status.status_id == status_id).first()
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    for key, value in status.dict().items():
        setattr(db_status, key, value)
    db.commit()
    db.refresh(db_status)
    return db_status

@app.delete("/status/{status_id}")
def delete_status(status_id: int, db: Session = Depends(get_db)):
    status = db.query(models.Status).filter(models.Status.status_id == status_id).first()
    if status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    db.delete(status)
    db.commit()
    return {"message": "Status deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

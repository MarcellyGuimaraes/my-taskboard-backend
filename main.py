# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Criar tabelas no banco de dados, se ainda não existirem
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
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


@app.get("/icones/")
def read_icones(db: Session = Depends(get_db)):
    icones = db.query(models.Icone).all()
    return icones

@app.post("/icones/")
def create_icone(icone: models.IconeCreate, db: Session = Depends(get_db)):
    db_icone = models.Icone(**icone.dict())
    db.add(db_icone)
    db.commit()
    db.refresh(db_icone)
    return db_icone

@app.get("/icones/{icone_id}")
def read_icone(icone_id: int, db: Session = Depends(get_db)):
    icone = db.query(models.Icone).filter(models.Icone.icone_id == icone_id).first()
    if icone is None:
        raise HTTPException(status_code=404, detail="Icone not found")
    return icone

@app.put("/icones/{icone_id}")
def update_icone(icone_id: int, icone: models.IconeUpdate, db: Session = Depends(get_db)):
    db_icone = db.query(models.Icone).filter(models.Icone.icone_id == icone_id).first()
    if db_icone is None:
        raise HTTPException(status_code=404, detail="Icone not found")
    for key, value in icone.dict().items():
        setattr(db_icone, key, value)
    db.commit()
    db.refresh(db_icone)
    return db_icone

@app.delete("/icones/{icone_id}")
def delete_icone(icone_id: int, db: Session = Depends(get_db)):
    icone = db.query(models.Icone).filter(models.Icone.icone_id == icone_id).first()
    if icone is None:
        raise HTTPException(status_code=404, detail="Icone not found")
    db.delete(icone)
    db.commit()
    return {"message": "Icone deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

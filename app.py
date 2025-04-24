from fastapi import FastAPI, Depends
from sqlmodel import Session,select
from database import get_db

from models.tasks import Tasks
app = FastAPI()


@app.get("/")
def get_hello():
    return {"message": "welcome api tasks"}   
    
@app.get("/task")
def get_tasks(db: Session = Depends(get_db)):
    statement = select(Tasks)
    results = db.exec(statement)
    return {"data": results.all()}

@app.post("/task")
def create_task(task: Tasks, db: Session = Depends(get_db)):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task











"""

@app.get("/")
def root():
    return {"message": "Hello World"}

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/task")
def get_posts(db: Session = Depends(get_db)):
    posts = db.(Task).all()
    return {"data": posts}
    
@app.get("/task")
def get_tasks(db: Session = Depends(get_db)):
    statement = select(Task)
    results = db.exec(statement)
    return {"data": results.all()}

@app.get("/task/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
   #print(id)  
   posts = db.query(Task).all()
   return {"post": id} 

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
"""
from sqlalchemy import create_engine, text
import os

db_connection_string= os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl" : {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs=[]
  
  for r in result.all():
    jobs.append(r._mapping)

  return jobs

def load_job_from_db(id):
  val=id
  with engine.connect() as conn:
    # result = conn.execute(
    #   text("SELECT * FROM jobs WHERE id = :val"),
    #   val=id
    # )
    # rows = result.all()
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = {val}"),
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])

def add_application_to_db(job_id, data):
  
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    query= query.bindparams(job_id=job_id,
                           full_name=data['full_name'],
                           email=data['email'],
                           linkedin_url=data['linkedin_url'],
                           education=data['education'],
                           work_experience=data['work_experience'],
                           resume_url=data['resume_url']
                        )

    conn.execute(query)
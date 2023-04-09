from sqlalchemy import select
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import logging
from .ai_processing import process_ai_input
import os
from dotenv import load_dotenv
import uuid
import hashlib
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.config import DATABASE_URL, database
from app.models import Submission, Base
import datetime
import pytz


app = FastAPI()
logging.basicConfig(level=logging.INFO)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
#submit_endpoint = f"/submit/{str(uuid.uuid4())}"

# 发送日历请求
submit_endpoint = f"/api/report"
ai_summaries = []

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """index page"""
    db = Session(engine)
    # 从数据库中查询最新摘要数据
    web_summaries = db.query(Submission.output).all()
    web_summaries = [summary[0] for summary in web_summaries] if web_summaries else []
    logging.info(f"summaries: {web_summaries}")
    return templates.TemplateResponse("index.html", {"request": request, "submit_endpoint": submit_endpoint, "web_summaries": web_summaries})

@app.post(submit_endpoint)
async def submit(request: Request):
    """submit a summary and get an AI summary in return"""
    global ai_summaries
    data = await request.json()
    summary = data.get('summary')
    logging.info(f"Summary: {summary}")
    ai_summary = process_ai_input(summary)
    # ai_summary = "This is a test summary 2" 
    # 保存到内存中
    ai_summaries = list(set(ai_summaries))
    ai_summaries.append(ai_summary) 
    # 保存到数据库
    content_hash = hashlib.sha256(summary.encode()).hexdigest() # 生成一个hash
    # 生成一个北京时间，只有年月日，保存到数据库中
    date = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d")
    submission = Submission(id=str(uuid.uuid4()), content_hash=content_hash, input=summary, output=ai_summary, date = date) # 生成一个新的id
    logging.info(f"submission: {submission}")


    # 检查是否有重复的
    async with database:
        db = Session(engine)
        existing_submission = db.execute(select(Submission).where(Submission.content_hash == submission.content_hash)).scalar()
        if existing_submission:
            # 如果存在，则更新现有记录而不是添加新记录
            existing_submission.input = submission.input
            existing_submission.output = submission.output
        else:
            db.add(submission)
        db.commit()
        db.close()

    # 返回结果
    logging.info(f"AI Summary: {ai_summary}")

    logging.info(f"AI Summaries: {ai_summaries}")
    return JSONResponse(content={"ai_summary": ai_summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

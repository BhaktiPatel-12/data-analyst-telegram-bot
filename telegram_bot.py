import os
import json

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
Application,
MessageHandler,
filters,
ContextTypes
)

from agent import analyze_question
from logger import save_log


from dotenv import load_dotenv
import os

load_dotenv(".env")

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

print("TOKEN:", TOKEN)

LOG_URL=os.getenv(
"LOG_URL"
)



async def handle(
    update:Update,
    context:ContextTypes.DEFAULT_TYPE
):

    question=update.message.text


    answer=analyze_question(
        question
    )


    save_log(
        question,
        answer
    )


    response={
        "answer":answer,
        "log_url":LOG_URL
    }


    await update.message.reply_text(
        json.dumps(response)
    )



def start():

    app=Application.builder().token(
        TOKEN
    ).build()


    app.add_handler(
        MessageHandler(
            filters.TEXT,
            handle
        )
    )


    print(
        "Bot running..."
    )


    app.run_polling()



if __name__=="__main__":
    start()
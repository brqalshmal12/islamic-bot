import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = " "  # <-- الصق التوكن هنا بين القوس8826066609:AAG1gUhUywDub7jmnkzC9PaotfsJJH63EZQ

ayat = ["﴿ أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ ﴾","﴿ إِنَّ مَعَ الْعُسْرِ يُسْرًا ﴾"]
azkar = ["سبحان الله","أستغفر الله"]

async def start(u,c):
    await u.message.reply_text("بوت إسلامي شغال ❤️\n/aya\n/zekr")

async def aya(u,c):
    await u.message.reply_text(random.choice(ayat))

async def zekr(u,c):
    await u.message.reply_text(random.choice(azkar))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("aya", aya))
app.add_handler(CommandHandler("zekr", zekr))
app.run_polling()

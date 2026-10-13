import os,random
from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes

ayat=["﴿ أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ ﴾","﴿ إِنَّ مَعَ الْعُسْرِ يُسْرًا ﴾","﴿ لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا ﴾"]
azkar=["سبحان الله وبحمده","أستغفر الله","اللهم صل على محمد"]

async def start(u,c):
    await u.message.reply_text("أهلاً بك في البوت الإسلامي ❤️\n/aya - آية\n/zekr - ذكر")
async def aya(u,c):
    await u.message.reply_text(random.choice(ayat))
async def zekr(u,c):
    await u.message.reply_text(random.choice(azkar))

if __name__=='__main__':
    TOKEN=os.environ.get("BOT_TOKEN")
    app=ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("aya",aya))
    app.add_handler(CommandHandler("zekr",zekr))
    app.run_polling()

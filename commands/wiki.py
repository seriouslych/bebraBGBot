import wikipedia

def wiki_message(bot, message, log):
    wiki_msg = message.text.split(maxsplit=1)[1]
    
    wikipedia.set_lang("ru")
    
    try:
        wk = wikipedia.page(wiki_msg)
        
        content = wikipedia.summary(wiki_msg, sentences=4)
        
        bot.reply_to(message, f"{wk.title}\n\n{content}\n\n[Источник]({wk.url})", parse_mode='Markdown')
        
        log.info(f"[@{message.from_user.username}] - WIKI - Отправлена статья")
    except Exception as e:
        log.exception("Не найдена страница")
        bot.reply_to(message, "Статья не найдена :(")
cmd = input("Enter Command : ")
video_url = input("Enter Video URL : ")
caption = input("Enter Caption : ")

f = open("main.py", "a")

f.write("""
@bot.message_handler(commands=['Medium_Term_Staking_Updated'])
def send_medium_term_staking_updated(message, content_types=['video']):
    video = open('Medium Term Staking Updated.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video,supports_streaming=True,timeout=10000)
""")

exec(open("main.py").read())

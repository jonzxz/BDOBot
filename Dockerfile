FROM gorialis/discord.py

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV DISCORD_TOKEN=$DISCORD_TOKEN
ENV PRAW_CLIENT_ID=$PRAW_CLIENT_ID
ENV PRAW_CLIENT_SECRET=$PRAW_CLIENT_SECRET
ENV TZ=Asia/Singapore

COPY . .

CMD ["python", "main.py"]

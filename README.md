# How to start the project?

## Add environment variables

Create file `.env`. Next, paste it in `.env` and add your bot token

```dotenv
BOT_TOKEN=<your_bot_token>
```

## Setup with docker compose

```bash
git clone https://github.com/LaGGgggg/yp_business_card_tg_bot
cd yp_business_card_tg_bot
docker compose up -d --build
```

## Setup with docker

```bash
git clone https://github.com/LaGGgggg/yp_business_card_tg_bot
cd yp_business_card_tg_bot
docker build . -t tg-bot
docker run --detach -it -p 8080:8080 tg-bot
```

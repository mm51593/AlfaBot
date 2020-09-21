from settings import Settings
from bot import Bot

def main():
    settings = Settings()
    Alfa = Bot(settings)
    Alfa.start()
    return

main()

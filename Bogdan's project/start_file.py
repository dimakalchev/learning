import time
from price_monitoring import Monitoring


with Monitoring() as bot:
    bot.land_first_page()
    bot.filtres()
    bot.take_data()
    bot.check_sale()






time.sleep(100)
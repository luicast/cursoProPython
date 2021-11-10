from datetime import datetime
import pytz

bogotaTimezone = pytz.timezone('America/Bogota')
bogotaDate = datetime.now(bogotaTimezone)
print('bogota: ', bogotaDate.strftime('%d/%m/%y, %H:%M:%S'))

mexicoTimezone = pytz.timezone('America/Mexico_City')
mexicoDate = datetime.now(mexicoTimezone)
print('ciudad de mexico: ', mexicoDate.strftime('%d/%m/%y, %H:%M:%S'))

caracasTimezone = pytz.timezone('America/Caracas')
caracasDate = datetime.now(caracasTimezone)
print('caracas: ', caracasDate.strftime('%d/%m/%y, %H:%M:%S'))
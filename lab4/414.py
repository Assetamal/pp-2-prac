from datetime import datetime, timezone, timedelta
import re

def parse_datetime(date_str):
    # Формат: YYYY-MM-DD UTC±HH:MM
    m = re.match(r'(\d{4}-\d{2}-\d{2}) UTC([+-]\d{2}):(\d{2})', date_str)
    if not m:
        raise ValueError("Invalid format")
    
    date_part, tz_hour, tz_min = m.groups()
    dt = datetime.strptime(date_part, "%Y-%m-%d")  # локальная полуночь
    tz_offset = int(tz_hour)*60 + int(tz_min)
    tzinfo = timezone(timedelta(minutes=tz_offset))
    dt = dt.replace(tzinfo=tzinfo)
    return dt.astimezone(timezone.utc)  # переводим в UTC

# Чтение дат
dt1 = parse_datetime(input())
dt2 = parse_datetime(input())

# Разница в днях
delta = abs((dt1 - dt2).total_seconds())
days = int(delta // 86400)  # полные дни
print(days)
import time
from datetime import datetime

import requests.exceptions
from requests_tor import RequestsTor


def get(url: str, headers: dict[str, str]) -> dict[str, any]:
    rt = RequestsTor(tor_ports=(9050,), tor_cport=9051, autochange_id=1)
    try:
        init_time = time.time()
        r = rt.get(url, headers=headers)
        end_time = time.time()

        date = r.headers.get("Date")
        if date:
            date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT")

    except requests.exceptions.ConnectionError:
        return {
            "url": url,
            "status": None,
            "date": int(datetime.now().timestamp() * 1000),
            "elapsed": time.time() - init_time,
            "size": None,
            "header_date": None,
            "header_elapsed": None,
        }

    else:
        return {
            "url": url,
            "status": r.status_code,
            "date": int(datetime.now().timestamp() * 1000),
            "elapsed": end_time - init_time,
            "size": len(r.content),
            "header_date": date,
            "header_elapsed": r.elapsed.total_seconds(),
        }

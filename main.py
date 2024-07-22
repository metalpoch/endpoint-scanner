import concurrent.futures
import sys

from lib import credentials, fetch, utils
from lib.analytics import Analytics

url = credentials.URL
headers = credentials.HEADERS


def main() -> None:
    count = 0
    results = []
    autopage, qty, max_workers = utils.input_validate(sys.argv)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        if autopage:
            futures = [
                executor.submit(fetch.get, f"{url}={n%10}", headers) for n in range(qty)
            ]
        else:
            futures = [
                executor.submit(fetch.get, f"{url}=1", headers) for _ in range(qty)
            ]
        for future in concurrent.futures.as_completed(futures):
            print(f"\rproccess: {round((count*100)/qty, 2)}%   ", end="")
            results.append(future.result())
            count += 1
    print()
    subtitle = f"{qty} requests {"with" if autopage else "without"} pagination and {max_workers} max workers"

    analytic = Analytics(results)
    analytic.to_csv(title=subtitle)
    analytic.chart(title="Response Behavior", subtitle=subtitle)


if __name__ == "__main__":
    main()

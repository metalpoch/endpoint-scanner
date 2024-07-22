# endpoint-scanner

## Installation

#### Clone this repository [GitHub](https://github.com/metalpoch/Traffic-Access-Dashboard#) and create a virtual environment

```bash
git clone https://github.com/metalpoch/endpoint-scanner
cd endpoint-scanner/
python -m venv .venv
source .venv/bin/activate
```

## Dependencies

#### Use [pip](https://pip.pypa.io/en/stable/) to install the modules in the file requirements.txt

```bash
pip install -r requirements.txt
```

#### Create a credentials.py into the dir lib

This Python script must contain the following variables

```python
URL = "https//some-endpoint-to-scan.some"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
```

#### Download and start Tor Browser or install Tor

Notes:
In Tor torrc file control port is disabled by default. Needs to uncomment line ControlPort 9051
If you face an error Authentication failed: unable to read '/run/tor/control.authcookie' ([Errno 13] Permission denied: '/run/tor/control.authcookie') - needs to add your current user to the tor group. ps ax o comm,group | grep tor - command to find tor group (group name will be in the second column, for example debian-tor). sudo usermod -a -G debian-tor $USER - add your current user to tor group
Restart Tor (/etc/init.d/tor restart) and re-login

## Use

It is required to pass `<auto-pagination|no-auto-pagination>`, `<querys: int>` and `<MaxWorkers: int>` as arguments, in that same order.

#### Consult single endpoint

```bash
python no-auto-pagination 1000 100  ## 1000 querys with 10 workers
```

#### If you want to add a page depending on the query number

make sure the endpoint ends with the '=' of the query. Example https://some-endpoint.some?page=

```bash
python auto-pagination 1000 100 ## 1000 querys with 10 workers
```

# MLC Forecast

## Forecast for MLC price

### Download and active enviroment

Config virtualenv:

```bash
$ git clone https://github.com/eadomenech/mlcForecast.git
```

```bash
$ cd mlcForecast/
```

```bash
$ python3 -m venv env
```

```bash
$ source env/bin/activate
```

### Install requirements:

```bash
$ pip install -r requirements.txt
```

### Create and update dataset:

Init dataset (run once)
```bash
$ python scrape/start.py
```

Update dataset (run once)
```bash
$ python scrape/update.py
```


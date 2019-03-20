# Quickstarter AWS Environment

This is being developed using Zappa and Flask for API.

### Quickstart

Example of config file: `environ.rc`

```
export DEBUG=1
export DYNAMODB_ENDPOINT=http://localhost:8000
export VALID_DOMAIN=bbva.com
```

Then run:

For local development we assume Dynamodb on local or AWS configured correctly.

```
. environ.rc
python api.py
```

### Deployment

```
zappa deploy dev
```

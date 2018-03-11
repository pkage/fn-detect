# to get started:

```
$ git clone https://github.com/quadnix/fn-detect
$ virtualenv env_fndetect -p python3
$ source env_fndetect/bin/activate
$ make install-deps-venv
```

get twitter api keys and make a file `twitter_config.json` containing:

```json
{
	"consumer_key": "xxxxx",
	"consumer_secret: "xxxxx",
	"access_token_key": "xxxxx",
	"access_token_secret": "xxxxx"
}
```

and get mashape api keys as well, placing them into `mashape.json`:

```json
{
	"mashape": "xxxxx"
}
```

Finally:

```
$ make run
```

to run the web client

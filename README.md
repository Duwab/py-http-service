# Python service management over http

Goal : In a compose CI stack, being able to

```bash
user@test-container:~$ curl -XPOST http://remote-container:8080/services/rabbitmq?action=stop
```

## Requirements

* python 2
* `pip install Flask`

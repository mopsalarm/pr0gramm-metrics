pr0gramm metrics
================

You need to set `DATADOG_API_KEY` to your datadog api key.

Run this using docker:
```sh

docker pull mopsalarm/pr0gramm-metrics:latest
docker run -d --restart=unless-stopped -e DATADOG_API_KEY=yourkey mopsalarm/pr0gramm-metrics
```

#!/usr/bin/env python3
import random
import time
from contextlib import contextmanager

import datadog
import requests

print("Initializing datadog")
datadog.initialize()

print("Starting datadog stats")
stats = datadog.ThreadStats()
stats.start()


def metric_name(name):
    return "ext.pr0gramm.request." + name


@contextmanager
def measure(name, tags=None):
    try:
        with stats.timer(metric_name(name + ".time"), tags=tags):
            yield
            return True

    except KeyboardInterrupt:
        raise

    except Exception as err:
        print("Got error during request '{}': {}".format(name, err))
        stats.increment(metric_name(name + ".error"), tags=tags)


def measure_feed_performance():
    # ensure that we get a request that is not cached
    item_id = random.randint(0, 1000000)
    url = "http://pr0gramm.com/api/items/get"
    params = {"older": item_id, "flags": 15}

    with measure("feed", tags=["cache:miss"]):
        success = requests.get(url, params, timeout=10).content

    if success:
        with measure("feed", tags=["cache:hit"]):
            # noinspection PyStatementEffect
            requests.get(url, params, timeout=10).content


def main():
    while True:
        # noinspection PyBroadException
        try:
            measure_feed_performance()
        except KeyboardInterrupt:
            raise
        except Exception:
            pass

        time.sleep(60)


if __name__ == '__main__':
    main()

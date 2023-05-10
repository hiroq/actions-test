from datadog import initialize, statsd
import time

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

statsd.increment('example_metric.increment', tags=["environment:dev"])
time.sleep(1)
statsd.increment('example_metric.increment', tags=["environment:dev"])

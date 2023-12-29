# Monitoring
In order to monitor our system we used [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/).

## Prometheus
Prometheus enables the collection and storage of time-series data. This capability facilitates real-time monitoring and the triggering of alerts when predefined thresholds are met. 

In our case, it has been locally installed and run through the command
    ```
    prometheus --config.file=prometheus.yml
    ``` \
This command starts the Prometheus server, collecting essential metrics needed for Grafana visualization.

![prometheus](https://github.com/se4ai2324-uniba/GHIPrediction/assets/48125720/dd620f34-8b4b-4d0c-9f9a-cb493ffebb7d)

## Grafana
In combination with Prometheus for a more comprehensive visualization of data generated (also using [Locust](https://locust.io/)), we use [Grafana](https://grafana.com/), which is locally installed. 
Grafana allows us to customize and explore the metrics dashboards to gain insights into the performance of our application.

![grafana](https://github.com/se4ai2324-uniba/GHIPrediction/assets/48125720/b3606fd2-508c-479d-b715-f1c88840abec)

In this dashboard, we show some of the metrics that Grafana can handle, such as: 	
* Response size	    -> to get the dimensions in bytes of every request
* Request duration	-> to show how the duration of the requests changes over time also depending on the number of requests
* Scrape duration   -> to show how the scrape duration changes over time also depending on the number of requests
* Total requests	-> Total number of requests over time (in combination with scrape and request duration)

 This combination of Prometheus and Grafana provides a valid monitoring and visualization solution, contributing to the overall efficiency and performance analysis of our system.

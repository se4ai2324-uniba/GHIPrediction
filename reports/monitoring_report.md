# Monitoring
To monitor our system we used [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/), and [Better Up Time](https://betterstack.com/uptime).

## Prometheus
Prometheus enables the collection and storage of time-series data. This capability facilitates real-time monitoring and the triggering of alerts when predefined thresholds are met. 

In our case, it has been locally installed and run through the command
    ```
    prometheus --config.file=prometheus.yml
    ``` \
This command starts the Prometheus server, collecting essential metrics needed for Grafana visualization.

![prometheus](https://github.com/se4ai2324-uniba/GHIPrediction/assets/48125720/dd620f34-8b4b-4d0c-9f9a-cb493ffebb7d)

## Grafana
In combination with Prometheus for a more comprehensive visualization of data generated (also using [Locust](https://locust.io/)), we use Grafana, which is locally installed. 
Grafana allows us to customize and explore the metrics dashboards to gain insights into the performance of our application.

![grafana](https://github.com/se4ai2324-uniba/GHIPrediction/assets/48125720/b3606fd2-508c-479d-b715-f1c88840abec)

In this dashboard, we show some of the metrics that Grafana can handle, such as: 	
* Response size	    -> to get the dimensions in bytes of every request;
* Request duration	-> to show how the duration of the requests changes over time also depending on the number of requests;
* Scrape duration   -> to show how the scrape duration changes over time also depending on the number of requests;
* Total requests	-> total number of requests over time (in combination with scrape and request duration);

 ## Better Up Time
 In addition to Prometheus and Grafana, we also use a third-party service that allows us to ensure the continuous availability and performance monitoring of our application, Better Up Time.
 In particular, we monitor if the address of our system goes down:
 
![betteruptime](https://github.com/se4ai2324-uniba/GHIPrediction/assets/48125720/9880b2c3-8b98-4d63-bf74-3ccd481b8936)

 This combination of Prometheus, Grafana, and Better Up Time provides a valid monitoring and visualization solution, contributing to the overall efficiency and performance analysis of our system.

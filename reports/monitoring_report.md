# Monitoring
To monitor our system we used [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/), [Better Up Time](https://betterstack.com/uptime), and [Alibi](https://docs.seldon.io/projects/alibi-detect/en/latest/).

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

## Alibi
With Alibi we can have under control also the data drift, checking, whenever it is necessary, if the data on which the model predicts, provokes a drift.
In particular, we have defined a GitHub action that replicates every step of our pipeline, and then it runs the Alibi module. This allows the user to check whether some drifting is present in the data or not. The user can check the output of the Alibi module directly in the terminal of the GitHub action itself which can be triggered only manually.

![alibi](https://github.com/se4ai2324-uniba/GHIPrediction/assets/48125720/a773d7f9-892d-4377-834d-b5d917680c65)


 This combination of Prometheus, Grafana, Better Up Time, and Alibi provides a valid monitoring and visualization solution, contributing to the overall efficiency and performance analysis of our system.

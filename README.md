# Load Test

## About the project

This project was developed as a final work for the Performance Evaluation Modeling discipline at University of Fortaleza, as a way to get to know and gain practical experience in the use of a benchmark widely known in the market.

That way we were asked to do some load tests with four framework among 12 listed on this article:https://k6.io/blog/comparing-best-open-source-load-testing-tools/. As a target service of the load tests, we choosed *httpbin service*, available at https://httpbin.org/ (online) and https://github.com/postmanlabs/httpbin (source code). 

The frameworks that we used was: 
1. Apachebench 
2. Vegeta
3. Locust
4. Artillery

> Observation: To run, you have to install `Docker` and `Docker Compose`.

## Usage  

At first, it was defined 2 types of workload levels (numbers of concurrent users) to be submitted to the target service by each load generation tool. 

Numbers of concurrent users: 10 and 100 users 

After that, the performance of the target system was monitored with Prometheus, then Prometheus was integrated with Grafana, in order to allow the visualization, in real time, of the httpbin metrics being collected by Prometheus during the load tests.

## Usage 

In order to replicated what was done you have to: 
1. Download httpbin code 
2. Change 
3. Clone this project with:  
```
git clone 
```
4. To run, use the command below: 
```
docker-compose up --build
```

After that, you can access these services:

Grafana: http://localhost:3000
Prometheus: http://localhost:9090
HttpBin: http://localhost:8080
Statsd: http://localhost:9102/metrics
NodeExporter: http://localhost:9110
cAdvisor: http://localhost:8090



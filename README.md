Algs API

# Summary
A python service with api endpoints for both naive and "clever" solutions to various common computer science algorithm questions. 

# Instructions

## Starting
* Run docker
* in _deployments_ folder run `docker-compose up --build`
* if you don't want to view the output logs, run with `-d` to "detach" 

## Stopping
* `docker-compose down`

## Responses
Here's an example endpoint.
You can change between `/gcd/clever?` and `/gcd/naive?` to notice the difference in compute time for two approaches. 

`http://localhost:5000/gcd/clever?a=555555&b=43224245`
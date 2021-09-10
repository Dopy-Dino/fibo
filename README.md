# Fibo Simple Server

## Run the web server without Docker Container

To run web server without Docker Container, we need `python 3` and `pip3` as prerequisites.

After you got the prerequisites available on the system, create python virtualenv :

```
pip3 install virtualenv
virtualenv /path/to/fibo-env
source /path/to/fibo-env/bin/activate
```

Then install required packages :

```
cd /path/to/fibo/
pip install -Ur requirements.txt
```

Run the wsgi server using this gunicorn command :

```
gunicorn --bind 0.0.0.0:5000 wsgi:app --access-logfile -
```

Access the local web server using `curl -i "localhost:5000/fib?n=10"

## Run the web server using Docker Container locally

Use these instructions to run web server using Docker Container locally

```
cd /path/to/fibo/
docker build -t fibo .
docker run -p 8080:8080 fibo
```

Access the local web server using `curl -i "localhost:8080/fib?n=10"

note that you can change the tag above to e.g `fibo:v1` or add your docker hub path like `robeevanjava/fibo:1`

## Run the web server using Kubernetes Locally

As prerequisites for this, is to have either minikube or another local development kubernetes application like kind, k3s, rancher etc.
Presuming you already have tools like minikube started locally, simply run this manifest : 

```
kubectl apply -f k8s.yaml -n default
kubectl port-forward service/fibo-svc 8080:8080
```

Access the local web server using `curl -i "localhost:8080/fib?n=10" 




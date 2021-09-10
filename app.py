from flask import Flask, request

app = Flask(__name__)

@app.route("/fib")
def fiboPage():
    if request.args.get('n'):
        n = request.args.get('n')
        fiboResult = fibonacci(n)
        return '%s\n' % (str(fiboResult))
    else:
        return 'where is the n?', 404

def fibonacci(n):
    try:
        n = int(n)
        if n <= 0:
            return 0
        elif n >= 1 and n <= 100000:
            fib = [0, 1]
            for x in range(2, n+1):
                fib.append(fib[x-1] + fib[x-2])
            return fib[-1]
        else:
            return 'value n better under 100000'
    except ValueError:
        return 'value can not be converted to integer'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
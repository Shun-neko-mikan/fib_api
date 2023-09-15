from flask import Flask,request , jsonify

app = Flask(__name__)

@app.route('/fib')
def fib():
    try:
        n = int(request.args.get('n'))
        if n > 20000:
            message = jsonify({'status': 413, 'message': 'ValueError: n must be less than 20000.'})
            return message, 413
        elif n < 1:
            message = jsonify({'status': 400, 'message': 'ValueError: n must be positive.'})
            return message, 400
        return jsonify({'result': fibonacci(n)})
    except ValueError:
        message = jsonify({'status': 400, 'message': 'ValueError: n must be a natural number.'})
        return message, 400
    


def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


if __name__ == '__main__':
    app.run()
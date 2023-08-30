from flask import Flask,request , jsonify

app = Flask(__name__)

@app.route('/fib')
def fib():
    try:
        n = int(request.args.get('n'))
        return jsonify({'result': fibonacci(n)})
    except Exception as e:
        message = jsonify({'status': 400, 'message': 'Bad Request.'})
        return message, 400
    


def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


if __name__ == '__main__':
    app.run()
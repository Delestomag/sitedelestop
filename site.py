from flask import Flask, render_template_string

# Инициализация Flask-приложения
app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delesto P3rexodn1k</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom right, #4e3b79, #6a2b8a);
            color: white;
            text-align: center;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            overflow: hidden;
            position: relative;
        }

        .snowflake {
            position: absolute;
            top: -10px;
            z-index: 10;
            pointer-events: none;
            font-size: 24px;
            color: rgba(255, 255, 255, 0.8);
            user-select: none;
            animation: snow 10s linear infinite;
        }

        @keyframes snow {
            to {
                transform: translateY(100vh);
            }
        }

        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 15px;
            max-width: 400px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            position: relative;
            z-index: 1;
        }

        h1 {
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
            position: relative;
            z-index: 2;
            overflow: hidden;
        }

        .santa-hat {
            position: absolute;
            top: -20px;
            left: 0;
            width: 25px;
            height: 20px;
            background: url('https://img.icons8.com/ios/452/santa-claus-hat.png') no-repeat center center;
            background-size: cover;
            z-index: 3;
        }

        p {
            font-size: 14px;
            margin-bottom: 20px;
            text-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
        }

        .button {
            display: block;
            width: 100%;
            margin: 10px 0;
            padding: 12px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-size: 14px;
            transition: background-color 0.3s, transform 0.1s, box-shadow 0.3s;
            box-shadow: 0 0 15px rgba(0, 123, 255, 0.9);
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
            transform: translateX(-5px);
        }

        .button:hover {
            box-shadow: 0 0 25px rgba(0, 123, 255, 1);
        }

        .button:active {
            transform: scale(0.95);
            background: #28a745;
            box-shadow: 0 0 25px rgba(40, 167, 69, 1);
        }
    </style>
    <script>
        function createSnowflakes() {
            for (let i = 0; i < 20; i++) {
                let snowflake = document.createElement('div');
                snowflake.textContent = '❄';
                snowflake.classList.add('snowflake');
                snowflake.style.left = `${Math.random() * 100}%`;
                snowflake.style.animationDuration = `${Math.random() * 5 + 5}s`;
                snowflake.style.animationDelay = `${Math.random() * 5}s`;
                document.body.appendChild(snowflake);
            }
        }

        window.onload = createSnowflakes;
    </script>
</head>
<body>
    <div class="container">
        <h1>
            <span>delesto</span>
            <span class="santa-hat"></span>
            <span> p3rexodn1k</span>
        </h1>
        <p>используйте кнопки ниже для перехода туда, куда вам нужно</p>
        <a href="https://t.me/fakefakefakefakp" class="button">channel</a>
        <a href="https://t.me/B_i_o_Delesto" class="button">BIO</a>
        <a href="https://t.me/DeepNet_robot" class="button">BOT</a>
        <a href="https://t.me/delesto" class="button">Account</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
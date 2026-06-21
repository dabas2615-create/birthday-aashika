html = """
<!DOCTYPE html>
<html>
<head>
    <title>Happy Birthday Aashika</title>

    <style>

        body{
            margin:0;
            background:linear-gradient(to right,#ff9a9e,#fad0c4);
            text-align:center;
            font-family:Arial, sans-serif;
            overflow:hidden;
        }

        h1{
            color:white;
            font-size:55px;
            margin-top:30px;
            animation:glow 2s infinite alternate;
        }

        @keyframes glow{
            from{
                text-shadow:0 0 10px white;
            }
            to{
                text-shadow:0 0 30px yellow;
            }
        }

        img{
            width:250px;
            border-radius:20px;
            box-shadow:0 0 20px white;
            margin-top:20px;
        }

        p{
            font-size:24px;
            color:white;
            width:80%;
            margin:auto;
            margin-top:20px;
            line-height:1.6;
        }

        .heart{
            position:absolute;
            color:red;
            font-size:30px;
            animation:float 6s linear infinite;
        }

        @keyframes float{
            from{
                transform:translateY(100vh);
            }
            to{
                transform:translateY(-100px);
            }
        }

    </style>

</head>

<body>

    <h1>🎉 Happy Birthday Aashika 🎉</h1>

    <img src="aashika.jpg" alt="Aashika">

    <p>
        Dear Aashika ❤️ <br><br>

        Wishing you a birthday filled with happiness,
        love, laughter and beautiful memories. 🌸 <br><br>

        May all your dreams come true and may your life
        always be full of success and joy. ✨ <br><br>

        You are truly special and deserve all the happiness
        in the world. 💖
    </p>

    <div class="heart" style="left:10%;">❤️</div>
    <div class="heart" style="left:20%; animation-delay:1s;">❤️</div>
    <div class="heart" style="left:30%; animation-delay:2s;">❤️</div>
    <div class="heart" style="left:40%; animation-delay:3s;">❤️</div>
    <div class="heart" style="left:50%; animation-delay:4s;">❤️</div>
    <div class="heart" style="left:60%; animation-delay:2s;">❤️</div>
    <div class="heart" style="left:70%; animation-delay:1s;">❤️</div>
    <div class="heart" style="left:80%; animation-delay:3s;">❤️</div>
    <div class="heart" style="left:90%; animation-delay:4s;">❤️</div>

</body>
</html>
"""

with open("birthday.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Birthday Website Created Successfully!")
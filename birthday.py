<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Happy Birthday Aashika</title>

<style>

body{
    margin:0;
    background:linear-gradient(to right,#ff9a9e,#fad0c4);
    text-align:center;
    font-family:Arial,sans-serif;
    overflow-x:hidden;
}

h1{
    color:white;
    font-size:50px;
    margin-top:20px;
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

.photos{
    display:flex;
    justify-content:center;
    gap:20px;
    flex-wrap:wrap;
    margin-top:20px;
}

.photos img{
    width:250px;
    border-radius:20px;
    box-shadow:0 0 20px white;
}

p{
    font-size:24px;
    color:white;
    width:85%;
    margin:auto;
    margin-top:30px;
    line-height:1.7;
}

#cakeBtn{
    margin-top:30px;
    padding:15px 30px;
    border:none;
    border-radius:30px;
    font-size:20px;
    cursor:pointer;
    background:white;
    color:#ff4d6d;
    font-weight:bold;
    box-shadow:0 0 15px white;
}

#cakeBox{
    display:none;
    margin-top:30px;
}

#cake{
    font-size:150px;
}

.cut{
    animation:cutCake 3s forwards;
}

@keyframes cutCake{
    0%{
        transform:scale(1);
    }
    50%{
        transform:scale(1.3) rotate(-5deg);
    }
    100%{
        transform:scale(0.8);
        opacity:0.6;
    }
}

.heart{
    position:fixed;
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

#message{
    display:none;
    color:white;
    font-size:30px;
    margin-top:20px;
    font-weight:bold;
}

.confetti{
    position:fixed;
    font-size:25px;
    animation:fall 4s linear forwards;
}

@keyframes fall{
    from{
        transform:translateY(-100px);
    }
    to{
        transform:translateY(100vh);
    }
}

</style>
</head>

<body>

<h1>🎉 Happy Birthday Aashika 🎉</h1>

<div class="photos">
    <img src="1000410295.jpg" alt="">
    <img src="1000410286.jpg" alt="">
</div>

<p>
Dear Aashika ❤️ <br><br>

Wishing you a birthday filled with happiness,
love, laughter and beautiful memories. 🌸 <br><br>

May all your dreams come true and may your life
always be full of success and joy. ✨ <br><br>

You are truly special and deserve all the happiness
in the world. 💖
</p>

<button id="cakeBtn" onclick="showCake()">
🎂 Click Here For Surprise 🎂
</button>

<div id="cakeBox">
    <div id="cake">🎂</div>
    <h2 style="color:white;">Make A Wish ✨</h2>
</div>

<div id="message">
🎉 Cake Cut Successfully 🎉<br>
Happy Birthday Aashika ❤️
</div>

<div class="heart" style="left:10%">❤️</div>
<div class="heart" style="left:20%;animation-delay:1s">❤️</div>
<div class="heart" style="left:30%;animation-delay:2s">❤️</div>
<div class="heart" style="left:40%;animation-delay:3s">❤️</div>
<div class="heart" style="left:50%;animation-delay:4s">❤️</div>
<div class="heart" style="left:60%;animation-delay:2s">❤️</div>
<div class="heart" style="left:70%;animation-delay:1s">❤️</div>
<div class="heart" style="left:80%;animation-delay:3s">❤️</div>
<div class="heart" style="left:90%;animation-delay:4s">❤️</div>

<script>

function showCake(){

    document.getElementById("cakeBox").style.display="block";

    let cake=document.getElementById("cake");

    cake.classList.add("cut");

    createConfetti();

    setTimeout(function(){

        cake.innerHTML="🍰";

        document.getElementById("message").style.display="block";

    },3000);
}

function createConfetti(){

    for(let i=0;i<40;i++){

        let confetti=document.createElement("div");

        confetti.innerHTML="🎉";

        confetti.classList.add("confetti");

        confetti.style.left=Math.random()*100+"%";

        confetti.style.animationDuration=
        (Math.random()*3+2)+"s";

        document.body.appendChild(confetti);

        setTimeout(()=>{
            confetti.remove();
        },5000);
    }
}

</script>

</body>
</html>
           

var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");

// загрузка изображений
var wolf = new Image();
var egg = new Image();


wolf.src = "images/wolf.png";
bomb.src = "images/bomb.png";
egg.src = "images/egg.png";
fake_egg.src = "images/fake_egg.png";
grass.src = "images/grass.png";
tree.src = "images/tree.png";

// начальные значения координат волка
var wolfX = cvs.width / 2 - 30;
var wolfY = cvs.height - 150;

// начальные значения скорости падения яиц
var eggSpeed = 2;
var fakeEggSpeed = 3;
var bombSpeed = 4;

// начальный счет игрока
var score = 0;

// массив яиц и фейковых яиц
var eggs = [];
var fakeEggs = [];
var bombs = [];

// функция отрисовки волка
function drawWolf() {
  ctx.drawImage(wolf, wolfX, wolfY);
}

// функция отрисовки яиц
function drawEggs() {
  for (var i = 0; i < eggs.length; i++) {
    ctx.drawImage(egg, eggs[i].x, eggs[i].y, 50, 50);
  }
}

// функция отрисовки фейковых яиц
function drawFakeEggs() {
  for (var i = 0; i < fakeEggs.length; i++) {
    ctx.drawImage(fake_egg, fakeEggs[i].x, fakeEggs[i].y, 50, 50);
  }
}

// функция отрисовки бомб
function drawBombs() {
  for (var i = 0; i < bombs.length; i++) {
    ctx.drawImage(bomb, bombs[i].x, bombs[i].y, 50, 50);
  }
}

// функция отрисовки счета игрока
function drawScore() {
  ctx.font = "20px Arial";
  ctx.fillStyle = "black";
  ctx.fillText("Score: " + score, 20, 30);
}

// функция проверки столкновения волка и объектов
function checkCollision(obj) {
  if (wolfX + 50 >= obj.x && wolfX <= obj.x + 50 &&
      wolfY + 50 >= obj.y && wolfY <= obj.y + 50) {
    if (obj.type === "egg") {
      score += 1;
    } else if (obj.type === "fake_egg") {
      score -= 5;
    } else if (obj.type === "bomb") {
      score -= 10;
    }
    return true;
  }
  return false;
}

// функция обновления игры
function update() {
  // очистка экрана
  ctx.clearRect(0, 0, cvs.width, cvs.height);

  // обновление координат фейковых яиц и проверка столкновения
for (var i = 0; i < fakeEggs.length; i++) {
    fakeEggs[i].y += fakeEggSpeed;
    if (checkCollision(fakeEggs[i])) {
        fakeEggs.splice(i, 1);
    }
}
    
    // обновление координат бомб и проверка столкновения
for (var i = 0; i < bombs.length; i++) {
    bombs[i].y += bombSpeed;
    if (checkCollision(bombs[i])) {
        bombs.splice(i, 1);
    }
}
    
    // добавление яиц и фейковых яиц в массивы
    if (Math.random() < 0.01) {
    eggs.push({x: Math.random() * cvs.width, y: -50, type: "egg"});
    }
    if (Math.random() < 0.005) {
    fakeEggs.push({x: Math.random() * cvs.width, y: -50, type: "fake_egg"});
    }
    
    // добавление бомб в массив
    if (Math.random() < 0.002) {
    bombs.push({x: Math.random() * cvs.width, y: -50, type: "bomb"});
    }
    
    // отрисовка объектов и счета игрока
    drawGrass();
    drawTree();
    drawWolf();
    drawEggs();
    drawFakeEggs();
    drawBombs();
    drawScore();
    
    // проверка поражения
    if (score < -20) {
    alert("Game over!");
    clearInterval(interval);
    }
    }
    
    // запуск игры
    var interval = setInterval(update, 10);
    
    // обработчик нажатия на клавиши
    document.addEventListener("keydown", function(event) {
    if (event.code === "ArrowLeft" && wolfX > 0) {
    wolfX -= 20;
    } else if (event.code === "ArrowRight" && wolfX < cvs.width - 50) {
    wolfX += 20;
    }
    }); 
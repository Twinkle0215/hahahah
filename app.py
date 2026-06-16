import streamlit as st
import streamlit.components.v1 as components
 
st.set_page_config(page_title="가시 피하기 게임", layout="wide")
 
st.markdown("""
    <style>
        .block-container { padding: 0 !important; }
        iframe { border: none !important; }
    </style>
""", unsafe_allow_html=True)
 
game_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body { margin: 0; background: #0a0a15; display: flex; justify-content: center; padding: 20px; }
</style>
</head>
<body>
 
<div id="game-container" style="text-align: center; font-family: 'Segoe UI', Arial, sans-serif; background: #0a0a15; padding: 25px; border-radius: 20px; box-shadow: 0 15px 45px rgba(0,0,0,0.8); width: 700px; margin: 0 auto; user-select: none;">
    <h2 style="color: #00f2fe; text-shadow: 0 0 15px #00f2fe; margin: 0 0 10px 0;">🔥 13.0 버전 🔥</h2>
    <div style="position: relative; width: 660px; height: 280px; margin: 0 auto;">
        <canvas id="gameCanvas" width="660" height="280" style="border:3px solid #333; border-radius: 10px; background: #05050a; display: block; cursor: pointer;"></canvas>
        <div id="start-screen" style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,0.85); border-radius: 8px; display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; z-index: 10;">
            <h1 style="color: #ff3366; margin-bottom: 5px; text-shadow: 0 0 15px #ff3366;">가시 피하기!</h1>
            <p style="color: #bbb; margin-bottom: 15px;">일반 모드: 10초마다 속도 가속 & 5초마다 가시 최대치 +1칸!</p>
            <div style="margin-bottom: 20px;">
                <label style="margin: 0 15px; font-size: 16px; font-weight: bold; color: #00ff87; cursor:pointer;"><input type="radio" name="gameModeSelect" value="classic" checked> 일반 모드 (5초 진화형)</label>
                <label style="margin: 0 15px; font-size: 16px; font-weight: bold; color: #00f2fe; cursor:pointer;"><input type="radio" name="gameModeSelect" value="random"> 랜덤 모드 (멀티버스)</label>
            </div>
            <div style="display: flex; gap: 15px;">
                <button id="start-btn" style="padding: 12px 35px; font-size: 18px; font-weight: bold; background: linear-gradient(45deg, #ff007f, #00f2fe); border:none; border-radius: 30px; color:#fff; cursor:pointer;">GAME START</button>
                <button id="credits-btn" style="padding: 12px 25px; font-size: 16px; font-weight: bold; background: #1a1a3a; border: 2px solid #00f2fe; border-radius: 30px; color:#00f2fe; cursor:pointer;">CREDITS</button>
            </div>
        </div>
        <div id="settings-menu" style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(5,5,15,0.9); border-radius: 8px; display: none; flex-direction: column; justify-content: center; align-items: center; color: white; z-index: 15;">
            <h2 style="color: #ffbc00; margin-bottom: 20px;">PAUSED / SETTINGS</h2>
            <div style="display: flex; flex-direction: column; gap: 12px; width: 250px;">
                <button id="resume-btn" style="padding: 10px; font-weight: bold; background: #333; color: #fff; border: 1px solid #555; border-radius: 6px; cursor: pointer;">계속하기 (RESUME)</button>
                <button id="practice-btn" style="padding: 10px; font-weight: bold; background: #113322; color: #00ff87; border: 1px solid #00ff87; border-radius: 6px; cursor: pointer;">연습 모드: OFF</button>
                <div style="background: #222; padding: 8px; border-radius: 6px; border: 1px solid #444; text-align: center;">
                    <span style="font-size: 13px; display: block; margin-bottom: 5px; color: #aaa;">프레임 제한 (FPS LIMIT)</span>
                    <select id="fps-select" style="background: #000; color: #fff; border: 1px solid #666; padding: 3px 10px; border-radius: 4px; cursor: pointer; width: 100%;">
                        <option value="max">제한 없음 (Max)</option>
                        <option value="60">60 FPS</option>
                        <option value="30">30 FPS</option>
                    </select>
                </div>
                <button id="home-btn" style="padding: 10px; font-weight: bold; background: #441111; color: #ff6666; border: 1px solid #ff3333; border-radius: 6px; cursor: pointer;">홈 메뉴로 이동</button>
            </div>
        </div>
        <div id="credits-screen" style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(5,5,15,0.95); border-radius: 8px; display: none; flex-direction: column; justify-content: center; align-items: center; color: white; z-index: 20; border: 2px solid #00f2fe;">
            <h2 style="color: #00f2fe; margin-bottom: 25px;">🎮 GAME CREDITS 🎮</h2>
            <div style="background: rgba(255,255,255,0.05); padding: 20px 40px; border-radius: 12px; border: 1px solid #333; margin-bottom: 25px; text-align: left; width: 300px; line-height: 2;">
                <div style="font-size: 18px; color: #00ff87; font-weight: bold; display: flex; justify-content: space-between;"><span>💡 아이디어 :</span><span style="color:#fff;">나</span></div>
                <div style="font-size: 18px; color: #ff3366; font-weight: bold; display: flex; justify-content: space-between; margin-top: 10px;"><span>🛠️ 제 작 :</span><span style="color:#fff;">제미나이 (Gemini)</span></div>
            </div>
            <button id="credits-close-btn" style="padding: 10px 35px; font-weight: bold; background: #333; color: #fff; border: 1px solid #666; border-radius: 20px; cursor: pointer;">닫기 (CLOSE)</button>
        </div>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px; color: white; padding: 0 10px;">
        <div style="text-align: left;">
            <div style="font-size: 18px; color: #00ff87; font-weight: bold;">SCORE: <span id="score">0</span></div>
            <div style="margin-top: 5px; display: flex; gap: 5px;">
                <div id="type-badge" style="display: inline-block; padding: 2px 10px; border-radius: 4px; background: #00ff87; color: black; font-weight: bold; font-size: 12px;">일반 모드</div>
                <div id="mode-badge" style="display: inline-block; padding: 2px 10px; border-radius: 4px; background: #00ff87; color: black; font-weight: bold; font-size: 12px;">CUBE</div>
                <div id="max-spike-badge" style="display: inline-block; padding: 2px 10px; border-radius: 4px; background: #ff3366; color: white; font-weight: bold; font-size: 12px;">최대 가시: 3칸</div>
            </div>
        </div>
        <div><button id="pause-btn" style="padding: 8px 18px; background: #222; border: 1px solid #444; color: white; border-radius: 5px; cursor: pointer; font-weight: bold;">PAUSE (P)</button></div>
        <div style="text-align: right; line-height: 1.3;">
            <div style="font-size: 18px; color: #00f2fe; font-weight: bold;">SPEED: <span id="speed-display">7.5</span></div>
            <div id="spike-timer" style="font-size: 11px; color: #ff3366; font-weight: bold;">가시 확장: 5.0초</div>
            <div id="speed-timer" style="font-size: 11px; color: #ffbc00; font-weight: bold;">속도 가속: 10.0초</div>
        </div>
    </div>
</div>
 
<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const scoreElement = document.getElementById("score");
const speedElement = document.getElementById("speed-display");
const speedTimerElement = document.getElementById("speed-timer");
const spikeTimerElement = document.getElementById("spike-timer");
const typeBadge = document.getElementById("type-badge");
const modeBadge = document.getElementById("mode-badge");
const maxSpikeBadge = document.getElementById("max-spike-badge");
const startScreen = document.getElementById("start-screen");
const settingsMenu = document.getElementById("settings-menu");
const creditsScreen = document.getElementById("credits-screen");
const startBtn = document.getElementById("start-btn");
const creditsBtn = document.getElementById("credits-btn");
const creditsCloseBtn = document.getElementById("credits-close-btn");
const pauseBtn = document.getElementById("pause-btn");
const resumeBtn = document.getElementById("resume-btn");
const practiceBtn = document.getElementById("practice-btn");
const homeBtn = document.getElementById("home-btn");
const fpsSelect = document.getElementById("fps-select");
 
const CEILING_Y = 0;
const GROUND_Y = 240;
 
let player, obstacles, score, isGameOver, isPaused, baseSpeed, jumpPower, obstacleTimer, loopId;
let selectedSystemMode = "classic";
let highScoreClassic = 0, highScoreRandom = 0;
let isPressing = false, isJustPressed = false;
let currentMode = "CUBE";
let isMini = false, ballGravity = 1, isPracticeMode = false;
let currentSpeedMultiplier = 1;
let classicSpeedTimer = 0, classicSpikeTimer = 0, maxSpikesAllowed = 3;
let fpsLimit = "max", lastFrameTime = 0;
let playerTrail = [], deathParticles = [];
 
const pColors = { CUBE: "#00ff87", SHIP: "#ff007f", BALL: "#ffbc00", WAVE: "#00f2fe" };
const arrowColors = { 1: "#00ff87", 2: "#ffbc00", 3: "#ff3366", 4: "#e040ff" };
 
function initGame() {
    cancelAnimationFrame(loopId); clearInterval(obstacleTimer);
    selectedSystemMode = document.querySelector('input[name="gameModeSelect"]:checked').value;
    if (selectedSystemMode === "classic") {
        baseSpeed = 7.5; jumpPower = -12.0; currentMode = "CUBE"; isMini = false;
        classicSpeedTimer = 10.0; classicSpikeTimer = 5.0; maxSpikesAllowed = 3;
    } else { baseSpeed = 8.0; jumpPower = -12.5; currentMode = "CUBE"; isMini = false; }
    player = { x: 100, y: GROUND_Y - 26, size: 26, vy: 0, gravity: 0.76, jumpForce: jumpPower, isGrounded: true, rotation: 0 };
    obstacles = []; playerTrail = []; deathParticles = [];
    score = 0; currentSpeedMultiplier = 1; ballGravity = 1;
    isGameOver = false; isPaused = false; isJustPressed = false;
    updateUI();
    startScreen.style.display = "none"; settingsMenu.style.display = "none";
    creditsScreen.style.display = "none"; pauseBtn.style.display = "inline-block";
    obstacleTimer = setInterval(spawnManager, 850);
    lastFrameTime = performance.now();
    loopId = requestAnimationFrame(gameLoop);
}
 
function updateUI() {
    scoreElement.innerText = score;
    modeBadge.innerText = currentMode; modeBadge.style.background = pColors[currentMode];
    if (selectedSystemMode === "classic") {
        typeBadge.innerText = "일반 모드"; typeBadge.style.background = "#00ff87";
        speedElement.innerText = baseSpeed.toFixed(1);
        speedTimerElement.style.display = "block";
        speedTimerElement.innerText = "속도 가속: " + classicSpeedTimer.toFixed(1) + "초";
        spikeTimerElement.style.display = "block";
        spikeTimerElement.innerText = "가시 확장: " + classicSpikeTimer.toFixed(1) + "초";
        maxSpikeBadge.style.display = "inline-block";
        maxSpikeBadge.innerText = "최대 가시: " + maxSpikesAllowed + "칸";
        maxSpikeBadge.style.background = "#ff3366"; maxSpikeBadge.style.color = "white";
    } else {
        typeBadge.innerText = "랜덤 모드"; typeBadge.style.background = "#00f2fe";
        speedElement.innerText = currentSpeedMultiplier + "x";
        speedTimerElement.style.display = "none"; spikeTimerElement.style.display = "none";
        maxSpikeBadge.style.display = "inline-block"; maxSpikeBadge.innerText = "MULTIVERSE";
        maxSpikeBadge.style.background = "#ffffff"; maxSpikeBadge.style.color = "#000";
    }
    if (isPracticeMode) { practiceBtn.innerText = "연습 모드: ON"; practiceBtn.style.background = "#00ff87"; practiceBtn.style.color = "#000"; }
    else { practiceBtn.innerText = "연습 모드: OFF"; practiceBtn.style.background = "#113322"; practiceBtn.style.color = "#00ff87"; }
}
 
function spawnManager() {
    if(isGameOver || isPaused) return;
    let width = isMini ? 20 : 30; let height = isMini ? 24 : 36; let rand = Math.random();
    if (selectedSystemMode === "classic") {
        let count = Math.floor(Math.random() * maxSpikesAllowed) + 1;
        for(let i=0; i<count; i++) obstacles.push({ x: canvas.width + (i * (width-2)), y: GROUND_Y, width: width, height: height, type: 'spike', pos: 'bottom', isBig: false });
        return;
    }
    if (currentMode === "CUBE" || currentMode === "BALL") {
        if (rand < 0.4) {
            let count = Math.floor(Math.random() * 3) + 1;
            for(let i=0; i<count; i++) obstacles.push({ x: canvas.width + (i * (width + 4)), y: GROUND_Y, width: width, height: height, type: 'spike', pos: 'bottom', isBig: false });
        } else if (rand < 0.65) {
            let count = Math.floor(Math.random() * 3) + 1;
            for(let i=0; i<count; i++) obstacles.push({ x: canvas.width + (i * (width + 10)), y: CEILING_Y + height, width: width, height: height, type: 'spike', pos: 'top', isBig: false });
        } else {
            let blockHeight = 55 + Math.floor(Math.random() * 55); let blockWidth = 70 + Math.floor(Math.random() * 40);
            obstacles.push({ x: canvas.width, y: GROUND_Y - blockHeight, width: blockWidth, height: 18, type: 'block' });
            if(Math.random() < 0.4) obstacles.push({ x: canvas.width + 25, y: GROUND_Y - blockHeight, width: 20, height: 22, type: 'spike', pos: 'bottom', isBig: false });
        }
    } else if (currentMode === "SHIP") {
        if (rand < 0.6) {
            let sw = isMini ? 15 : 24; let sh = isMini ? 30 : 45; let isBottom = Math.random() < 0.5; let count = Math.floor(Math.random() * 2) + 1;
            for(let i=0; i<count; i++) obstacles.push({ x: canvas.width + (i * (sw + 15)), y: isBottom ? GROUND_Y : CEILING_Y + sh, width: sw, height: sh, type: 'spike', pos: isBottom ? 'bottom' : 'top', isBig: false });
        } else obstacles.push({ x: canvas.width, y: 60 + Math.random() * 70, width: 60, height: 35, type: 'block' });
    } else if (currentMode === "WAVE") {
        obstacles.push({ x: canvas.width, y: 50 + Math.random() * 80, width: 60, height: 40, type: 'block' });
    }
    if (Math.random() < 0.18) {
        const modes = ["CUBE","SHIP","BALL","WAVE"].filter(m => m !== currentMode);
        obstacles.push({ x: canvas.width + 190, y: 5, width: 35, height: 230, type: 'portal', portalTo: modes[Math.floor(Math.random() * modes.length)] });
    }
    if (Math.random() < 0.12) obstacles.push({ x: canvas.width + 230, y: 15, width: 35, height: 210, type: 'sizePortal', sizeToMini: !isMini });
    if (Math.random() < 0.12) {
        const speeds = [1,2,3,4].filter(s => s !== currentSpeedMultiplier);
        obstacles.push({ x: canvas.width + 270, y: 10, width: 40, height: 220, type: 'speedArrow', targetSpeed: speeds[Math.floor(Math.random() * speeds.length)] });
    }
}
 
function handleInput() {
    if (isGameOver || isPaused) return;
    let fm = isMini ? 1.15 : 1.0;
    if (currentMode === "CUBE") {
        if (isPressing && player.isGrounded) {
            let sb = selectedSystemMode === "classic" ? (baseSpeed * 0.04) : 0;
            player.vy = (player.jumpForce - sb) * (isMini ? 0.88 : 1.0); player.isGrounded = false;
        }
    } else if (currentMode === "SHIP") {
        if (isPressing) player.vy -= (0.95 * fm);
    } else if (currentMode === "WAVE") {
        let cs = selectedSystemMode === "classic" ? baseSpeed : (baseSpeed + (currentSpeedMultiplier - 1) * 1.8);
        player.vy = isPressing ? -cs * 0.9 * fm : cs * 0.9 * fm;
    }
}
 
function handleBallClick() { if (currentMode === "BALL" && player.isGrounded) { ballGravity *= -1; player.isGrounded = false; } }
 
function checkCollision(p, o) {
    let pL = p.x+5, pR = p.x+p.size-5, pT = p.y+4, pB = p.y+p.size-4;
    if (o.type === 'spike') {
        let pad = o.isBig ? 14 : 7, oL = o.x+pad, oR = o.x+o.width-pad, oT, oB;
        if (o.pos === 'bottom') { oT = o.y-o.height+3; oB = o.y; } else { oT = o.y; oB = o.y+o.height-3; }
        if (pR>oL && pL<oR && pB>oT && pT<oB) return !isPracticeMode;
    } else if (o.type === 'block') {
        if (pR>o.x && pL<o.x+o.width && pB>o.y && pT<o.y+o.height) {
            if (currentMode !== "WAVE" && pB <= o.y+12 && p.vy * (currentMode==="BALL" ? ballGravity : 1) >= 0) { player.y = o.y-player.size; player.vy = 0; player.isGrounded = true; return false; }
            return !isPracticeMode;
        }
    } else if (o.type === 'portal') {
        if (pR>o.x && pL<o.x+o.width && pB>o.y && pT<o.y+o.height) { if (currentMode !== o.portalTo) { currentMode = o.portalTo; ballGravity = 1; updateUI(); } }
    } else if (o.type === 'sizePortal') {
        if (pR>o.x && pL<o.x+o.width && pB>o.y && pT<o.y+o.height) { if (isMini !== o.sizeToMini) { isMini = o.sizeToMini; player.size = isMini ? 16 : 26; updateUI(); } }
    } else if (o.type === 'speedArrow') {
        if (pR>o.x && pL<o.x+o.width && pB>o.y && pT<o.y+o.height) { if (currentSpeedMultiplier !== o.targetSpeed) { currentSpeedMultiplier = o.targetSpeed; updateUI(); } }
    }
    return false;
}
 
function createDeathEffect(x, y, color) {
    for(let i=0; i<40; i++) deathParticles.push({ x, y, vx: (Math.random()-0.5)*10, vy: (Math.random()-0.5)*10, size: Math.random()*4+2, alpha: 1, color });
}
 
function update() {
    if (isGameOver) { deathParticles.forEach(p => { p.x+=p.vx; p.y+=p.vy; p.alpha-=0.02; }); deathParticles = deathParticles.filter(p => p.alpha>0); return; }
    if (isPaused) return;
    if (selectedSystemMode === "classic") {
        let ts = 1/60;
        classicSpeedTimer -= ts; if (classicSpeedTimer <= 0) { baseSpeed *= 1.15; classicSpeedTimer = 10.0; }
        classicSpikeTimer -= ts; if (classicSpikeTimer <= 0) { maxSpikesAllowed++; classicSpikeTimer = 5.0; }
    }
    handleInput();
    let cs = selectedSystemMode === "classic" ? baseSpeed : (baseSpeed + (currentSpeedMultiplier-1)*1.8);
    let lg = player.gravity * (isMini ? 1.35 : 1.0);
    if (currentMode === "CUBE") {
        player.vy += lg; player.y += player.vy;
        if (player.y >= GROUND_Y-player.size) { player.y = GROUND_Y-player.size; player.vy = 0; player.isGrounded = true; player.rotation = Math.round(player.rotation/90)*90; }
        else player.rotation += cs*1.4;
    } else if (currentMode === "SHIP") {
        player.vy += (0.48*(isMini?1.3:1.0)); player.vy *= 0.91; player.y += player.vy;
        player.rotation = player.vy*2.5;
        if (player.y >= GROUND_Y-player.size) { player.y = GROUND_Y-player.size; player.vy = 0; }
        if (player.y <= CEILING_Y) { player.y = CEILING_Y; player.vy = 0; }
    } else if (currentMode === "BALL") {
        player.vy += lg*ballGravity; player.y += player.vy;
        if (ballGravity===1 && player.y >= GROUND_Y-player.size) { player.y = GROUND_Y-player.size; player.vy = 0; player.isGrounded = true; }
        else if (ballGravity===-1 && player.y <= CEILING_Y) { player.y = CEILING_Y; player.vy = 0; player.isGrounded = true; }
        else player.isGrounded = false;
        player.rotation += cs*1.8*ballGravity;
    } else if (currentMode === "WAVE") {
        player.y += player.vy; player.rotation = player.vy>0 ? 30 : -30;
        if (player.y <= CEILING_Y) { player.y = CEILING_Y; player.vy = 0; }
        if (player.y >= GROUND_Y-player.size) { player.y = GROUND_Y-player.size; player.vy = 0; }
    }
    playerTrail.push({ x: player.x+player.size/2, y: player.y+player.size/2, color: pColors[currentMode] });
    if (playerTrail.length > 35) playerTrail.shift();
    playerTrail.forEach(t => t.x -= cs);
    for (let i = obstacles.length-1; i >= 0; i--) {
        obstacles[i].x -= cs;
        if (checkCollision(player, obstacles[i])) { triggerGameOver(); return; }
        if (obstacles[i].x+obstacles[i].width < 0) {
            if(obstacles[i].type !== 'portal' && obstacles[i].type !== 'sizePortal' && obstacles[i].type !== 'speedArrow' && !obstacles[i].counted) { score++; obstacles[i].counted = true; }
            obstacles.splice(i, 1);
        }
    }
    updateUI(); isJustPressed = false;
}
 
function triggerGameOver() {
    isGameOver = true; clearInterval(obstacleTimer);
    if (!isPracticeMode) {
        if (selectedSystemMode === "classic" && score > highScoreClassic) highScoreClassic = score;
        if (selectedSystemMode === "random" && score > highScoreRandom) highScoreRandom = score;
    }
    createDeathEffect(player.x+player.size/2, player.y+player.size/2, pColors[currentMode]);
}
 
function draw() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.strokeStyle = "#252538"; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(0,GROUND_Y); ctx.lineTo(canvas.width,GROUND_Y); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(0,CEILING_Y+2); ctx.lineTo(canvas.width,CEILING_Y+2); ctx.stroke();
    if (playerTrail.length > 1) {
        ctx.save(); ctx.lineWidth = currentMode==="WAVE" ? 4 : 2;
        for (let i=1; i<playerTrail.length; i++) {
            ctx.strokeStyle = playerTrail[i].color; ctx.globalAlpha = i/playerTrail.length*0.6;
            ctx.beginPath(); ctx.moveTo(playerTrail[i-1].x,playerTrail[i-1].y); ctx.lineTo(playerTrail[i].x,playerTrail[i].y); ctx.stroke();
        }
        ctx.restore();
    }
    deathParticles.forEach(p => { ctx.save(); ctx.globalAlpha=p.alpha; ctx.fillStyle=p.color; ctx.fillRect(p.x,p.y,p.size,p.size); ctx.restore(); });
    obstacles.forEach(o => {
        if(o.type==='spike') {
            ctx.fillStyle = o.isBig?"#ff0055":"#ff3366"; ctx.beginPath();
            if(o.pos==='bottom') { ctx.moveTo(o.x,o.y); ctx.lineTo(o.x+o.width/2,o.y-o.height); ctx.lineTo(o.x+o.width,o.y); }
            else { ctx.moveTo(o.x,CEILING_Y); ctx.lineTo(o.x+o.width/2,CEILING_Y+o.height); ctx.lineTo(o.x+o.width,CEILING_Y); }
            ctx.fill(); ctx.strokeStyle="white"; ctx.lineWidth=o.isBig?2.5:1.5; ctx.stroke();
        } else if(o.type==='block') {
            ctx.fillStyle="#4facfe"; ctx.fillRect(o.x,o.y,o.width,o.height); ctx.strokeStyle="white"; ctx.strokeRect(o.x,o.y,o.width,o.height);
        } else if(o.type==='portal') {
            ctx.strokeStyle=pColors[o.portalTo]; ctx.lineWidth=6;
            ctx.beginPath(); ctx.ellipse(o.x+o.width/2,o.y+o.height/2,o.width/2,o.height/2,0,0,Math.PI*2); ctx.stroke();
        } else if(o.type==='sizePortal') {
            ctx.save(); ctx.strokeStyle=o.sizeToMini?"#e040ff":"#ffffff"; ctx.lineWidth=4; ctx.setLineDash([5,5]);
            ctx.beginPath(); ctx.ellipse(o.x+o.width/2,o.y+o.height/2,o.width/2,o.height/2,0,0,Math.PI*2); ctx.stroke(); ctx.restore();
        } else if(o.type==='speedArrow') {
            ctx.save(); ctx.fillStyle=arrowColors[o.targetSpeed]; ctx.shadowBlur=10; ctx.shadowColor=arrowColors[o.targetSpeed];
            let stepY=o.height/6;
            for(let a=0; a<6; a++) { let cy=o.y+(a*stepY)+5; for(let b=0; b<3; b++) { let ox=o.x+(b*9); ctx.beginPath(); ctx.moveTo(ox,cy); ctx.lineTo(ox+14,cy+12); ctx.lineTo(ox,cy+24); ctx.fill(); } }
            ctx.restore();
        }
    });
    if (!isGameOver) {
        ctx.save(); ctx.translate(player.x+player.size/2,player.y+player.size/2); ctx.rotate(player.rotation*Math.PI/180); ctx.fillStyle=pColors[currentMode];
        if(currentMode==="CUBE") { ctx.fillRect(-player.size/2,-player.size/2,player.size,player.size); ctx.strokeStyle="black"; ctx.strokeRect(-player.size/2+(isMini?2:4),-player.size/2+(isMini?2:4),player.size-(isMini?4:8),player.size-(isMini?4:8)); }
        else if(currentMode==="SHIP") { ctx.beginPath(); ctx.moveTo(-player.size*0.6,player.size*0.25); ctx.lineTo(player.size*0.6,0); ctx.lineTo(-player.size*0.6,-player.size*0.5); ctx.fill(); }
        else if(currentMode==="BALL") { ctx.beginPath(); ctx.arc(0,0,player.size/2,0,Math.PI*2); ctx.fill(); ctx.strokeStyle="black"; ctx.beginPath(); ctx.moveTo(-player.size/2,0); ctx.lineTo(player.size/2,0); ctx.stroke(); }
        else if(currentMode==="WAVE") { ctx.beginPath(); ctx.moveTo(-player.size*0.5,player.size*0.3); ctx.lineTo(player.size*0.5,0); ctx.lineTo(-player.size*0.5,-player.size*0.3); ctx.fill(); }
        ctx.restore();
    } else {
        ctx.fillStyle="rgba(0,0,0,0.65)"; ctx.fillRect(0,0,canvas.width,canvas.height);
        ctx.fillStyle="#ff3366"; ctx.font="bold 28px 'Segoe UI'"; ctx.textAlign="center";
        ctx.fillText("CRASHED",canvas.width/2,canvas.height/2-25);
        let hs = selectedSystemMode==="classic" ? highScoreClassic : highScoreRandom;
        ctx.fillStyle="#fff"; ctx.font="bold 16px 'Segoe UI'";
        ctx.fillText("현재 기록: "+score+"  |  (모드 최고기록: "+hs+")",canvas.width/2,canvas.height/2+5);
        ctx.fillStyle="#bbb"; ctx.font="13px 'Segoe UI'";
        ctx.fillText("클릭, Space 또는 위쪽 방향키(▲)를 누르면 재도전",canvas.width/2,canvas.height/2+35);
    }
}
 
function gameLoop(timestamp) {
    if (isPaused) return;
    if (fpsLimit==="max") { update(); draw(); loopId=requestAnimationFrame(gameLoop); }
    else {
        let ti=1000/parseInt(fpsLimit), el=timestamp-lastFrameTime;
        if (el>=ti) { lastFrameTime=timestamp-(el%ti); update(); draw(); }
        loopId=requestAnimationFrame(gameLoop);
    }
}
 
function togglePause() {
    if(isGameOver) return; isPaused=!isPaused;
    if(!isPaused) { settingsMenu.style.display="none"; lastFrameTime=performance.now(); gameLoop(performance.now()); }
    else { settingsMenu.style.display="flex"; ctx.fillStyle="rgba(0,0,0,0.4)"; ctx.fillRect(0,0,canvas.width,canvas.height); }
}
 
window.addEventListener("keydown", e => {
    if(e.code==="Space"||e.code==="ArrowUp") { e.preventDefault(); if(isGameOver) initGame(); else { if(!isPressing) isJustPressed=true; isPressing=true; handleBallClick(); } }
    if(e.code==="KeyP") { e.preventDefault(); togglePause(); }
});
window.addEventListener("keyup", e => { if(e.code==="Space"||e.code==="ArrowUp") isPressing=false; });
canvas.addEventListener("mousedown", () => { if(isGameOver) initGame(); else { isJustPressed=true; isPressing=true; handleBallClick(); } });
window.addEventListener("mouseup", () => isPressing=false);
 
startBtn.addEventListener("click", initGame);
pauseBtn.addEventListener("click", togglePause);
resumeBtn.addEventListener("click", togglePause);
creditsBtn.addEventListener("click", () => { creditsScreen.style.display="flex"; });
creditsCloseBtn.addEventListener("click", () => { creditsScreen.style.display="none"; });
practiceBtn.addEventListener("click", () => { isPracticeMode=!isPracticeMode; updateUI(); });
homeBtn.addEventListener("click", () => {
    isPaused=false; settingsMenu.style.display="none"; startScreen.style.display="flex";
    clearInterval(obstacleTimer); cancelAnimationFrame(loopId);
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.fillStyle="#555"; ctx.font="16px Arial"; ctx.textAlign="center";
    ctx.fillText("플레이 할 모드를 선택하고 GAME START를 누르세요",canvas.width/2,canvas.height/2);
});
fpsSelect.addEventListener("change", e => { fpsLimit=e.target.value; });
 
ctx.fillStyle="#555"; ctx.font="16px Arial"; ctx.textAlign="center";
ctx.fillText("플레이 할 모드를 선택하고 GAME START를 누르세요",canvas.width/2,canvas.height/2);
</script>
 
</body>
</html>
"""
 
components.html(game_html, height=520, scrolling=False)
 

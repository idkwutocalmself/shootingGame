var started = false;
var s = function(sketch) {
    sketch.setup = function() {
        sketch.createCanvas(800, 600);
        p5Ready();
        draw.canvas.onclick = function() {
			window.start = new Date().getTime();
            startGame(draw.canvas);
            draw.canvas.onclick = null;
        };
    };
};
var spawnsPerX = {};
var draw = new p5(s, 'pad');

function p5Ready() {
    draw.textWrap('CHAR');
    draw.textSize(50);
    draw.text('some text', 50, 60);
}

function startGame() {
    draw.textWrap('CHAR');
    draw.clear();
    draw.text('some more text this is some text that will wrap lololololololololololololololololol', 50, 60, 700);
}
alreadyJoinedWarning = ['You have already joined.', 'Stop asking to join if you have already joined.', 'Please stop joining again.', 'STOP! THIS IS YOUR FINAL WARNING TO STOP PRESSING THE JOIN KEY!'];
var p1joined = false;
var p1curwarn = 0;
var p2joined = false;
var p2curwarn = 0;
onkeydown = function(ev) {
	if (!started) {
		switch (ev.keyCode) {
			case 191:
				if (p2joined) {
					
				}
				break;
		}
	}
}
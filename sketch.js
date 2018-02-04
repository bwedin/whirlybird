// save this file as sketch.js
// Sketch One

var x = 100.0; 
var y = 100;
var speed = 2.5; 
var uploadedImage = null;

var fileDrop = function( p ) {
  var x = 100; 
  var y = 100;
  p.setup = function() {
  // create canvas
    var c = p.createCanvas(200, 200);
    c.parent('sketch-holder-2');
    p.background(100);
    // Add an event for when a file is dropped onto the canvas
    c.drop(p.gotFile);
  }

  p.draw = function() {
    p.fill(255);
    p.noStroke();
    p.textSize(12);
    p.text('Drag an image file onto the canvas.', 10, 20);
    p.noLoop();
  }

  p.gotFile = function(file) {
    console.log('yo?')
    console.log(file.type)
    // If it's an image file
    if (file.type === 'image') {

      // Create an image DOM element but don't show it
      var img = p.createImg(file.data).hide();
      // Draw the image onto the canvas
      uploaded(img);
    } else {
      println('Not an image file!');
    }
}

};

function uploaded(img) {
    uploadedImage = img;
    console.log('hello!');
  }

function setup() {
    var myp5 = new p5(fileDrop, 'c1');
    var canvas = createCanvas(400, 200);
    canvas.parent('sketch-holder');
};

function draw() {
    background(100);
    fill(1);
    x += speed; 
    if(x > width){
      x = 0; 
    }
    ellipse(x,y,50,50);
    if(uploadedImage) {
      image(uploadedImage, 0, 0, width, height);
    }
  };


function uploadedFile(inputDiv) {
  console.log($(inputDiv).val());
}


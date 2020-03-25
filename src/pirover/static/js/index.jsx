// add handler to each button
import axios from 'axios';

// MOVE ACTIONS

var currMove = null

function move() {
  if(currMove != null) {
    axios.post('/api/action/move', {
      direction: currMove,
      args: {
        wait: false,
        duration: 0.5
      }
    })
    .catch(function (error) {
      console.log(error)
    });
  }
}

setInterval(move, 50);

document.getElementById('leftButton').onmousedown = function() { currMove = 'left' }
document.getElementById('leftButton').onmouseup = function() { currMove = null }
document.getElementById('rightButton').onmousedown = function() { currMove = 'right' }
document.getElementById('rightButton').onmouseup = function() { currMove = null }
document.getElementById('forwardButton').onmousedown = function() { currMove = 'forward' }
document.getElementById('forwardButton').onmouseup = function() { currMove = null }
document.getElementById('backwardButton').onmousedown = function() { currMove = 'backward' }
document.getElementById('backwardButton').onmouseup = function() { currMove = null }

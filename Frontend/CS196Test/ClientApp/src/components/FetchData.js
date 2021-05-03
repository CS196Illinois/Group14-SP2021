import React, { Component } from 'react';
import './FetchData.css';
import $ from 'jquery';
export class FetchData extends Component {
  static displayName = FetchData.name;


  startVideo(event)
  {
    const player = document.getElementById('player');
    const constraints = {video: true,};
    navigator.mediaDevices.getUserMedia(constraints).then((stream) => {player.srcObject = stream;});
  }

  captureImg(event)
  {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
    const player = document.getElementById('player');
    context.drawImage(player, 0, 0, canvas.width, canvas.height);
    var dataURL = canvas.toDataURL();
    $.ajax({
        traditional:true,
        url:'http://localhost:5000/capture',
        type:"POST",
        data:dataURL,
        success:function(response) {document.getElementById('feedback').innerHTML = response},
        error:function(response) {document.getElementById('feedback').innerHTML = 'an error occured. Please try again'}
        });
  }



  render() {
    return (
    <div>
        <h1>Webcam Mask Detection</h1>
        <div class = 'videoPlayer'>
            <video id="player" controls autoPlay></video>
        </div>

        <div class='preview'>
            <h3>image preview</h3>
            <canvas id="canvas" width='320' height='240'></canvas>
            <div>
                <b>Feedback: </b>
                <b id='feedback'> No input provided</b>
            </div>
        </div>

        <div class = 'start button'>
            <button onClick={this.startVideo}>Enable your webcam</button>
            <button onClick={this.captureImg}> capture an image</button>
        </div>
    </div>
    );
  }
}

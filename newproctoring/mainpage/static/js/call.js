navigator.mediaDevices.getUserMedia({video: true, audio: true})
  .then(function(stream) {
    var video = document.querySelector('video');
    video.srcObject = stream;
    video.onloadedmetadata = function(e) {
      video.play();
    };
  })
  .catch(function(err) {
    console.log(err.name + ": " + err.message);
  });

// var socket = io.connect('http://localhost:8000');
// $('#generate-btn').click(function() {
//     socket.emit('generate_event');
// });

// socket.on('generated_output', function(output) {
//     $('#generated-text').append(output + '<br>');
// });
$(document).ready(function() {
  var socket = io.connect('http://' + document.domain + ':' + location.port);

  $('#generate-btn').click(function() {
      var userInput = $('#user-input').val();
      socket.emit('generate_event', userInput);
  });

  socket.on('generated_output', function(output) {
      $('#output-div').html(output);
  });
});















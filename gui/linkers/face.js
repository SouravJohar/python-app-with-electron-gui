function detect_faces() {

  document.getElementById("detect").value = "Hang on..."
  var python = require("python-shell")
  var path = require("path")

    var options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    pythonPath : '/usr/local/bin/python3'
  }

  var face = new python("faces.py", options);

  face.end(function(err, code, message) {
    document.getElementById("detect").value = "Detect faces";
    })

}


function add_face(){
  var python = require("python-shell")
  var path = require("path")
  var name = document.getElementById("person").value

    var options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    pythonPath : '/usr/local/bin/python3',
    args : ["cam", name]
  }

  var face = new python("add_face.py", options);

  face.end(function(err, code, message) {
    swal("Face added!", "We can now recognize your face", "success")
    document.getElementsById("add").innerHTML = "Add a new face";
  })
}

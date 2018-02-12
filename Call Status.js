// Node.JS version
// Miles away from working just yet...... :(
//
)
var http = require("http");

var options = {
  "method": "GET",
  "hostname": [
    "192",
    "168",
    "1",
    "86"
  ],
  "path": [
    "getxml"
  ],
  "headers": {
    "Authorization": "Basic aW50ZWdyYXRvcjppbnRlZ3JhdG9y",
  }
};

var req = http.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.end();
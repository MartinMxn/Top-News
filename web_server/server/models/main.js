const mongoose = require("mongoose");

module.exports.connect = uri => {
  // don't forget to add user on mlib
  mongoose.connect(uri, {useNewUrlParser: true, useCreateIndex: true,});

  mongoose.connection.on("error", err => {
    console.error(`Mongoose connection error: ${err}`);
    process.exit(1);
  });

  //load models
  require("./user");
};

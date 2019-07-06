import React from "react";
import ReactDom from "react-dom";

import { browserHistory, Router } from "react-router";
import routes from "./routes";
import "bootstrap/dist/css/bootstrap.min.css";
import "materialize-css/dist/css/materialize.min.css";

ReactDom.render(
  <Router history={browserHistory} routes={routes} />,
  document.getElementById("root")
);

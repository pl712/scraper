import React from "react";
import Sidebar from "./Sidebar";
import Feed from "./Feed";
import Widgets from "./Widgets";
import RightPanel from "./RightPanel";
import "./App.css";

function App() {
  return (
    // BEM
    <div className="app">
      <Sidebar />
      <Feed />
      {/* <Widgets /> */}
      {/* <RightPanel /> */}
    </div>
  );
}

export default App;

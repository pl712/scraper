import Sidebar from "./Sidebar";
import Feed from "./Feed";
import Widgets from "./Widgets";
import RightPanel from "./RightPanel";
import "./App.css";
import React, { useState } from 'react';

function App() {
  const [selectedCategory, setSelectedCategory] = useState(null);
  function handleCategorySelect(category) {
    setSelectedCategory(category);
  }

  return (
    // BEM
    <div className="app">
      <Sidebar onCategorySelect={handleCategorySelect}  />
      <Feed category={selectedCategory} />
      {/* <Widgets /> */}
      {/* <RightPanel /> */}
    </div>
  );
}

export default App;
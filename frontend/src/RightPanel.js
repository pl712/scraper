import React, { useState, useEffect } from "react";
import TweetBox from "./TweetBox";
import Post from "./Post";
import "./RightPanel.css";
import TimeLine from "./TimeLine";

function Feed() {
  const [topic, setTopic] = useState([]);

  useEffect(() => {
    setTopic('general');
  }, []);

  return (
    <div className="feed">
      <div className="feed__header">
        <h2>TimeLine</h2>
      </div>
      <TimeLine topic={topic} />
    </div>
  );
}

export default Feed;

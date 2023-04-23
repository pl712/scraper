import React, { useState, useEffect } from "react";
import TweetBox from "./TweetBox";
import Post from "./Post";
import "./Feed.css";
import FlipMove from "react-flip-move";
import data from "./data/posts_with_labels.json";
import axios from 'axios'


function Feed({ category }) {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    setPosts([]);
    const filteredData = category ? data.filter((post) => post.label === category) : data;
    setPosts(filteredData);
  }, [category]);

  return (
    <div className="feed">
      <div className="feed__header">
        <h2>Filtered Tweets</h2>
      </div>

      <TweetBox />

      <FlipMove>
        {posts.map((post,index) => (
          <Post
            key={index}
            displayName={post.displayName}
            username={post.username}
            verified={post.verified}
            text={post.text}
            avatar={post.avatar}
            image={post.image}
            label={post.label}
          />
        ))}
      </FlipMove>
    </div>
  );
}

export default Feed;

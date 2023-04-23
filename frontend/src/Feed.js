import React, { useState, useEffect } from "react";
import TweetBox from "./TweetBox";
import Post from "./Post";
import "./Feed.css";
import FlipMove from "react-flip-move";
import data from "./data/posts.json";
import axios from 'axios'


function Feed() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    // axios.get('/getMessages/general-topic/0').then(response => {
    //   console.log("SUCCESS", response)
    //   setPosts(response)
    // }).catch(error => {
    //   console.log(error)
    // })
    setPosts(data.posts)
  }, []);

  return (
    <div className="feed">
      <div className="feed__header">
        <h2>Home</h2>
      </div>

      <TweetBox />

      <FlipMove>
        {posts.map((post) => (
          <Post
            key={post.text}
            displayName={post.displayName}
            username={post.username}
            verified={post.verified}
            text={post.text}
            avatar={post.avatar}
            image={post.image}
          />
        ))}
      </FlipMove>
    </div>
  );
}

export default Feed;

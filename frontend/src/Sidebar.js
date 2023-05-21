import React from "react";
import "./Sidebar.css";
import TwitterIcon from "@material-ui/icons/Twitter";
import SidebarOption from "./SidebarOption";
import HomeIcon from "@material-ui/icons/Home";
import SearchIcon from "@material-ui/icons/Search";
import NotificationsNoneIcon from "@material-ui/icons/NotificationsNone";
import MailOutlineIcon from "@material-ui/icons/MailOutline";
import BookmarkBorderIcon from "@material-ui/icons/BookmarkBorder";
import ListAltIcon from "@material-ui/icons/ListAlt";
import PermIdentityIcon from "@material-ui/icons/PermIdentity";
import MoreHorizIcon from "@material-ui/icons/MoreHoriz";
import { Button } from "@material-ui/core";

function Sidebar({ onCategorySelect }) {
  // 'web3 activities and events', 'web3 announcements', 'web3 research output', 
  // 'web3 meme', 'crypto and markets', 'web3 phishing or irrelevant', 'unknown'
  // function handleCategorySelect(category) {
  //   if (onCategorySelect) {
  //     onCategorySelect(category);
  //   }
  // }
  return (
    <div className="sidebar">
      <TwitterIcon className="sidebar__twitterIcon" />

      <SidebarOption active Icon={HomeIcon} text="All" onClick={() => onCategorySelect(null)} />
      <SidebarOption Icon={SearchIcon} text="web3 activities and events" onClick={() => onCategorySelect("web3 activities and events")} />
      <SidebarOption Icon={NotificationsNoneIcon} text="web3 announcements" onClick={() => onCategorySelect("Web3 Announcements")} />
      <SidebarOption Icon={MailOutlineIcon} text="web3 research output" onClick={() => onCategorySelect("Web3 Research Output")} />
      <SidebarOption Icon={BookmarkBorderIcon} text="web3 meme" onClick={() => onCategorySelect("Web3 meme")} />
      <SidebarOption Icon={ListAltIcon} text="crypto and markets" onClick={() => onCategorySelect("Crypto and Markets")} />
      <SidebarOption Icon={PermIdentityIcon} text="web3 phishing or irrelevant"   onClick={() => onCategorySelect("web3 phishing or irrelevant")} />
      <SidebarOption Icon={MoreHorizIcon} text="unknown"  onClick={() => onCategorySelect("Unknown")} />
    
      {/* Button -> Tweet */}
      <Button variant="outlined" className="sidebar__tweet" fullWidth>
        Tweet
      </Button>
    </div>
  );
}

export default Sidebar;

import Sidebar from "./Sidebar";
import Feed from "./Feed";
import Widgets from "./Widgets";
import RightPanel from "./RightPanel";
import "./App.css";
import React, { useEffect, useState } from 'react';
import Rightbar from "./Rightbar";
import { Dialog } from "@material-ui/core";
import DialogTitle from '@mui/material/DialogTitle';
import { TextField } from '@material-ui/core';


function addID(open){

  return(
    <Dialog open = {open}>
      <DialogTitle>This is the Dialog</DialogTitle>
    </Dialog>
  )
}



// function SimpleDialog(props) {
//   const { onClose, selectedValue, open } = props;

//   const handleClose = () => {
//     onClose(selectedValue);
//   };


//   return (
//     <Dialog onClose={handleClose} open={open}>
//       <DialogTitle>Set backup account</DialogTitle>
//     <Dialog/>
//     );
// }



export default function App() {
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [open, setOpen] = React.useState(false);
  const  [id, setid] = React.useState();
  const [fetched, setfetch] = React.useState(false)
  
  const handleId = (event)=>{
      console.log(fetched)
      setfetch(true)
  }

  const handlechange = (event)=>{
    setid(event.target.value)
  }
    
  const handleClickOpen = () => {
    setOpen(true);
    console.log(open)
  }; 
  function handleCategorySelect(category) {
    setSelectedCategory(category);
  }



  return (
    // BEM
    <div>
      <div className="loading" style={{display: fetched ? "block" : "none"}}>Loading ....</div>
      <div className="app">
        <Sidebar onCategorySelect={handleCategorySelect} />
        <Feed category={selectedCategory} />
        {/* <Widgets /> */}
        {/* <RightPanel /> */}
        <div className="right">
          {/* <Rightbar/> */}
          <div className='rightslide'>
              <div>
                    Please input your Twitter ID:
              </div>
              <div className='text'>
                  <TextField label="Twitter ID" variant="outlined" onChange={handlechange}/>
              </div>
              <button className='button' onClick={handleId}>Fetch</button>
          </div>
        </div>
      </div>
    </div>
    
    
   
  );
}


import Sidebar from "./Sidebar";
import Feed from "./Feed";
import Widgets from "./Widgets";
import RightPanel from "./RightPanel";
import "./App.css";
import React, { useState } from 'react';
import Rightbar from "./Rightbar";
import { Dialog } from "@material-ui/core";
import DialogTitle from '@mui/material/DialogTitle';


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
    
  const handleClickOpen = () => {
    setOpen(true);
    console.log(open)
  }; 
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
      <div className="right">
        <Rightbar/>
      </div>
      
    </div>
    
   
  );
}


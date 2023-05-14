import React, { useState } from 'react';
import { TextField } from '@material-ui/core';
import './rightslide.css'
function Rightbar(){
    const  [id, setid] = React.useState();
    const handleId = ()=>{
        console.log(id)
    }
    const handlechange = (event)=>{
        setid(event.target.value)
    }
    return(
        
            <div className='rightslide'>
                <div>
                    Please input your Twitter ID:
                </div>
                <div className='text'>
                    <TextField label="Twitter ID" variant="outlined" onChange={handlechange}/>
                </div>
                <button className='button' onClick={handleId}>Fetch</button>
            </div>
            
        
        
       
    )
}




export default Rightbar;
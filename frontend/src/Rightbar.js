import React, { useState, useEffect} from 'react';
import { TextField } from '@material-ui/core';
import './rightslide.css'
function Rightbar(){
    const  [id, setid] = React.useState();
    let fetched = false
    
    const handleId = (event)=>{
        console.log(fetched)
        fetched = true
        console.log("after :", fetched)
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
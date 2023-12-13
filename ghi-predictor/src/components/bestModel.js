import React, { useEffect, useState } from "react";
import axios from "axios";


export default function BestModel(){
    const [name, setName] = useState("")
    const [learning, setLearing] = useState(0.0)
    const [r2, setR2] = useState(0)
    const [rmse, setRmse] = useState(0)
    

    const callParams = async() =>{
        try{
            const response = await axios.get('http://localhost:8000/best_model');
            setName(response.data.name)
            setLearing(response.data.params)
            setR2(response.data.r2)
            setRmse(response.data.rmse)
              
        } catch (e) {
            
        }
    }

    useEffect(() => {
        callParams();
      }, []);

    return (
        <>
            <div>
                - The best model is: <b>{name}</b>
            </div>
            <div>
                - The learing rate is: <b>{learning['learning_rate']}</b>
            </div>
            <div>
                - The max Depth is: <b>{learning['max_depth']}</b>
            </div>
            <div>
                - The number of estimator used is: <b>{learning['n_estimators']}</b>
            </div>
            <div>
                - R2: <b>{r2}</b>
            </div>
            <div>
                - Rmse: <b>{rmse}</b>
            </div>
        </>
    );

}
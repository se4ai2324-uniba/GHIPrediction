import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import axios from "axios";
import React, { useState, useEffect } from "react";

import Grid from '@mui/material/Grid';


export default function Predictor(){

        const [temperature, setTemperature] = useState(0.0)
        const [dni, setDni] = useState(0.0)
        const [humidity, setHumidity] = useState(0.0)
        const [api, setApi] = useState(null);
    
        const callGhi = async() =>{
            try{
              const response = await axios.post(process.env.REACT_APP_API + '/prediction',{
                    "temperature": temperature,
                    "dni": dni,
                    "humidity":humidity}

                );
                setApi(response.data)
                  
            } catch (e) {
                setApi(null);
            }
        }

        const showData = () =>{
                alert(JSON.stringify(api));
              //   <Alert severity="success">
              //   <AlertTitle>Predetto</AlertTitle>
              //   Il ghi predetto è: <strong>{JSON.stringify(api)}</strong>
              // </Alert>
        }

        useEffect(() => {
            if (api != null){
                showData()
            }
          }, [api]);

        return (
            <>
             <Grid container spacing={2}>
             <Grid item xs={4}>
            <TextField
              label="Temperature"
              variant="outlined"
              fullWidth
              margin="normal"
              name="Temperature"
              value={temperature}
              onChange={(e) => {
                setTemperature(e.target.value);
            }}
            />
              </Grid>
             <Grid item xs={4}>
            <TextField
              label="Humidity"
              variant="outlined"
              fullWidth
              margin="normal"
              name="Humidity"
              value={humidity}
              onChange={(e) => {
                setHumidity(e.target.value);
            }}
            />
            </Grid>
            <Grid item xs={4}>
             <TextField
              label="Dni"
              variant="outlined"
              fullWidth
              margin="normal"
              name="Dni"
              value={dni}
              onChange={(e) => {
                setDni(e.target.value);
            }}
            />
            </Grid>
            </Grid>
            <Grid container spacing={2}>

            <Grid item xs={5.5}></Grid>
            <Grid item xs={6.5}>

            <Button
            sx={{ height: "100%", marginLeft: "10px" }}
            variant="contained"
            name="Predict"
            color='success'
            onClick={() => {
              callGhi();
            }}
          >
            Predict
            </Button>
            </Grid> 
            </Grid>
            </>
        );
      };     


      
      
      
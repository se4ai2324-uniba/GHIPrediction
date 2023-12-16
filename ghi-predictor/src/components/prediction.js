import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import axios from "axios";
import React, { useState, useEffect } from "react";
import BasicTable from './Table';
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';

export default function Predictor(){
        const [rows, setRows] = useState(localStorage.getItem('rows') ? JSON.parse(localStorage.getItem('rows')):[]);
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
                setRows(rows =>[...rows, {temperature: temperature, humidity: humidity, dni: dni, ghi:response.data.predicted_GHI}]);
                localStorage.setItem('rows', JSON.stringify([...rows, {temperature: temperature, humidity: humidity, dni: dni, ghi:response.data.predicted_GHI}]));

              } catch (e) {
                setApi(null);
            }
        }
        
        useEffect(() => {
          }, [api]);

        return (
            <>
            <Container maxWidth="lg">

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

            <Grid item xs={5}></Grid>
            <Grid item xs={6}>
            
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
            <Button
            sx={{ height: "100%", marginLeft: "10px" }}
            variant="contained"
            name="Predict"
            color='error'
            disabled={(rows.length>0) ? false : true}
            onClick={() => {
              localStorage.setItem('rows','[]');
              window.location.reload()
            }}
          >
            Reset
            </Button>
            </Grid> 
            </Grid>

            <BasicTable rows={rows}/>
            </Container>
            </>
        );
      };     


      
      
      
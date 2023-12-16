import React, { useEffect, useState } from "react";
import axios from "axios";
import Container from '@mui/material/Container';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

export default function BestModel(){
    const [name, setName] = useState("")
    const [learning, setLearing] = useState(0.0)
    const [r2, setR2] = useState(0)
    const [rmse, setRmse] = useState(0)
    

    const callParams = async() =>{
        try{
            const response = await axios.get(process.env.REACT_APP_API + '/best_model');
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
       <Container maxWidth="lg">
       <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Params</TableCell>
            <TableCell>Value</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
            <TableRow
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell>Best Model</TableCell>
              <TableCell>{name}</TableCell>
            </TableRow>
            <TableRow
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell>Learing Rate</TableCell>
              <TableCell>{learning['learning_rate']}</TableCell>
            </TableRow>
            <TableRow
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell>Max Depth</TableCell>
              <TableCell>{learning['max_depth']}</TableCell>
            </TableRow>
            <TableRow
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell>Estimators</TableCell>
              <TableCell>{learning['n_estimators']}</TableCell>
            </TableRow>
            <TableRow
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell>R2</TableCell>
              <TableCell>{r2}</TableCell>
            </TableRow>
            <TableRow
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell>Rmse</TableCell>
              <TableCell>{rmse}</TableCell>
            </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
            </Container>
        </>
    );

}
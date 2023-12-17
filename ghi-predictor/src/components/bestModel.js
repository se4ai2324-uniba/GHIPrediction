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
    const [tableData, setTableData] = useState([]);
    

    const callParams = async() =>{
        try{
            const response = await axios.get(process.env.REACT_APP_API + '/best_model');
            setName(response.data.name)
            const paramsArray = Object.entries(response.data.params).map(([key, value]) => ({ param: key, value }));
        
            setTableData(paramsArray);
            setR2(response.data.r2);
            setRmse(response.data.rmse);
              
        } catch (e) {
            
        }
    }

    useEffect(() => {
        callParams();
        console.log(tableData.keys)
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
              <TableRow>
                <TableCell>Name</TableCell>
                <TableCell>{name}</TableCell>
              </TableRow>
              {tableData.map((row, index) => (
                <TableRow key={index}>
                  <TableCell>{Object.values(row)[0]}</TableCell>
                  <TableCell>{Object.values(row)[1]}</TableCell>
                </TableRow>
              ))}
              <TableRow>
                <TableCell>R2</TableCell>
                <TableCell>{r2}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell>RMSE</TableCell>
                <TableCell>{rmse}</TableCell>
              </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
            </Container>
        </>
    );

}
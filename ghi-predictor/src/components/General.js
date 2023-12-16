import React, { useEffect, useState } from "react";
import axios from "axios";
import Container from '@mui/material/Container';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

export default function General(){
    const [params, setParams] = useState("")
    const [name, setName] = useState("")
    const [git, setGit] = useState("")
    const [contributors, setContributors] = useState([])

    const callParams = async() =>{
        try{
            const response = await axios.get(process.env.REACT_APP_API);
            setParams(response.data)
            setName(response.data.name)
            setGit(response.data.github)
            setContributors(response.data.contributors)
              
        } catch (e) {
            setParams("");
        }
    }

    useEffect(() => {
        callParams();
      }, []);

    return (
        <>
        <Container maxWidth="lg">

        <Grid container spacing={2}>
             <Grid item xs={4}>
                    <Card sx={{ minWidth: 275 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                The name of the project is: 
                </Typography>
                <Typography variant="body2">
                {name}
                </Typography>
            </CardContent>
            </Card>
            </Grid>
            <Grid item xs={4}>
            <Card sx={{ minWidth: 275 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                Github Repository:
                </Typography>
                <Typography variant="body2">
                {git}
                </Typography>
            </CardContent>
            <CardActions>
                <Button size="small" href={git}>Open link</Button>
            </CardActions>
            </Card>
            </Grid>
            <Grid item xs={4}>
            <Card sx={{ minWidth: 275 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                Contributors
                </Typography>
                <Typography variant="body2">
                <b>{contributors[0]}, {contributors[1]}, {contributors[2]}</b>
                </Typography>
            </CardContent>
            </Card>
            </Grid>
            </Grid>
            </Container>
        </>
    );

}
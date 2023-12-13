import React, { useEffect, useState } from "react";
import { Tab, Tabs } from "@mui/material";
import { useNavigate, useLocation } from "react-router-dom";

export default function TabNav() {
  const navigateTo = useNavigate();
  const location = useLocation();
  const [value, setValue] = useState(location.pathname);

  const handleChange = (e, newValue) => {
    console.log("NEW", newValue);
    navigateTo(newValue);
    setValue(newValue);
  };

  useEffect(() => {
    setValue(location.pathname)
  }, [location.pathname]);

  return (
    <div style={{ display: "flex", justifyContent: "space-evenly" }}>
      <Tabs
        aria-label="basic tabs example"
        onChange={handleChange}
        value={value}
      >
        <Tab label="General Informations" value="/" />
        <Tab label="Ghi Prediction" value="/prediction" />
        <Tab label="Best Model Params" value="/best_model" />
      </Tabs>
    </div>
  );
}
// import './App.css';
// import Predictor from '../src/components/prediction';
// function App() {
//   return <Predictor/>
// }

// export default App;


import {
  BrowserRouter as Router,
  Route,
  Link,
  Routes,
  Navigate,
} from "react-router-dom";
import Predictor from '../src/components/prediction';
import BestModel from '../src/components/bestModel';
import General from '../src/components/General';


import Tracker from "../src/components/Tracker";
function App() {
  return (
    <Router>
      <Tracker />
      <Routes>
        <Route path="/" element={<General />}></Route>
        <Route path="/best_model" element={<BestModel />}></Route>
        <Route path="/prediction" element={<Predictor />}></Route>
        <Route path="/" element={<Navigate to={"/"} />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
import Navbar from "../../navbar/Navbar";

import { Routes, Route } from "react-router-dom";
import LandingPage from "../pages/landing/LandingPage";
import Profile from "../pages/profile/Profile";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </div>
  );
}

export default App;

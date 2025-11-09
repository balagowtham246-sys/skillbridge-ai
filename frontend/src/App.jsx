import React from "react";
<<<<<<< HEAD
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { UserProvider } from "./contexts/UserContext";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Recommendations from "./pages/Recommendations";
import Profile from "./pages/Profile";
import "./config/api"; // Import API configuration

export default function App() {
  return (
    <Router>
      <UserProvider>
        <Navbar />
        <div className="min-h-screen bg-gray-50">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/recommendations" element={<Recommendations />} />
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </div>
      </UserProvider>
    </Router>
  );
}
=======
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import AIRecommend from "./pages/AIRecommend";
import Dashboard from "./pages/Dashboard";
import Profile from "./pages/Profile";

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<AIRecommend />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </>
  );
}

export default App;
>>>>>>> 686041933804193522e48a97c6023f7b2132512f

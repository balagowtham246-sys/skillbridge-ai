// frontend/src/pages/Home.jsx
import React from "react";
import { Link } from "react-router-dom";

const Home = () => (
  <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-slate-800 to-slate-900 text-white">
    <h1 className="text-4xl font-bold mb-4">SkillBridge AI</h1>
    <p className="mb-6">Bridge your skills. Build your future.</p>
    <Link to="/recommendations" className="bg-blue-600 px-4 py-2 rounded">
      Get Started
    </Link>
  </div>
);

export default Home;

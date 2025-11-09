import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  const user = JSON.parse(localStorage.getItem("user"));

  return (
    <nav className="flex justify-between items-center bg-blue-600 text-white px-6 py-3 shadow-md">
      <div className="text-2xl font-bold tracking-wide">SkillBridge AI</div>
      <div className="flex gap-6">
        <Link to="/" className="hover:underline">
          Home
        </Link>
        <Link to="/recommendations" className="hover:underline">
          Recommendations
        </Link>
        <Link to="/profile" className="hover:underline">
          Profile
        </Link>
      </div>
      {user ? (
        <div className="text-sm text-gray-100">
          👋 {user.name} | XP: {user.xp || 0}
        </div>
      ) : (
        <div className="text-sm italic text-gray-100">Guest</div>
      )}
    </nav>
  );
}

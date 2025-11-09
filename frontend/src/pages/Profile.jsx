<<<<<<< HEAD
// frontend/src/pages/Profile.jsx
import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../contexts/UserContext";

export default function Profile() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [isRegistering, setIsRegistering] = useState(false);
  const { user, login, register, logout: contextLogout } = useContext(UserContext);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isRegistering) {
      if (!name.trim() || !email.trim() || !password.trim()) {
        alert("Please fill in all fields!");
        return;
      }
      try {
        await register(name, email, password);
        navigate("/");
      } catch (error) {
        console.error("Registration error:", error);
        alert(error.response?.data?.detail || "Registration failed");
      }
    } else {
      if (!email.trim() || !password.trim()) {
        alert("Please fill in all fields!");
        return;
      }
      try {
        await login(email, password);
        navigate("/");
      } catch (error) {
        console.error("Login error:", error);
        alert(error.response?.data?.detail || "Login failed");
      }
    }
  };

  const logout = () => {
    localStorage.removeItem("user");
    localStorage.removeItem("token");
    setUser(null);
    setName("");
  };

  return (
    <div className="p-8 flex flex-col items-center justify-center min-h-[80vh] bg-gray-50">
      {!user ? (
        <div className="bg-white shadow-xl rounded-2xl p-8 w-96">
          <h2 className="text-2xl font-semibold mb-4 text-center text-gray-800">
            {isRegistering ? "Register" : "Login"}
          </h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            {isRegistering && (
              <input
                className="border border-gray-300 p-2 w-full rounded"
                placeholder="Enter your name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            )}
            <input
              type="email"
              className="border border-gray-300 p-2 w-full rounded"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <input
              type="password"
              className="border border-gray-300 p-2 w-full rounded"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button
              type="submit"
              className="bg-blue-600 text-white px-4 py-2 rounded w-full hover:bg-blue-700 transition"
            >
              {isRegistering ? "Register" : "Login"}
            </button>
          </form>
          <button
            onClick={() => setIsRegistering(!isRegistering)}
            className="mt-4 text-blue-600 hover:underline w-full text-center"
          >
            {isRegistering
              ? "Already have an account? Login"
              : "Don't have an account? Register"}
          </button>
        </div>
      ) : (
        <div className="bg-white shadow-xl rounded-2xl p-8 w-96 text-center">
          <h2 className="text-2xl font-bold text-gray-800 mb-2">👤 {user.name}</h2>
          <p className="text-gray-500 mb-3">Email: {user.email}</p>
          <button
            onClick={contextLogout}
            className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
          >
            Logout
          </button>
        </div>
      )}
=======
import React, { useState } from "react";
import { motion } from "framer-motion";

export default function Profile() {
  const [skills, setSkills] = useState(["Python", "HTML", "SQL"]);
  const [name] = useState("Kamal");
  const [email] = useState("kamal@example.com");

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-900 to-slate-800 text-white flex flex-col items-center pt-24 px-4">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="w-full max-w-2xl bg-slate-900/60 backdrop-blur-md border border-slate-700 rounded-2xl p-8 shadow-2xl"
      >
        <h2 className="text-3xl font-bold text-blue-400 mb-4 text-center">
          Profile
        </h2>

        <div className="space-y-3 text-gray-300">
          <p>
            👤 <span className="font-semibold text-white">{name}</span>
          </p>
          <p>
            📧 <span className="font-semibold text-white">{email}</span>
          </p>
        </div>

        <h3 className="text-lg font-semibold mt-6 mb-2 text-blue-300">
          Your Skills
        </h3>
        <div className="flex flex-wrap gap-2">
          {skills.map((skill, i) => (
            <span
              key={i}
              className="bg-blue-600/30 border border-blue-400/50 text-blue-200 px-3 py-1 rounded-full text-sm"
            >
              {skill}
            </span>
          ))}
        </div>

        <button
          onClick={() => alert("Feature coming soon 🚀")}
          className="mt-6 bg-gradient-to-r from-blue-500 to-indigo-500 hover:from-indigo-600 hover:to-purple-600 text-white py-2 px-6 rounded-xl transition-all duration-300 shadow-md hover:shadow-blue-500/30"
        >
          ✏️ Edit Profile
        </button>
      </motion.div>

      <footer className="text-gray-400 text-sm mt-10">
        © 2025 <span className="text-blue-400 font-semibold">Team QUADCORE</span> | IBM TechXchange Hackathon
      </footer>
>>>>>>> 686041933804193522e48a97c6023f7b2132512f
    </div>
  );
}

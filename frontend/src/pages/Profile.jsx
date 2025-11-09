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
    </div>
  );
}

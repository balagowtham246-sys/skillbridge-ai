import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';
import '../config/api';

export const UserContext = createContext();

export const useUser = () => useContext(UserContext);

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if we have a token
    const token = localStorage.getItem('token');
    if (token) {
      axios.get("/profile", {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then(res => setUser(res.data))
        .catch(() => {
          localStorage.removeItem('token');
          setUser(null);
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const login = async (email, password) => {
    try {
      const res = await axios.post("/login", { email, password });
      localStorage.setItem('token', res.data.access_token);
      setUser(res.data.user);
      return res.data.user;
    } catch (error) {
      console.error("Login error:", error.response?.data?.detail || error.message);
      throw error;
    }
  };

  const register = async (name, email, password) => {
    try {
      const res = await axios.post("/register", { name, email, password });
      localStorage.setItem('token', res.data.access_token);
      setUser(res.data.user);
      return res.data.user;
    } catch (error) {
      console.error("Registration error:", error.response?.data?.detail || error.message);
      throw error;
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  const value = {
    user,
    loading,
    login,
    register,
    logout
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
};

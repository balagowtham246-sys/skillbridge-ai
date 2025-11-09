<<<<<<< HEAD
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
=======
import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';

export default function Navbar() {
  const navItems = [
    { path: '/', label: 'Home' },
    { path: '/dashboard', label: 'Dashboard' },
    { path: '/profile', label: 'Profile' }
  ];

  return (
    <motion.nav 
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ type: "spring", stiffness: 100, damping: 15 }}
      className="p-4 bg-white shadow"
    >
      <div className="container mx-auto flex items-center justify-between">
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5, delay: 0.3 }}
          className="text-xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 text-transparent bg-clip-text"
        >
          SkillBridge
        </motion.div>
        <div className="space-x-4 text-sm">
          {navItems.map((item, i) => (
            <motion.span
              key={item.path}
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3, delay: 0.5 + i * 0.1 }}
            >
              <Link 
                to={item.path}
                className="text-gray-600 hover:text-blue-600 transition-colors"
              >
                <motion.span
                  whileHover={{ scale: 1.1 }}
                  whileTap={{ scale: 0.95 }}
                >
                  {item.label}
                </motion.span>
              </Link>
            </motion.span>
          ))}
        </div>
      </div>
    </motion.nav>
>>>>>>> 686041933804193522e48a97c6023f7b2132512f
  );
}

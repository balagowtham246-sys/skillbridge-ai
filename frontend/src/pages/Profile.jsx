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
    </div>
  );
}

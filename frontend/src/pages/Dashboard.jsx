import React from "react";
import { motion } from "framer-motion";

export default function Dashboard() {
  const recommendations = [
    { id: 1, title: "Machine Learning Foundations", duration: "3 months" },
    { id: 2, title: "Deep Learning Advanced", duration: "2 months" },
    { id: 3, title: "Data Visualization with Python", duration: "1 month" },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-900 to-slate-800 text-white flex flex-col items-center pt-24 px-4">
      <h2 className="text-3xl font-bold text-blue-400 mb-8">Your Dashboard</h2>

      <div className="w-full max-w-4xl bg-slate-900/60 backdrop-blur-md border border-slate-700 rounded-2xl p-8 shadow-2xl">
        <h3 className="text-xl font-semibold mb-4 text-center">
          Recommended Learning Tracks
        </h3>

        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="grid sm:grid-cols-2 md:grid-cols-3 gap-4"
        >
          {recommendations.map((rec) => (
            <div
              key={rec.id}
              className="bg-slate-800 border border-blue-500/30 p-5 rounded-xl shadow-md hover:shadow-blue-500/30 transition-all duration-300"
            >
              <h4 className="font-semibold text-blue-300">{rec.title}</h4>
              <p className="text-gray-400 text-sm mt-1">
                ⏱ Duration: {rec.duration}
              </p>
            </div>
          ))}
        </motion.div>
      </div>

      <footer className="text-gray-400 text-sm mt-10">
        © 2025 <span className="text-blue-400 font-semibold">Team QUADCORE</span> | IBM TechXchange Hackathon
      </footer>
    </div>
  );
}

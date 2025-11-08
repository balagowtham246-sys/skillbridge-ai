import React, { useState } from 'react';
import Loader from '../components/Loader';
import { generatePath } from '../services/api';
import { motion } from "framer-motion";

export default function AIRecommend(){
  const [goal, setGoal] = useState('');
  const [skills, setSkills] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function onSubmit(e){
    e.preventDefault();
    setLoading(true);
    try{
      const payload = { current_skills: skills.split(',').map(s=>s.trim()).filter(Boolean), goal_role: goal };
      const res = await generatePath(payload);
      setResult(res);
    }catch(err){
      console.error(err);
      alert('Error generating path');
    }finally{ setLoading(false); }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-slate-900 to-slate-800 text-white px-4 py-10">
      <div className="w-full max-w-3xl bg-slate-900/70 backdrop-blur-md rounded-2xl p-6 shadow-2xl">
        <h2 className="text-2xl font-bold mb-6 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-emerald-400">AI Learning Path Generator</h2>
        
        <motion.form 
          onSubmit={onSubmit} 
          className="space-y-6"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <motion.input
              type="text"
              className="w-full mb-3 p-3 rounded-xl text-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-400"
              placeholder="Enter skills (e.g. Python, HTML)"
              value={skills}
              onChange={(e) => setSkills(e.target.value)}
              whileFocus={{ scale: 1.02 }}
            />
          </motion.div>
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.3 }}
          >
            <motion.input
              type="text"
              className="w-full mb-3 p-3 rounded-xl text-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-400"
              placeholder="Enter career goal (e.g. Data Scientist)"
              value={goal}
              onChange={(e) => setGoal(e.target.value)}
              whileFocus={{ scale: 1.02 }}
            />
          </motion.div>
          <motion.div 
            className="flex justify-center"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
          >
            <motion.button
              type="submit"
              disabled={loading}
              className="bg-gradient-to-r from-blue-500 to-indigo-500 hover:from-indigo-500 hover:to-purple-500 text-white py-2 px-6 rounded-xl font-semibold flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              {loading ? 'Generating...' : '🚀 Generate Learning Path'}
            </motion.button>
          </motion.div>
        </motion.form>

        <div className="mt-8">
          {loading && (
            <div className="flex justify-center">
              <Loader />
            </div>
          )}
          
          {result && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
              className="space-y-6"
            >
              <motion.div 
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.5, delay: 0.2 }}
                className="bg-slate-800/50 rounded-lg p-6 border border-slate-700"
              >
                <h3 className="text-xl font-semibold mb-3 text-emerald-400">Career Path Summary</h3>
                <p className="text-gray-300 leading-relaxed">{result.summary}</p>
              </motion.div>
              
              {result.recommended_courses?.length > 0 && (
                <div className="mt-8 space-y-4">
                  <motion.h4 
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.5, delay: 0.4 }}
                    className="text-xl font-semibold mb-4 text-blue-400"
                  >
                    Recommended Learning Path
                  </motion.h4>
                  {result.recommended_courses.map((rec, index) => (
                    <motion.div
                      key={index}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ 
                        duration: 0.5,
                        delay: 0.6 + index * 0.2,
                        type: "spring",
                        stiffness: 100 
                      }}
                      whileHover={{ scale: 1.02 }}
                      className="bg-slate-800 border border-blue-500/30 rounded-xl p-5 shadow-md hover:shadow-lg"
                    >
                      <h3 className="text-lg font-bold text-blue-300">{rec.title}</h3>
                      <p className="text-gray-300 mt-1 italic">
                        ⏱ Duration: {rec.duration}
                      </p>
                      <div className="mt-2">
                        <span className="px-3 py-1 rounded-full text-xs font-medium bg-blue-500/20 text-blue-400">
                          {Math.round(rec.confidence * 100)}% Match
                        </span>
                      </div>
                    </motion.div>
                  ))}
                </div>
              )}
            </motion.div>
          )}
        </div>
      </div>
      <footer className="text-center text-gray-400 text-sm mt-10">
        © 2025 <span className="font-semibold text-blue-400">Team QUADCORE</span> | IBM TechXchange Hackathon
      </footer>
    </div>
  );
}

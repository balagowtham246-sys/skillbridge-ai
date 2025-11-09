import React, { useState } from "react";
import axios from "axios";
import { motion } from "framer-motion";

export default function Recommendations() {
  const [input, setInput] = useState("");
  const [recommendation, setRecommendation] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!input.trim()) return;
    setLoading(true);
    const res = await axios.get("/recommend", { params: { skill: input } });
    setRecommendation(res.data);
    setLoading(false);
  };

  return (
    <div className="p-8 text-center">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">🎯 AI Career Recommendation</h1>

      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter a skill (e.g. Python, React, ML)..."
        className="border w-1/2 p-3 rounded-lg"
      />
      <div>
        <button
          onClick={handleGenerate}
          disabled={loading}
          className="bg-blue-600 text-white px-4 py-2 rounded mt-3 hover:bg-blue-700 transition"
        >
          {loading ? "Generating..." : "Generate Learning Path"}
        </button>
      </div>

      {recommendation && (
        <motion.div
          className="mt-10 p-6 bg-white rounded-2xl shadow-lg text-left w-3/4 mx-auto"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="text-xl font-semibold text-blue-700 mb-3">
            Domain: {recommendation.domain}
          </h2>
          <p className="text-gray-600 mb-5">
            Here’s your customized learning path for <b>{recommendation.skill}</b>.
          </p>
          <ul className="list-disc ml-6">
            {recommendation.learning_path.map((step, idx) => (
              <li key={idx} className="mb-3">
                <a
                  href={step.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-600 font-medium hover:underline"
                >
                  {step.step}
                </a>
                <p className="text-gray-500 text-sm">{step.notes}</p>
              </li>
            ))}
          </ul>
        </motion.div>
      )}
    </div>
  );
}

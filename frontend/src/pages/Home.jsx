import "@fontsource/poppins";
import { useState } from "react";
import jsPDF from "jspdf";
import "jspdf-autotable";
import { generatePath } from '../services/api';

const downloadPDF = (result) => {
  const doc = new jsPDF();
  doc.setFont("helvetica", "bold");
  doc.setFontSize(18);
  doc.text("SkillBridge AI Learning Path", 20, 20);
  doc.setFontSize(12);
  doc.text(`Goal: ${result.goal}`, 20, 35);
  doc.text("Summary:", 20, 45);
  doc.text(result.summary, 20, 55, { maxWidth: 170 });

  const tableData = result.recommended_courses.map((c) => [c.title, c.duration]);
  doc.autoTable({
    head: [["Course Title", "Duration"]],
    body: tableData,
    startY: 80,
  });

  doc.save(`SkillBridge_${result.goal.replace(/\s+/g, "_")}.pdf`);
};

export default function Home() {
  const [skills, setSkills] = useState("");
  const [goal, setGoal] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleGenerate = async () => {
    if (!skills || !goal) {
      alert("Please enter both current skills and your target role!");
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const data = await generatePath({
        current_skills: skills.split(",").map((s) => s.trim()),
        goal_role: goal,
      });
      setResult(data);
    } catch (error) {
      console.error("Error fetching learning path:", error);
      alert("Could not reach backend. Make sure FastAPI is running!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-[#0f2027] via-[#203a43] to-[#2c5364] text-white font-[Poppins]">
      {/* Logo */}
      <div className="flex flex-col items-center mb-10">
        <img
          src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png"
          alt="SkillBridge Logo"
          className="w-24 h-24 animate-bounce"
        />
        <h1 className="text-5xl font-extrabold mt-3 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400 drop-shadow-lg">
          SkillBridge AI
        </h1>
        <p className="text-gray-300 italic mt-2">
          Bridge your skills. Build your future.
        </p>
      </div>

      {/* Form Section */}
      <div className="bg-white/10 backdrop-blur-lg p-8 rounded-2xl shadow-lg w-[90%] sm:w-[500px] flex flex-col gap-5">
        <input
          type="text"
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
          placeholder="💡 Current skills (e.g. Python, HTML, SQL)"
          className="w-full px-4 py-3 rounded-lg bg-gradient-to-r from-blue-500/10 via-purple-500/10 to-pink-500/10 border border-gray-400 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <input
          type="text"
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
          placeholder="🎯 Target role (e.g. Data Scientist)"
          className="w-full px-4 py-3 rounded-lg bg-gradient-to-r from-purple-500/10 via-pink-500/10 to-blue-500/10 border border-gray-400 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-purple-400"
        />

        <button
          onClick={handleGenerate}
          disabled={loading}
          className={`mt-4 w-full py-3 rounded-lg text-lg font-semibold bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 hover:scale-105 transition-all ${
            loading ? "opacity-60 cursor-wait" : ""
          }`}
        >
          {loading ? "Generating Path..." : "🚀 Generate Learning Path"}
        </button>
      </div>

      {/* Results Section */}
      {result && (
        <div className="mt-12 w-[90%] sm:w-[650px] text-center">
          <h2 className="text-3xl font-extrabold mb-6 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent drop-shadow-lg">
            🎯 Learning Path for {result.goal}
          </h2>

          {/* AI Summary */}
          <p className="text-gray-200 italic mb-8 leading-relaxed">
            {result.summary}
          </p>

          {/* Courses */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {result.recommended_courses.map((course, i) => (
              <div
                key={i}
                className="p-5 rounded-2xl bg-gradient-to-br from-indigo-600/20 to-purple-600/20 border border-indigo-400/40 
                          hover:from-indigo-500/30 hover:to-purple-500/30 
                          shadow-[0_0_20px_rgba(99,102,241,0.3)] transition-all duration-500 transform hover:-translate-y-1"
              >
                <h3 className="text-xl font-bold text-blue-300 mb-2">
                  {course.title}
                </h3>
                <p className="text-gray-200 text-sm">⏱ Duration: {course.duration}</p>
              </div>
            ))}
          </div>

          {/* Action Buttons */}
          <div className="mt-10 flex justify-center gap-4">
            <button
              onClick={() => setResult(null)}
              className="px-6 py-2 bg-gradient-to-r from-pink-500 to-purple-500 rounded-full text-white font-semibold hover:scale-105 hover:shadow-[0_0_20px_rgba(236,72,153,0.6)] transition"
            >
              🔄 New Search
            </button>
            <button
              onClick={() => downloadPDF(result)}
              className="px-6 py-2 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full text-white font-semibold hover:scale-105 hover:shadow-[0_0_20px_rgba(59,130,246,0.6)] transition"
            >
              📄 Download PDF
            </button>
          </div>
        </div>
      )}

      <footer className="mt-10 text-sm text-gray-400">
        © 2025 Team QUADCORE | IBM TechXchange Hackathon
      </footer>
    </div>
  );
}

import "@fontsource/poppins";
import { Link } from "react-router-dom";

const teamMembers = [
  {
    name: "Bala Gowtham",
    role: "Team Lead & AI Developer",
    github: "https://github.com/balagowtham246-sys",
  },
  {
    name: "Ruby",
    role: "Frontend Developer",
    github: "#",
  },
  {
    name: "Kiruthic",
    role: "Backend Engineer",
    github: "#",
  },
  {
    name: "Mirdhula",
    role: "UI/UX Designer",
    github: "#",
  },
  {
    name: "Kamal",
    role: "AI/Integration Specialist",
    github: "#",
  },
  {
    name: "Sreenithi",
    role: "Data Analyst",
    github: "#",
  },
];

function Team() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-[#1a2a6c] via-[#b21f1f] to-[#fdbb2d] flex flex-col items-center justify-center text-white font-[Poppins]">
      <h1 className="text-5xl font-extrabold mb-10 drop-shadow-[0_0_25px_rgba(255,255,255,0.3)]">
        Team QUADCORE ⚡
      </h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-[90%] sm:w-[800px]">
        {teamMembers.map((member, i) => (
          <div
            key={i}
            className="p-6 bg-white/10 backdrop-blur-lg border border-white/20 rounded-2xl text-center shadow-[0_0_25px_rgba(255,255,255,0.3)] hover:scale-105 transition"
          >
            <h2 className="text-2xl font-bold text-yellow-300 mb-2">
              {member.name}
            </h2>
            <p className="text-gray-200 mb-4">{member.role}</p>
            <a
              href={member.github}
              target="_blank"
              className="text-blue-400 hover:text-blue-500 underline"
            >
              GitHub
            </a>
          </div>
        ))}
      </div>

      <Link
        to="/"
        className="mt-12 px-6 py-3 bg-gradient-to-r from-purple-500 to-blue-500 rounded-full font-semibold text-white hover:scale-105 hover:shadow-[0_0_20px_rgba(59,130,246,0.5)] transition"
      >
        🏠 Back to SkillBridge
      </Link>

      <footer className="absolute bottom-5 text-sm text-gray-300">
        © 2025 Team QUADCORE | IBM TechXchange Hackathon
      </footer>
    </div>
  );
}

export default Team;

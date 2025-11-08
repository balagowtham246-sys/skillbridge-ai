import "@fontsource/poppins";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";

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
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.6 }}
      className="min-h-screen bg-gradient-to-br from-[#1a2a6c] via-[#b21f1f] to-[#fdbb2d] flex flex-col items-center justify-center text-white font-[Poppins]"
    >
      <motion.h1 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.3 }}
        className="text-5xl font-extrabold mb-10 drop-shadow-[0_0_25px_rgba(255,255,255,0.3)]"
      >
        Team QUADCORE ⚡
      </motion.h1>

      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.5 }}
        className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-[90%] sm:w-[800px]"
      >
        {teamMembers.map((member, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ 
              duration: 0.5, 
              delay: 0.7 + i * 0.1,
              type: "spring",
              stiffness: 100
            }}
            whileHover={{ 
              scale: 1.05,
              boxShadow: "0 0 30px rgba(255,255,255,0.4)"
            }}
            className="p-6 bg-white/10 backdrop-blur-lg border border-white/20 rounded-2xl text-center shadow-[0_0_25px_rgba(255,255,255,0.3)]"
          >
            <motion.h2 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.3, delay: 0.8 + i * 0.1 }}
              className="text-2xl font-bold text-yellow-300 mb-2"
            >
              {member.name}
            </motion.h2>
            <motion.p 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.3, delay: 0.9 + i * 0.1 }}
              className="text-gray-200 mb-4"
            >
              {member.role}
            </motion.p>
            <motion.a
              href={member.github}
              target="_blank"
              whileHover={{ scale: 1.1, color: "#60A5FA" }}
              className="text-blue-400 hover:text-blue-500 underline inline-block"
            >
              GitHub
            </motion.a>
          </motion.div>
        ))}
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 1.2 }}
      >
        <motion.div
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          <Link
            to="/"
            className="mt-12 px-6 py-3 bg-gradient-to-r from-purple-500 to-blue-500 rounded-full font-semibold text-white hover:shadow-[0_0_20px_rgba(59,130,246,0.5)] inline-block"
          >
            🏠 Back to SkillBridge
          </Link>
        </motion.div>
      </motion.div>

      <motion.footer 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.6, delay: 1.4 }}
        className="absolute bottom-5 text-sm text-gray-300"
      >
        © 2025 Team QUADCORE | IBM TechXchange Hackathon
      </motion.footer>
    </motion.div>
  );
}

export default Team;

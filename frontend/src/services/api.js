import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
});

// Mock data for development
const mockData = {
  skills: [
    { id: 1, name: "Python", level: "Advanced" },
    { id: 2, name: "Machine Learning", level: "Intermediate" },
    { id: 3, name: "Data Analysis", level: "Advanced" },
  ],
  recommendations: {
    jobs: [
      {
        id: 1,
        title: "Data Scientist",
        company: "Tech Corp",
        confidence: 0.92,
        skills: ["Python", "Machine Learning", "Statistics"],
      },
      {
        id: 2,
        title: "ML Engineer",
        company: "AI Solutions",
        confidence: 0.88,
        skills: ["Python", "Deep Learning", "TensorFlow"],
      },
    ],
    courses: [
      {
        id: 1,
        title: "Advanced Deep Learning",
        platform: "Coursera",
        confidence: 0.95,
        duration: "3 months",
      },
      {
        id: 2,
        title: "Natural Language Processing",
        platform: "edX",
        confidence: 0.85,
        duration: "2 months",
      },
    ],
  },
};

export const generatePath = async (skills) => {
  try {
    const res = await API.post("/generate_path", { skills });
    return res.data;
  } catch (error) {
    console.warn("Using mock data for generatePath");
    // support both call styles: array of skill strings or object { current_skills, goal_role }
    const payload = Array.isArray(skills)
      ? { current_skills: skills, goal_role: "Data Scientist" }
      : skills || { current_skills: [], goal_role: "Data Scientist" };

    return {
      goal: payload.goal_role || "Data Scientist",
      summary: `Based on your skills (${(payload.current_skills || []).join(", ")}), we recommend the following learning path to reach the ${payload.goal_role || "Data Scientist"} role. Start with core courses and progress to applied projects.`,
      recommended_courses: mockData.recommendations.courses,
      recommended_jobs: mockData.recommendations.jobs,
    };
  }
};

export const getAnalytics = async () => {
  try {
    const res = await API.get("/analytics");
    return res.data;
  } catch (error) {
    console.warn("Using mock data for analytics");
    return {
      totalUsers: 1250,
      activeUsers: 890,
      averageConfidence: 0.87,
    };
  }
};

export const getUserSkills = async () => {
  try {
    const response = await API.get("/user/skills");
    return response.data;
  } catch (error) {
    console.warn("Using mock data for user skills");
    return mockData.skills;
  }
};

export const checkHealth = async () => {
  try {
    const res = await API.get("/health");
    return res.data;
  } catch (error) {
    return { status: "Mock OK" };
  }
};

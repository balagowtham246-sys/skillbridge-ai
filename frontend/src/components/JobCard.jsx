import React from 'react';

export default function JobCard({ title, company, skills = [] }) {
  return (
    <div className="border rounded p-4 shadow-sm bg-white">
      <h3 className="font-semibold text-lg">{title}</h3>
      <p className="text-sm text-gray-600">{company}</p>
      <div className="mt-3 flex flex-wrap gap-2">
        {skills.map((s, i) => (
          <span key={i} className="text-xs px-2 py-1 bg-gray-100 rounded">{s}</span>
        ))}
      </div>
    </div>
  );
}

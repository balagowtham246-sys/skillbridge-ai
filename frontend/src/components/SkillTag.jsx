import React from 'react';

export default function SkillTag({ text }) {
  return (
    <span className="inline-block bg-blue-50 text-blue-800 text-xs px-2 py-1 rounded">
      {text}
    </span>
  );
}

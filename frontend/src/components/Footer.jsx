import React from 'react';

export default function Footer() {
  return (
    <footer className="p-4 bg-gray-100 mt-8">
      <div className="container mx-auto text-center text-sm text-gray-600">
        © {new Date().getFullYear()} SkillBridge — Built with ❤️
      </div>
    </footer>
  );
}

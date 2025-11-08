import React from 'react';
import { motion } from 'framer-motion';

export default function Loader() {
  const loadingVariants = {
    initial: { rotate: 0 },
    animate: { 
      rotate: 360,
      transition: {
        duration: 1,
        repeat: Infinity,
        ease: "linear"
      }
    }
  };

  const pulseVariants = {
    initial: { scale: 0.8, opacity: 0.5 },
    animate: {
      scale: 1.2,
      opacity: 1,
      transition: {
        duration: 0.8,
        repeat: Infinity,
        repeatType: "reverse",
        ease: "easeInOut"
      }
    }
  };

  return (
    <div className="flex items-center justify-center p-4">
      <motion.div
        initial="initial"
        animate="animate"
        variants={pulseVariants}
        className="relative"
      >
        <motion.div
          initial="initial"
          animate="animate"
          variants={loadingVariants}
          className="w-12 h-12 border-4 border-blue-500 rounded-full border-t-transparent"
        />
      </motion.div>
    </div>
  );
}

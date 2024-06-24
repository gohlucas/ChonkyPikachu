import { useState } from "react";

interface OutputProps {
  imageUrls: string[];
  description: string[];
}
const OutputHandler: React.FC<OutputProps> = ({ imageUrls, description }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const nextImage = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % imageUrls.length);
  };

  const prevImage = () => {
    setCurrentIndex(
      (prevIndex) => (prevIndex - 1 + imageUrls.length) % imageUrls.length
    );
  };

  return (
    <div>
      <img
        src={imageUrls[currentIndex]}
        alt={`Image ${currentIndex + 1}`}
        style={{ width: "100%", height: "auto" }}
      />
      <p>{description[currentIndex]}</p>
      <div>
        <button onClick={prevImage} disabled={currentIndex === 0}>
          Back
        </button>
        <button
          onClick={nextImage}
          disabled={currentIndex === imageUrls.length - 1}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default OutputHandler;

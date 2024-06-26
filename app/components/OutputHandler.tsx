import { useState } from "react";

// declare type of variables
interface OutputProps {
  imageUrls: string[];
  description: string[];
}

// code to allow backward navigation in addition to the normal
// "click next" functionality
const OutputHandler: React.FC<OutputProps> = ({ imageUrls, description }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const nextImage = () => {
    setCurrentIndex((previousIndex) => (previousIndex + 1) % imageUrls.length);
  };

  const prevImage = () => {
    setCurrentIndex(
      (previousIndex) =>
        (previousIndex - 1 + imageUrls.length) % imageUrls.length
    );
  };

  return (
    <div>
      <img
        src={imageUrls[currentIndex]}
        alt={"error, image could not load"}
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

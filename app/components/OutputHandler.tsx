import { useState } from "react";
import "./submitbutton.css";

// declare type of variables
interface OutputProps {
  imageUrls: string[];
  description: string[];
}

// code to allow backward navigation in addition to the normal
// "click next" functionality
const OutputHandler: React.FC<OutputProps> = ({ imageUrls, description }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const handleRefresh = () => {
    window.location.href = "/intro";
  };

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
    <div className="container">
      <div className="output-container">
        <div className="sub-container">
          <p className="text-output">{description[currentIndex]}</p>
        </div>
        <div className="sub-container2">
          <img
            src={`images/${imageUrls[currentIndex]}`}
            alt={"error, image could not load"}
            className="image-output"
          />
        </div>

        <div className="sub-container3">
          <button onClick={prevImage} disabled={currentIndex === 0}>
            Previous
          </button>
        </div>
        <div className="sub-container4">
          <button
            onClick={nextImage}
            disabled={currentIndex === imageUrls.length - 1}
          >
            Next
          </button>
        </div>

        <button onClick={handleRefresh}>
          Click here to head back to Start Page
        </button>
      </div>
    </div>
  );
};

export default OutputHandler;

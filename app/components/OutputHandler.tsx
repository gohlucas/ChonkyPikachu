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
      <div className="test-overall-container">
        <div className="test-container">
          <p className="text-output">{description[currentIndex]}</p>
          <button
            className="prev-item"
            onClick={prevImage}
            disabled={currentIndex === 0}
          ></button>
        </div>
        <div className="test-container2">
          <img
            src={imageUrls[currentIndex]}
            alt={"error, image could not load"}
            className="image-output"
          />
          <button
            className="next-item"
            onClick={nextImage}
            disabled={currentIndex === imageUrls.length - 1}
          ></button>
        </div>
      </div>
    </div>
  );
};

export default OutputHandler;

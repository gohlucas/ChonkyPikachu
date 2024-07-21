import React from "react";
import Link from "next/link";
import ToOutput from "../components/ToOutput";

//Functional component on homepage to bring users to the next page
const Home: React.FC = () => {
  return (
    <main>
      <header>
        <ToOutput />
      </header>
    </main>
  );
};

export default Home;

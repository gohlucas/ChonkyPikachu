import React from "react";
import Link from "next/link";
import ModLocation from "../components/ModLocation";
// import "./IntroPage.css";

//Functional component on homepage to bring users to the next page
const Home: React.FC = () => {
  return (
    <main>
      <header>
        <div>
          <ModLocation />
          <Link href="/intro">
            <button> Click Here to head back to Start Page</button>
          </Link>
        </div>
      </header>
    </main>
  );
};

export default Home;

import React from "react";
import Link from "next/link";
import "./IntroPage.css";

//Functional component on homepage to bring users to the next page
const Home: React.FC = () => {
  return (
    <main>
      <header>
        <div style={{ fontSize: "30px" }}>
          <Link href="/users">
            <button className="button"></button>
          </Link>
          <Link href="/modStuff">
            <button>Click Here for Mod Stuff</button>
          </Link>
        </div>
      </header>
    </main>
  );
};

export default Home;

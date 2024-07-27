import React from "react";
import Link from "next/link";
import Head from "next/head"; // Import Head from Next.js to include external resources
import "bootstrap/dist/css/bootstrap.min.css"; // Import Bootstrap CSS
import "./styles.css"; // Import your custom CSS file

const Home: React.FC = () => {
  return (
    <>
      <Head>
        <link
          href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap"
          rel="stylesheet"
        />
      </Head>
      <div className="container-fluid d-flex flex-column align-items-center justify-content-center vh-100 bg-light background">
        <div className="card p-5 card-custom">
          <h1 className="mb-4 text-center custom-color custom-font">
            Welcome to ConveNUS, an indoor navigation application currently
            based on COM1
          </h1>
          <p className="lead mb-4 text-center custom-font lead-custom">
            Choose one of the options below!
          </p>
          <div className="d-flex justify-content-center">
            <Link href="/users">
              <button className="btn btn-custom mx-2 button-text-color">
                Click Here for Navigation
              </button>
            </Link>
            <Link href="/modStuff">
              <button className="btn btn-custom mx-2 button-text-color">
                Click Here for Mod Stuff
              </button>
            </Link>
            <Link href="/3DModelPage">
              <button className="btn btn-custom mx-2 button-text-color">
                Click Here for 3D Models
              </button>
            </Link>
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;

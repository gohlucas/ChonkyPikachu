import React from 'react';
import Link from 'next/link';
import './IntroPage.css';

const Home: React.FC = () => {
    return (
        <main>
            <header>
            <h1>Cannot find the room you are looking for? Use conveNUS!</h1>
            </header>
            <div style={{ fontSize: '30px' }}>
        <Link href="/users">
          <button className="button">Click Here</button>
        </Link>
      </div>
        </main>
    );
}

export default Home;
import React from 'react';
import Link from 'next/link';
import './IntroPage.css';

const Home: React.FC = () => {
    return (
        <main>
            <header>
            <div style={{ fontSize: '30px' }}>
        <Link href="/users">
          <button className="button"></button>
        </Link>
      </div>
            </header>
            
        </main>
    );
}

export default Home;
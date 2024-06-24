import React from 'react';
import Link from 'next/link';
import './IntroPage.css'; //Styling

const Home: React.FC = () => { //A functional component on the page
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
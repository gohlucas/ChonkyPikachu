import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <main>
      <h1>
        Welcome to ConveNUS, a web app to find your way around NUS. Pika...
        Pika... Pika...chuuuu!
      </h1>
      <h2>Styling and Beautification in progress...</h2>
      <img
        src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/88c4706a-565c-4f0a-acfc-b914df984541/dcbxe9t-25e1fa87-9e5d-49bd-b085-c0c7075d12d5.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzg4YzQ3MDZhLTU2NWMtNGYwYS1hY2ZjLWI5MTRkZjk4NDU0MVwvZGNieGU5dC0yNWUxZmE4Ny05ZTVkLTQ5YmQtYjA4NS1jMGM3MDc1ZDEyZDUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.qfko0yYu_E3cH4TuO0GNA3d8MM0l_fNleb_3P84vqus"
        alt="Image not Loading"
      ></img>
      <Link href="/users">Click Here</Link>
    </main>
  );
}

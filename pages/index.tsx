import Link from "next/link"

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-dark-900">
      <h1 className="text-4xl font-bold mb-12">Welcome to FirePlay</h1>
      <div className="flex flex-col gap-8 w-full max-w-md">
        <a
          href ="http://localhost:5001/"
          rel="noopener noreferrer"
          className="block bg-blue-800 hover:bg-blue-700 text-white text-center py-6 rounded-lg shadow-lg text-2xl font-semibold transition"
        >
          Movie Suggestion Through Mood
        </a>
        <Link
          href="/watchparty"
          className="block bg-green-800 hover:bg-green-700 text-white text-center py-6 rounded-lg shadow-lg text-2xl font-semibold transition"
        >
          Watch Party
        </Link>
      </div>
    </div>
  )
}
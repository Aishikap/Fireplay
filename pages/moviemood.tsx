import { useState } from "react"

export default function MovieMood() {
  const [emotions, setEmotions] = useState<string[]>([])
  const [input, setInput] = useState("")
  const [movies, setMovies] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  const handleAddEmotion = () => {
    if (input && !emotions.includes(input)) {
      setEmotions([...emotions, input])
      setInput("")
    }
  }

  const handleSubmit = async () => {
    setLoading(true)
    const res = await fetch("http://localhost:5001/suggest", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ emotions }),
    })
    const data = await res.json()
    setMovies(data.movies)
    setLoading(false)
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-dark-900">
      <h1 className="text-3xl mb-4">Movie Suggestion Through Mood</h1>
      <div className="flex gap-2 mb-4">
        <input
          className="border px-2 py-1 rounded"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Enter emotion (e.g. happy, sad)"
        />
        <button
          type="button"
          className="bg-blue-700 text-white px-4 py-1 rounded"
          onClick={handleAddEmotion}
        >
          Add
        </button>
      </div>
      <div className="mb-4">
        {emotions.map(e => (
          <span key={e} className="bg-blue-200 px-2 py-1 rounded mr-2">{e}</span>
        ))}
      </div>
      <button
        className="bg-green-700 text-white px-6 py-2 rounded mb-6"
        onClick={handleSubmit}
        disabled={emotions.length === 0 || loading}
      >
        {loading ? "Loading..." : "Get Suggestions"}
      </button>
      {movies && (
        <div className="w-full max-w-xl bg-white rounded shadow p-4">
          <h2 className="text-xl mb-2">Suggestions:</h2>
          <ul>
            {Object.entries(movies).map(([title, summary]: any) => (
              <li key={title} className="mb-2">
                <strong>{title}</strong>
                <div className="text-sm text-gray-700">{summary[0]}</div>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}
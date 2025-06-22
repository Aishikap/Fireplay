import Layout from "../../components/Layout"
import { useState } from "react"
import InputText from "../../components/input/InputText"
import Button from "../../components/action/Button"
import { useRouter } from "next/router"
import { Tooltip } from "react-tooltip"
import useSWR from "swr"


export default function Index() {
  const router = useRouter()
  const { data } = useSWR("/api/stats", (url) =>
    fetch(url).then((r) => r.json())
  )
  const [room, setRoom] = useState("")

  return (
    <Layout meta={{ robots: "index, archive, follow" }} showNavbar={false}>
      <div
        className="flex items-center justify-center min-h-screen w-full"
      >
        <form
          className={
            "flex flex-col gap-4 justify-center rounded shadow p-12 bg-dark-900 m-8 w-[1000px] min-h-[300px]"
          }
          onSubmit={async (e) => {
            e.preventDefault()
            if (room.length >= 4) {
              await router.push("/watchparty/room/" + room)
            }
          }}
        >
          <h1 className={"text-3xl"}>Got invited?</h1>
          <div className="h-10">
            <InputText
              value={room}
              placeholder="Enter a room ID"
              onChange={(value) =>
                setRoom(value.toLowerCase().replace(/[^a-z]/g, ""))
              }
              className="h-full text-base px-2 py-1"
            />
          </div>
          <div className={"flex gap-2 justify-end"}>
            <Button
              tooltip={"Create a new personal room"}
              className={"p-2"}
              actionClasses={
                "bg-blue-900 hover:bg-blue-800 active:bg-blue-700"
              }
              onClick={() => {
                fetch("/api/generate")
                  .then((r) => r.json())
                  .then(async ({ roomId }) => {
                    if (
                      typeof roomId === "string" &&
                      roomId.length >= 4 &&
                      roomId.match(/^[a-z]{4,}$/)
                    ) {
                      console.log("Generated new roomId:", roomId)
                      await router.push("/watchparty/room/" + roomId)
                    } else {
                      throw Error("Invalid roomId generated: " + roomId)
                    }
                  })
                  .catch((error) => {
                    console.error("Failed to generate new roomId", error)
                  })
              }}
            >
              Generate room
            </Button>
            <Button
              tooltip={room.length < 4 ? "Invalid room id" : "Join room"}
              className={"p-2"}
              actionClasses={
                room.length >= 4
                  ? "bg-blue-900 hover:bg-blue-800 active:bg-blue-700"
                  : "bg-dark-700 hover:bg-dark-600 active:bg-red-700 cursor-not-allowed"
              }
              disabled={room.length < 4}
              type={"submit"}
            >
              Join room
            </Button>
          </div>
          <small className={"text-neutral-600"}>
            <div>Currently connected:</div>
            <div className={"flex flex-row gap-2"}>
              <div>Rooms: {data?.rooms || 0}</div>
              <div>Users: {data?.users || 0}</div>
            </div>
          </small>
        </form>
      </div>

      <Tooltip
        style={{
          backgroundColor: "var(--dark-700)",
        }}
      />
    </Layout>
  )
}

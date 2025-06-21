import { FC } from "react"
import IconClipboard from "../icon/IconClipboard"

interface Props {
  value: string
  className?: string
}

const InputClipboardCopy: FC<Props> = ({ value, className }) => {
  return (
    <div
      className={"rounded flex flex-row items-center bg-dark-900 " + className}
    >
      <input
        className={"rounded grow bg-dark-900 p-2 " + className}
        value={value}
        type={"text"}
        readOnly={true}
        onClick={(event) => {
          const target = event.target as HTMLInputElement
          target.select()
        }}
      />
      <button
        className={
          "p-2 bg-blue-900 hover:bg-blue-800 active:bg-blue-700 flex flex-row items-center rounded-r cursor-copy"
        }
        data-tooltip-content={"Click to copy"}
        type={"button"}
        onClick={() => {
          navigator.clipboard
            .writeText(value)
            .then(() => {})
            .catch((error) => {
              console.error("Failed to copy", error)
            })
        }}
      >
        <IconClipboard /> Copy
      </button>
    </div>
  )
}

export default InputClipboardCopy

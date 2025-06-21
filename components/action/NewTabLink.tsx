import { FC, ReactNode } from "react"
import classNames from "classnames"

interface Props {
  href: string
  className?: string
  children?: ReactNode
}

const NewTabLink: FC<Props> = ({ href, children, className }) => {
  return (
    <a
      href={href}
      className={classNames(
        "mx-1 transition-colors hover:text--blue900",
        className
      )}
      target={"_blank"}
      rel={"noreferrer"}
    >
      {children}
    </a>
  )
}

export default NewTabLink

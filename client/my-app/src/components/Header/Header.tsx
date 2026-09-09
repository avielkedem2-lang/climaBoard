import { Link } from "react-router";
import "./header.css"

export default function Header() {
  return (
    <div className="header">
        <Link to={"/dashboard"}><button className="but-header">Home</button></Link>
        <Link to={"search"}><button className="but-header">Search</button></Link>
        <Link to={"favorites"}><button className="but-header">favorites</button></Link>
    </div>
  )
}

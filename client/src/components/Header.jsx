import NavBar from "../components/Navbar"

export default function Header() {
  return (
    <header>
      <div className="logo-div">
        <h1 className="logo">EasyTax!</h1>
        <hr />
      </div>
      <NavBar />
      <div className="hamburger-menu">
        <div className="bar"></div>
        <div className="bar"></div>
        <div className="bar"></div>
      </div>
    </header>
  );
}

import "bootstrap/dist/css/bootstrap.min.css";
import logo from "./logo.svg";
import "./App.css";
import ChartComponent from "./Components/ChartComponent";
import NavbarComponent from "./Components/MyNavbar";

function App() {
  return (
    <>
    <NavbarComponent />
      <ChartComponent />
    </>
  );
}

export default App;

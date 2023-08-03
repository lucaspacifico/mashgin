import { Container } from "react-bootstrap";
import { Route, Routes, useLocation } from "react-router-dom";
import { Navbar } from "./components/Navbar";
import { ShoppingCartProvider } from "./context/ShoppingCartContext";
import { Orders } from "./pages/Orders";
import { Store } from "./pages/Store";

function App() {
  const location = useLocation();

  return (
    <ShoppingCartProvider>
      <Navbar />
      <Container className="mb-4">
        <Routes>
          <Route path="/" element={<Store />} />
          <Route path="/orders" element={<Orders />} />
        </Routes>
      </Container>
    </ShoppingCartProvider>
  );
}

export default App;

import { useEffect } from "react";
import { Container } from "react-bootstrap";
import { Route, Routes, useLocation } from "react-router-dom";
import { Navbar } from "./components/Navbar";
import {
  ShoppingCartProvider,
  useShoppingCart,
} from "./context/ShoppingCartContext";
import { Orders } from "./pages/Orders";
import { Store } from "./pages/Store";

function App() {
  const location = useLocation();

  // Access the ShoppingCartContext and call the resetCart function when the location changes
  const shoppingCartContext = useShoppingCart();
  useEffect(() => {
    if (location.pathname === "/orders") {
      shoppingCartContext.resetCart;
    }
  }, [location.pathname, shoppingCartContext]);

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

import { useState } from "react";
import { Button, Offcanvas, Stack } from "react-bootstrap";
import { useShoppingCart } from "../context/ShoppingCartContext";
import storeItems from "../data/items.json";
import { PaymentEntity } from "../types/types";
import { formatCurrency } from "../utilities/formatCurrency";
import { CartItem } from "./CartItem";
import PaymentFormModal from "./PaymentFormModal";

type ShoppingCartProps = {
  isOpen: boolean;
};

export function ShoppingCart({ isOpen }: ShoppingCartProps) {
  const handleCheckout = () => {
    setShowPaymentModal(true);
  };

  const handlePaymentSubmit = (payment: PaymentEntity) => {
    // Perform actions with the payment data, e.g., process the payment
    console.log("Payment data:", payment);
    setShowPaymentModal(false);
  };

  const { closeCart, cartItems } = useShoppingCart();
  const [showPaymentModal, setShowPaymentModal] = useState(false);
  const totalValue = cartItems.reduce(
    (total, cartItem) => total + cartItem.original_price * cartItem.quantity,
    0
  );

  return (
    <Offcanvas show={isOpen} onHide={closeCart} placement="end">
      <Offcanvas.Header closeButton>
        <Offcanvas.Title>Cart</Offcanvas.Title>
      </Offcanvas.Header>
      <Offcanvas.Body>
        <Stack gap={3}>
          {cartItems.map((item) => (
            <CartItem key={item.id} {...item} />
          ))}
          <div className="ms-auto fw-bold fs-5">
            Total{" "}
            {formatCurrency(
              cartItems.reduce((total, cartItem) => {
                const item = storeItems.find((i) => i.id === cartItem.id);
                return total + (item?.price || 0) * cartItem.quantity;
              }, 0)
            )}
          </div>
        </Stack>
      </Offcanvas.Body>
      <Button variant="primary" onClick={handleCheckout}>
        Checkout
      </Button>
      <PaymentFormModal
        show={showPaymentModal}
        onHide={() => setShowPaymentModal(false)}
        onSubmit={handlePaymentSubmit}
        total_value={totalValue}
      />
    </Offcanvas>
  );
}

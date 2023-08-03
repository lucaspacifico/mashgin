import { useState } from "react";
import { Button, Modal, Offcanvas, Stack } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { createOrder } from "../api/api";
import { useShoppingCart } from "../context/ShoppingCartContext";
import storeItems from "../data/items.json";
import SuccessPage from "../pages/SuccessPage";
import { PaymentEntity } from "../types/types";
import { formatCurrency } from "../utils/formatCurrency";
import { CartItem } from "./CartItem";
import PaymentFormModal from "./PaymentFormModal";

type ShoppingCartProps = {
  isOpen: boolean;
};

export function ShoppingCart({ isOpen }: ShoppingCartProps) {
  const navigate = useNavigate();
  const [showSuccessModal, setShowSuccessModal] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleCheckout = () => {
    setShowPaymentModal(true);
  };

  function refreshPage() {
    window.location.reload();
  }

  const handlePaymentSubmit = async (payment: PaymentEntity) => {
    setShowSuccessModal(true);

    await createOrder(payment, cartItems);
    setIsSubmitting(true);
    await new Promise((resolve) => setTimeout(resolve, 2000));
    setShowPaymentModal(false);

    localStorage.setItem("shopping-cart", "[]");
    navigate("/orders");

    setIsSubmitting(false);
  };

  const handleSuccessModalClose = () => {
    setShowSuccessModal(false);
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

      <Modal show={showSuccessModal} onHide={handleSuccessModalClose}>
        <Modal.Header closeButton>
          <Modal.Title>Payment Success</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <SuccessPage onClose={handleSuccessModalClose} />
        </Modal.Body>
      </Modal>

      {isSubmitting && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            backgroundColor: "rgba(0, 0, 0, 0.5)",
            zIndex: 9999,
          }}
        />
      )}
    </Offcanvas>
  );
}

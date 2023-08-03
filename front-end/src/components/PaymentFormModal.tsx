import { useState } from "react";
import { Button, Form, Modal } from "react-bootstrap";
import { PaymentEntity } from "../types/types";

type PaymentFormModalProps = {
  total_value: number;
  show: boolean;
  onHide: () => void;
  onSubmit: (payment: PaymentEntity) => void;
};

const PaymentFormModal: React.FC<PaymentFormModalProps> = ({
  show,
  onHide,
  onSubmit,
  total_value,
}) => {
  const [paymentData, setPaymentData] = useState<PaymentEntity>({
    payment_method: "",
    acquirer: "",
    bank: "",
    value: total_value,
  });

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    onSubmit(paymentData);
    onHide();
  };

  return (
    <Modal show={show} onHide={onHide}>
      <Modal.Header closeButton>
        <Modal.Title>Payment Form</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="paymentMethod">
            <Form.Label>Payment Method</Form.Label>
            <Form.Control
              type="text"
              name="payment_method"
              required
              defaultValue={paymentData.payment_method}
              onChange={(e) =>
                setPaymentData({
                  ...paymentData,
                  payment_method: e.target.value,
                })
              }
            />
          </Form.Group>
          <Form.Group controlId="acquirer">
            <Form.Label>Acquirer</Form.Label>
            <Form.Control
              type="text"
              name="acquirer"
              defaultValue={paymentData.acquirer}
              onChange={(e) =>
                setPaymentData({ ...paymentData, acquirer: e.target.value })
              }
            />
          </Form.Group>
          <Form.Group controlId="bank">
            <Form.Label>Bank</Form.Label>
            <Form.Control
              type="text"
              name="bank"
              defaultValue={paymentData.bank}
              onChange={(e) =>
                setPaymentData({ ...paymentData, bank: e.target.value })
              }
            />
          </Form.Group>
          <Form.Group controlId="value">
            <Form.Label>Value</Form.Label>
            <Form.Control
              type="number"
              name="value"
              defaultValue={total_value.toString()}
              required
              readOnly
            />
          </Form.Group>
          <Modal.Footer>
            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Modal.Footer>
        </Form>
      </Modal.Body>
    </Modal>
  );
};

export default PaymentFormModal;

import { Button, Card, Container, Stack } from "react-bootstrap";
import { useShoppingCart } from "../context/ShoppingCartContext";
import { formatCurrency } from "../utils/formatCurrency";

export type StoreItemProps = {
  id: number;
  name: string;
  price: number;
  image_id: string;
  category_id: number;
};

export function StoreItem({ id, name, price, image_id }: StoreItemProps) {
  const {
    getItemQuantity,
    increaseCartQuantity,
    decreaseCartQuantity,
    removeFromCart,
  } = useShoppingCart();
  const quantity = getItemQuantity(id);
  const image_src = "/imgs/" + image_id + ".jpg";

  return (
    <Stack direction="horizontal" gap={3}>
      <Container fluid="md">
        <Card className="h-100">
          <Card.Img
            variant="top"
            src={image_src}
            height="100px"
            style={{ objectFit: "cover" }}
          />
          <Card.Body className="d-flex flex-column">
            <Card.Title className="d-flex justify-content-between align-items-baseline mb-4">
              <span className="fs-4">{name}</span>
              <span className="ms-2 text-muted">{formatCurrency(price)}</span>
            </Card.Title>
            <div className="mt-auto">
              {quantity === 0 ? (
                <Button
                  className="w-100"
                  onClick={() => increaseCartQuantity(id, price)}
                >
                  + Add To Cart
                </Button>
              ) : (
                <div
                  className="d-flex align-items-center flex-column"
                  style={{ gap: ".5rem" }}
                >
                  <div
                    className="d-flex align-items-center justify-content-center"
                    style={{ gap: ".5rem" }}
                  >
                    <Button onClick={() => decreaseCartQuantity(id)}>-</Button>
                    <div>
                      <span className="fs-3">{quantity}</span> in cart
                    </div>
                    <Button onClick={() => increaseCartQuantity(id, price)}>
                      +
                    </Button>
                  </div>
                  <Button
                    onClick={() => removeFromCart(id)}
                    variant="danger"
                    size="sm"
                  >
                    Remove
                  </Button>
                </div>
              )}
            </div>
          </Card.Body>
        </Card>
      </Container>
    </Stack>
  );
}

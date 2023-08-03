import { Card, Col, Container, Navbar, Row } from "react-bootstrap";
import { StoreItem, StoreItemProps } from "./StoreItem";

type CategoryItemsProps = {
  id: number;
  image_id: string;
  name: string;
  items: StoreItemProps[];
};

const CategoryComponent: React.FC<CategoryItemsProps> = ({
  id,
  image_id,
  name,
  items,
}) => {
  const image_src = "/imgs/" + image_id + ".jpg";

  return (
    <div>
      <Navbar className="bg-body-tertiary">
        <Container fluid="md">
          <Navbar.Brand href="#home">
            <h3>{name}</h3>
          </Navbar.Brand>
        </Container>
      </Navbar>
      <Card className="mb-3">
        <Card.Img
          variant="top"
          src={image_src}
          height="150px"
          style={{ objectFit: "cover" }}
        />
      </Card>
      <Container fluid="md">
        <Row xs={1} md={2} lg={3} className="g-3">
          {items.map((item) => (
            <Col key={item.id}>
              <StoreItem {...item} />
            </Col>
          ))}
        </Row>
      </Container>
    </div>
  );
};

export default CategoryComponent;

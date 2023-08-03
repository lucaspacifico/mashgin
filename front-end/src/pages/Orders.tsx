import { useEffect, useState } from "react";
import { ListGroup } from "react-bootstrap";
import { getAllOrders } from "../api/api";

export interface Order {
  id: number;
  payment_method_id: string;
  value: number;
  products_id: number[];
}

export function Orders() {
  const [orders, setOrders] = useState<Order[]>([]);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const response = await getAllOrders();
      // Map the response data to the Order interface
      const ordersData: Order[] = response.data.data.map((orderData: any) => {
        return {
          id: orderData.id,
          payment_method_id: orderData.payment_method_id,
          value: orderData.price,
          products_id: orderData.products_id,
        };
      });

      setOrders(ordersData);
    } catch (error) {
      console.error("Error fetching orders:", error);
    }
  };

  return (
    <div>
      <h1>Order List</h1>
      {orders.length > 0 ? (
        <ListGroup>
          {orders.map((order) => (
            <ListGroup.Item key={order.id}>
              <h3>Order ID: {order.id}</h3>
              <div>
                <strong>Payment Method:</strong> {order.payment_method_id}
              </div>
              <div>
                <strong>Value:</strong> ${order.value}
              </div>
              <div>
                <strong>Products IDs:</strong> {order.products_id}
              </div>
            </ListGroup.Item>
          ))}
        </ListGroup>
      ) : (
        <p>No orders available.</p>
      )}
    </div>
  );
}

import { array, number, object, string } from "joi";

class Order {
  constructor(id, price, payment_method_id, products_id) {
    const schema = object({
      id: number().optional(),
      price: number().required(),
      payment_method_id: string().required(),
      products_id: array().items(number()).required(),
    });

    const { error } = schema.validate({
      id,
      price,
      payment_method_id,
      products_id,
    });
    if (error) {
      throw new Error(`Invalid Order object: ${error.message}`);
    }

    this.id = id || null;
    this.price = price;
    this.payment_method_id = payment_method_id;
    this.products_id = products_id;
  }
}

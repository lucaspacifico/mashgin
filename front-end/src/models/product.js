import { number, object, string } from "joi";

class Product {
  constructor(id, name, image_id, price) {
    const schema = object({
      id: number().optional(),
      name: string().required(),
      image_id: string().required(),
      price: number().required(),
    });

    const { error } = schema.validate({ id, name, image_id, price });
    if (error) {
      throw new Error(`Invalid Product object: ${error.message}`);
    }

    this.id = id || null;
    this.name = name;
    this.image_id = image_id;
    this.price = price;
  }
}

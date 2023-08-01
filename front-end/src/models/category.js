import { number, object, string } from "joi";

class Category {
  constructor(id, name, image_id) {
    const schema = object({
      id: number().required(),
      name: string().required(),
      image_id: number().required(),
    });

    const { error } = schema.validate({ id, name, image_id });
    if (error) {
      throw new Error(`Invalid Category object: ${error.message}`);
    }

    this.id = id;
    this.name = name;
    this.image_id = image_id;
  }
}

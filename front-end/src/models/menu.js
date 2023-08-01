import { array, number, object, string } from "joi";

class Menu {
  constructor(id, name, categories_id) {
    const schema = object({
      id: number().optional(),
      name: string().required(),
      categories_id: array().items(number()).required(),
    });

    const { error } = schema.validate({ id, name, categories_id });
    if (error) {
      throw new Error(`Invalid Menu object: ${error.message}`);
    }

    this.id = id || null;
    this.name = name;
    this.categories_id = categories_id;
  }
}

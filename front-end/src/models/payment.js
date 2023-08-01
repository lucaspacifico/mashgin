import { number, object, string } from "joi";

class Payment {
  constructor(id, payment_method, acquirer, bank, value) {
    const schema = object({
      id: number().optional(),
      payment_method: string().required(),
      acquirer: string().optional(),
      bank: string().optional(),
      value: number().required(),
    });

    const { error } = schema.validate({
      id,
      payment_method,
      acquirer,
      bank,
      value,
    });
    if (error) {
      throw new Error(`Invalid Payment object: ${error.message}`);
    }

    this.id = id || null;
    this.payment_method = payment_method;
    this.acquirer = acquirer || null;
    this.bank = bank || null;
    this.value = value;
  }
}

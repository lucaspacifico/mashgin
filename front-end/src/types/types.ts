export interface CreateOrderRequest {
  payment_form: PaymentEntity;
  products_ids: number[];
}

export interface CreateMenuRequest {
  categories: CategoryEntity[];
  items: ProductEntity[];
}

export interface PaymentEntity {
  id?: number;
  payment_method: string;
  acquirer?: string;
  bank?: string;
  value: number;
}

export interface CategoryEntity {
  id: number;
  name: string;
  image_id: string;
}

export interface ProductEntity {
  id?: number;
  name: string;
  image_id: string;
  price: number;
  category_id: number;
}

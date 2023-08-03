import axios, { AxiosResponse } from "axios";
import { CartItem } from "../context/ShoppingCartContext";
import initialMenuData from "../data/initial_menu.json";
import {
  CreateMenuRequest,
  CreateOrderRequest,
  PaymentEntity,
} from "../types/types";

const API_BASE_URL = "http://localhost:8000";

export const createOrder = async (
  payment: PaymentEntity,
  cartItem: CartItem[]
): Promise<AxiosResponse> => {
  const orderData: CreateOrderRequest = {
    payment_form: payment,
    products_ids: cartItem.map((item) => item.id),
  };

  const url = `${API_BASE_URL}/order/create`;
  try {
    const response = await axios.post(url, orderData);
    return response;
  } catch (error) {
    console.error("Error creating order:", error);
    throw error;
  }
};

export const getMenuById = async (menu_id: number): Promise<AxiosResponse> => {
  const url = `${API_BASE_URL}/menu/${menu_id}`;
  try {
    const response = await axios.get(url);
    return response;
  } catch (error) {
    console.error("Error getting menu:", error);
    throw error;
  }
};

export const getLastMenuOrCreateMenu = async (): Promise<AxiosResponse> => {
  const url = `${API_BASE_URL}/menu/0`;
  try {
    const response = await axios.get(url);

    return response;
  } catch (error) {
    console.error("Error getting menu:", error);
    try {
      const createResponse = await createMenu();
      return createResponse;
    } catch (createError) {
      console.error("Error creating menu:", createError);
      throw createError;
    }
  }
};

export const createMenu = async (): Promise<AxiosResponse> => {
  const url = `${API_BASE_URL}/menu/create`;
  try {
    const createMenuRequest: CreateMenuRequest = initialMenuData;

    const response = await axios.post(url, createMenuRequest);
    return response;
  } catch (error) {
    console.error("Error creating menu:", error);
    throw error;
  }
};

export const getOrderById = async (
  order_id: number
): Promise<AxiosResponse> => {
  const url = `${API_BASE_URL}/order/${order_id}`;
  try {
    const response = await axios.get(url);
    return response;
  } catch (error) {
    console.error("Error getting order:", error);
    throw error;
  }
};

export const getAllOrders = async (): Promise<AxiosResponse> => {
  const url = `${API_BASE_URL}/order/`;
  try {
    const response = await axios.get(url);
    return response;
  } catch (error) {
    console.error("Error getting order:", error);
    throw error;
  }
};



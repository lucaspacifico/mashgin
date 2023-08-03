import axios, { AxiosResponse } from "axios";
import { CreateMenuRequest, CreateOrderRequest } from "../types/types";

const API_BASE_URL = "http://localhost:8000";

export const createOrder = async (
  orderData: CreateOrderRequest
): Promise<AxiosResponse> => {
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

export const createMenu = async (
  menuData: CreateMenuRequest
): Promise<AxiosResponse> => {
  const url = `${API_BASE_URL}/menu/create`;
  try {
    const response = await axios.post(url, menuData);
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

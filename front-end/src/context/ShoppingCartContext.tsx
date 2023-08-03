import { createContext, ReactNode, useContext, useState } from "react"
import { ShoppingCart } from "../components/ShoppingCart"
import { useLocalStorage } from "../hooks/useLocalStorage"

type ShoppingCartProviderProps = {
  children: ReactNode
}

export type CartItem = {
  id: number;
  quantity: number;
  current_price: number;
  original_price: number;
};

type ShoppingCartContext = {
  openCart: () => void;
  closeCart: () => void;
  getItemQuantity: (id: number) => number;
  increaseCartQuantity: (id: number, price: number) => void;
  getItemCurrentPrice: (id: number) => number;
  resetCart: () => void;
  decreaseCartQuantity: (id: number) => void;
  removeFromCart: (id: number) => void;
  cartQuantity: number;
  cartItems: CartItem[];
};

const ShoppingCartContext = createContext({} as ShoppingCartContext);

export function useShoppingCart() {
  return useContext(ShoppingCartContext);
}

export function ShoppingCartProvider({ children }: ShoppingCartProviderProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [cartItems, setCartItems] = useLocalStorage<CartItem[]>(
    "shopping-cart",
    []
  );

  const cartQuantity = cartItems.reduce(
    (quantity, item) => item.quantity + quantity,
    0
  );

  const openCart = () => setIsOpen(true);
  const closeCart = () => setIsOpen(false);
  function getItemQuantity(id: number) {
    return cartItems.find((item) => item.id === id)?.quantity || 0;
  }

  const resetCart = () => {
    setCartItems([]);
    setIsOpen(false);
  };

  function getItemCurrentPrice(id: number) {
    return cartItems.find((item) => item.id === id)?.current_price || 0;
  }

  function increaseCartQuantity(id: number, price: number) {
    setCartItems((currItems) => {
      const currentItems = currItems.find((item) => item.id === id);
      if (currentItems == null) {
        return [
          ...currItems,
          { id, quantity: 1, original_price: price, current_price: price },
        ];
      } else {
        return currItems.map((item) => {
          if (item.id === id) {
            return {
              ...item,
              quantity: item.quantity + 1,
              current_price: item.original_price * (item.quantity + 1),
              original_price: item.original_price,
            };
          } else {
            return item;
          }
        });
      }
    });
  }
  function decreaseCartQuantity(id: number) {
    setCartItems((currItems) => {
      if (currItems.find((item) => item.id === id)?.quantity === 1) {
        return currItems.filter((item) => item.id !== id);
      } else {
        return currItems.map((item) => {
          if (item.id === id) {
            return {
              ...item,
              quantity: item.quantity - 1,
              current_price: item.original_price * (item.quantity - 1),
              original_price: item.original_price,
            };
          } else {
            return item;
          }
        });
      }
    });
  }
  function removeFromCart(id: number) {
    setCartItems((currItems) => {
      return currItems.filter((item) => item.id !== id);
    });
  }

  return (
    <ShoppingCartContext.Provider
      value={{
        getItemQuantity,
        getItemCurrentPrice,
        increaseCartQuantity,
        decreaseCartQuantity,
        removeFromCart,
        openCart,
        closeCart,
        resetCart,
        cartItems,
        cartQuantity,
      }}
    >
      {children}
      <ShoppingCart isOpen={isOpen} />
    </ShoppingCartContext.Provider>
  );
}

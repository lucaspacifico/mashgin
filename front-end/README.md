

# Mashgin - Frontend - Client Side



The front-end was made using React Vite with react-bootstrap, and using typescript.

### Entrypoint - URL

```shell
http://localhost:8080
```

## Project Folder

Overall, this file structure promotes a modular and organized approach to building a React app with TypeScript. The separation of concerns into different directories has the intention to makes it easier to manage and scale the application as it grows. Following this structure:

`api`: This directory contains files related to API integration. The `api.ts` file likely contains functions for making API requests using `axios` or other HTTP libraries.

`components`: This directory contains reusable React components used throughout the application. Each component is typically defined in its own file for better organization and reusability.

> - `CartItem.tsx`: Component for displaying individual cart items.
> - `CategoryItems.tsx`: Component for displaying items within a category.
> - `Navbar.tsx`: Component representing the application's navigation bar.
> - `PaymentFormModal.tsx`: Component for displaying a modal with a payment form.
> - `ShoppingCart.tsx`: Component for displaying the shopping cart with its contents.
> - `StoreItem.tsx`: Component for displaying an individual store item.

`context`: This directory contains files related to React context. The `ShoppingCartContext.tsx` file likely defines the context and provider for managing the shopping cart state.

`data`: This directory contains static data files used in the application. It includes `initial_menu.json`, which may contain initial menu data, and `items.json`, which could contain item data for the store.

`hooks`: This directory contains custom React hooks. The `useLocalStorage.ts` file likely contains a custom hook for interacting with the browser's local storage.

`pages`: This directory contains page components that represent different routes or pages of the application.

> - `Orders.tsx`: Page component for displaying the list of orders.
> - `Store.tsx`: Page component for displaying the store and its categories.
> - `SuccessPage.tsx`: Page component for displaying a success message after a successful payment.

`types`: This directory contains TypeScript type definitions used in the application. The `types.ts` file likely includes interfaces or types for defining the shape of data used throughout the app.

## **Running the Application**

```
docker-compose up -d --build frontend
```

#### Running into local environment

Install node:v12.22.10 

```
  npm install
  ```

```
  npm run dev
````

It will run the front-end application.

## Images

Some images to present the pages

#### Front Page

![front_page](/resources/front_page.png)

#### Front Page with added Items

![front_page_with_added_items](/resources/front_page_with_added_items.png)



#### Front Page with Cart

![front_page_with_cart](/resources/front_page_with_cart.png)


#### Payment Form

#### ![payment_form](/resources/payment_form.png)

#### Order List

![order_list](/resources/order_list.png)


## Improvement Points

- Add tests to project and Storybook;
- Increase test coverage and fix the bugs that were found;
-  Include CI/CD routines in the code;
- Improve the payment flow and its structure;
- Make more effective use of framework tools, such as useEffect() and useMemo(). I ended up not using many front development features that could improve some parts of the code.
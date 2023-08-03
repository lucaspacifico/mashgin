import CategoryComponent from "../components/CategoryItems";
import initialMenuData from "../data/initial_menu.json";
import { CreateMenuRequest } from "../types/types";

export function Store() {
  const menuData: CreateMenuRequest = initialMenuData;

  const itemsByCategory: { [categoryId: number]: any } = {};
  menuData.items.forEach((item) => {
    if (!itemsByCategory[item.category_id]) {
      itemsByCategory[item.category_id] = [];
    }
    itemsByCategory[item.category_id].push(item);
  });


  return (
    <>
      <h1>Store</h1>
      {menuData.categories.map((category) => (
        <CategoryComponent
          key={category.id}
          id={category.id}
          image_id={category.image_id}
          name={category.name}
          items={itemsByCategory[category.id] || []}
        />
      ))}
    </>
  );
}

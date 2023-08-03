import { useEffect, useState } from "react";
import { getLastMenuOrCreateMenu } from "../api/api";
import CategoryComponent from "../components/CategoryItems";
import { CreateMenuRequest } from "../types/types";

export function Store() {
  const [menuData, setMenuData] = useState<CreateMenuRequest | null>(null);
  const [isMenuDataFetched, setIsMenuDataFetched] = useState(false);

  useEffect(() => {
    if (!isMenuDataFetched) {
      const fetchMenuData = async () => {
        try {
          const response = await getLastMenuOrCreateMenu();
          setMenuData(response.data);
        } catch (error) {
          console.error("Error fetching menu data:", error);
        }
        setIsMenuDataFetched(true);
      };
      fetchMenuData();
    }
  }, [isMenuDataFetched]);

  if (!menuData) {
    return <div>Loading...</div>;
  }

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

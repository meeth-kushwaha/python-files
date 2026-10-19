"""Program 043: Strategy Design Pattern for Discounts."""
from typing import Callable

class ShoppingCart:
    def __init__(self, total: float, discount_strategy: Callable[[float], float]):
        self.total = total
        self.discount_strategy = discount_strategy

    def final_price(self) -> float:
        return self.discount_strategy(self.total)

def standard_discount(amount: float) -> float:
    return amount

def vip_discount(amount: float) -> float:
    return amount * 0.80

def seasonal_promo(amount: float) -> float:
    return max(0.0, amount - 15.0)

if __name__ == "__main__":
    print("--- 043: Strategy Pattern ---")
    cart = ShoppingCart(100.0, vip_discount)
    print(f"VIP total: ${cart.final_price():.2f}")
    cart.discount_strategy = seasonal_promo
    print(f"Seasonal promo total: ${cart.final_price():.2f}")

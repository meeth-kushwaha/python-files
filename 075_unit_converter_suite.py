"""Program 075: Multi-Dimensional Unit Converter."""
class UnitConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return c * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f: float) -> float:
        return (f - 32) * 5 / 9

    @staticmethod
    def km_to_miles(km: float) -> float:
        return km * 0.621371

    @staticmethod
    def bytes_to_human(nbytes: int) -> str:
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if nbytes < 1024.0:
                return f"{nbytes:.2f} {unit}"
            nbytes /= 1024.0
        return f"{nbytes:.2f} PB"

if __name__ == "__main__":
    print("--- 075: Unit Converter Suite ---")
    print(f"100 C in F: {UnitConverter.celsius_to_fahrenheit(100):.1f}")
    print(f"10 km in miles: {UnitConverter.km_to_miles(10):.2f}")
    print(f"10485760 bytes: {UnitConverter.bytes_to_human(10485760)}")

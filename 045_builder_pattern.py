"""Program 045: Builder Pattern for SQL Query Construction."""
class QueryBuilder:
    def __init__(self, table: str):
        self.table = table
        self.fields = ["*"]
        self.conditions = []
        self.limit_val = None

    def select(self, *fields: str):
        self.fields = list(fields)
        return self

    def where(self, condition: str):
        self.conditions.append(condition)
        return self

    def limit(self, count: int):
        self.limit_val = count
        return self

    def build(self) -> str:
        query = f"SELECT {', '.join(self.fields)} FROM {self.table}"
        if self.conditions:
            query += f" WHERE {' AND '.join(self.conditions)}"
        if self.limit_val is not None:
            query += f" LIMIT {self.limit_val}"
        return query + ";"

if __name__ == "__main__":
    print("--- 045: Builder Pattern ---")
    sql = (QueryBuilder("users")
           .select("id", "username", "email")
           .where("active = 1")
           .where("age >= 18")
           .limit(10)
           .build())
    print("Constructed SQL:", sql)

from enum import Enum

class Tables(Enum):
    customer_customer_demo = "customer_customer_demo"
    customer_demographics = "customer_demographics"
    employee_territories = "employee_territories"
    orders = "orders"
    customers = "customers"
    products = "products"
    shippers = "shippers"
    suppliers = "suppliers"
    territories = "territories"
    us_states = "us_states"
    categories = "categories"
    region = "region"
    employees = "employees"
    order_details = "order_details"

TABLE_NAMES = [Tables.customer_customer_demo, Tables.customer_demographics, Tables.employee_territories,
               Tables.orders, Tables.customers, Tables.products,
               Tables.shippers, Tables.suppliers, Tables.territories,
               Tables.us_states, Tables.categories, Tables.region, Tables.employees, Tables.order_details]
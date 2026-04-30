import streamlit as st

st.set_page_config(page_title="Inventory Store", layout="wide")

# Title
st.title(" Inventory Management System")

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Select Option",
    ["Dashboard", "Add Product", "View Products", "Update Product", "Delete Product", "Reports"]
)

# Dashboard
if menu == "Dashboard":
    st.header(" Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Products", "0")

    with col2:
        st.metric("Low Stock Items", "0")

    with col3:
        st.metric("Total Value", "₹0")

# Add Product
elif menu == "Add Product":
    st.header("Add New Product")

    col1, col2 = st.columns(2)

    with col1:
        product_name = st.text_input("Product Name")
        category = st.selectbox("Category", ["Electronics", "Clothing", "Food", "Other"])

    with col2:
        price = st.number_input("Price", min_value=0)
        quantity = st.number_input("Quantity", min_value=0)

    st.text_area("Description")

    st.button("Add Product")

# View Products
elif menu == "View Products":
    st.header("Product List")

    st.text_input("Search Product")

    st.dataframe([])  

# Update Product
elif menu == "Update Product":
    st.header(" Update Product")

    st.selectbox("Select Product", ["Product 1", "Product 2"])

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("New Product Name")

    with col2:
        st.number_input("New Price")

    st.number_input("New Quantity")

    st.button("Update")

# Delete Product
elif menu == "Delete Product":
    st.header(" Delete Product")

    st.selectbox("Select Product to Delete", ["Product 1", "Product 2"])

    st.button("Delete")
 

# Reports
elif menu == "Reports":
    st.header(" Reports")

    st.selectbox("Select Report Type", ["Stock Report", "Sales Report"])

    st.line_chart([])  # Placeholder chart



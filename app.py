import streamlit as st

# Title of the app
st.title("Medicine Delivery App")

# Step 1: Collect User Personal Information
st.header("Enter Your Personal Information")
name = st.text_input("Name", help="Enter your full name")
phone_number = st.text_input("Phone Number", help="Enter a valid phone number")
street = st.text_input("Street", help="Enter your street address")
city = st.text_input("City", help="Enter your city")
pincode = st.text_input("Pincode", help="Enter your area's pincode")

# Combine street, city, and pincode into the delivery address
user_address = f"{street}, {city}, {pincode}"

# Initialize session state for medicines cart if not already present
if 'medicines' not in st.session_state:
    st.session_state['medicines'] = []

# Step 2: Add Medicines to Cart
st.header("Add Medicines to Cart")
medicine_name = st.text_input("Medicine Name", key='medicine_input', help="Enter the name of the medicine you want to add to the cart")
if st.button("Add Medicine to Cart"):
    if medicine_name.strip():  # Check if the medicine name is not empty
        st.session_state['medicines'].append(medicine_name.strip())
        st.success(f"'{medicine_name}' has been added to the cart!")
        st.session_state['medicine_input'] = ""  # Clear the input field after adding

# Step 3: View Cart Items
st.header("View Cart Items")
if st.session_state['medicines']:
    st.subheader("Medicines in Your Cart:")
    for i, med in enumerate(st.session_state['medicines'], start=1):
        st.write(f"{i}. {med}")
else:
    st.write("Your cart is currently empty.")

# Option to remove items from cart
remove_item = st.selectbox("Select an item to remove", options=["None"] + st.session_state['medicines'])
if st.button("Remove Selected Item"):
    if remove_item != "None":
        st.session_state['medicines'].remove(remove_item)
        st.success(f"'{remove_item}' has been removed from the cart!")

# Step 4: Payment Options
st.header("Payment Options")
payment_method = st.selectbox("Choose Payment Method", ["Select Payment Method", "Credit/Debit Card", "UPI", "Cash on Delivery"])

# Step 5: Submit the Order
if st.button("Place Order"):
    if all([name.strip(), phone_number.strip(), street.strip(), city.strip(), pincode.strip()]) and st.session_state['medicines'] and payment_method != "Select Payment Method":
        st.success("Your order has been successfully placed!")
        st.write("### Order Details:")
        st.write(f"**Name:** {name}")
        st.write(f"**Phone Number:** {phone_number}")
        st.write(f"**Address:** {user_address}")
        st.write(f"**Medicines Ordered:** {', '.join(st.session_state['medicines'])}")
        st.write(f"**Payment Method:** {payment_method}")
        # Backend logic to process the order can be added here
    else:
        st.error("Please complete all the required fields, add at least one medicine, and choose a payment method.")

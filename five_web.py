import time, os
import streamlit as st
import five_program_module as pm

# if not os.path.exists("shopping_list.txt"):
#     with open("shopping_list.txt", "w") as file_temp:
#         pass


def write_item():
    item = st.session_state["item_8554321"] + "\n"
    shopping_list.append(item)
    pm.write_shopping_list(shopping_list)


date_time = time.strftime("%I:%M %p %A, %d %B %Y")
shopping_list = pm.get_shopping_list()

st.title("shopping list app")
st.subheader("- by gunapriyakumari")
st.write("It is currently", date_time)

if shopping_list == []:
    st.checkbox("Your shopping list is currently empty!!", key="item_8554322")

else:
    for index, ee in enumerate(shopping_list):
        new_index = f"{index}-{ee}"
        checkbox_value = st.checkbox(ee, key=new_index)
        if checkbox_value:
            shopping_list.pop(index)

            pm.write_shopping_list(shopping_list)

            del st.session_state[new_index]

            st.rerun()

x = st.text_input(label=" ", placeholder="Enter an item...", key="item_8554321", on_change=write_item)
# st.session_state
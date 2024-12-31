import streamlit as st
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="pritri",
  database="retail_order"
)

mycursor = mydb.cursor()

st.title("RETAIL DATA ANALYSIS 🛒 :chart: :bar_chart:")
st.image("C:/Users/manib/OneDrive/Desktop/DS files/Screen-Shot-2018-11-26-at-2.10.07-PM.png",width=700)

tabs=st.tabs(['TAB1','TAB2'])
with tabs[0]:
    selected_option = st.selectbox("Choose an option:", 
    [
      "Q1:Find top 10 highest revenue generating products",
      "Q2:Find the top 5 cities with the highest profit margins",
      "Q3:Calculate the total discount given for each category",
      "Q4:Find the average sale price per product category",
      "Q5:Find the region with the highest average sale price",
      "Q6:Find the total profit per category",
      "Q7:Identify the top 3 segments with the highest quantity of orders",
      "Q8:Determine the average discount percentage given per region",
      "Q9:Find the product category with the highest total profit",
      "Q10:Calculate the total revenue generated per year"
    ],
    placeholder="Select a query",
    index=None
)
    
if selected_option == "Q1:Find top 10 highest revenue generating products":
  st.subheader("Find top 10 highest revenue generating products")
  mycursor.execute("SELECT sub_category,category,profit FROM order2 ORDER BY profit DESC LIMIT 10;")
  data=mycursor.fetchall()
  df=pd.DataFrame(data,columns=mycursor.column_names)
  st.dataframe(df)
elif selected_option == "Q2:Find the top 5 cities with the highest profit margins":
  st.subheader("Find the top 5 cities with the highest profit margins")
  mycursor.execute("select O1.city from order1 as O1 INNER JOIN (select order_id from order2 order by profit desc limit 5) as O2 ON O1.order_id = O2.order_id;")
  data=mycursor.fetchall()
  df=pd.DataFrame(data,columns=mycursor.column_names)
  st.dataframe(df)
elif selected_option == "Q3:Calculate the total discount given for each category":
  st.subheader("Calculate the total discount given for each category")
  mycursor.execute("SELECT category, SUM(discount) FROM order2 GROUP BY category;")
  data=mycursor.fetchall()
  df=pd.DataFrame(data,columns=mycursor.column_names)
  st.dataframe(df)
elif selected_option == "Q4:Find the average sale price per product category":
    st.subheader("Find the average sale price per product category")
    mycursor.execute("SELECT distinct category,avg(sales_price) FROM order2 GROUP BY category;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q5:Find the region with the highest average sale price":
    st.subheader("Find the region with the highest average sale price")
    mycursor.execute("SELECT REGION,AVG(SALES_PRICE)  FROM ORDER1 AS O1,ORDER2 AS O2 WHERE O1.ORDER_ID=O2.ORDER_ID GROUP BY REGION;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q6:Find the total profit per category":
    st.subheader("Find the total profit per category")
    mycursor.execute("SELECT category, SUM(PROFIT) FROM order2 GROUP BY category;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q7:Identify the top 3 segments with the highest quantity of orders":
    st.subheader("Identify the top 3 segments with the highest quantity of orders")
    mycursor.execute("SELECT O1.SEGMENT FROM ORDER1 AS O1 INNER JOIN (SELECT ORDER_ID FROM ORDER2 ORDER BY QUANTITY DESC LIMIT 3) AS O2 ON O1.ORDER_ID = O2.ORDER_ID;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q8:Determine the average discount percentage given per region":
    st.subheader("Determine the average discount percentage given per region")
    mycursor.execute("SELECT REGION,AVG(DISCOUNT_PERCENT) FROM ORDER1 AS O1,ORDER2 AS O2 WHERE O1.ORDER_ID=O2.ORDER_ID GROUP BY REGION;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q9:Find the product category with the highest total profit":
    st.subheader("Find the product category with the highest total profit")
    mycursor.execute("SELECT CATEGORY,PROFIT FROM ORDER2 order by PROFIT desc;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q10:Calculate the total revenue generated per year":
    selected_option == "Q10:Calculate the total revenue generated per year"
    st.subheader("Calculate the total revenue generated per year")
    mycursor.execute("SELECT YEAR(ORDER_DATE) AS YEAR ,SUM(PROFIT) AS SUM_PROFIT FROM ORDER1 AS O1,ORDER2 AS O2 WHERE O1.ORDER_ID=O2.ORDER_ID GROUP BY YEAR(ORDER_DATE);")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
else :
    selected_option = None


with tabs[1]:
    selected_option = st.selectbox("Choose an option:", 
    [                               
     "Q1:List all orders with a profit greater than 50",
     "Q2:Find orders from order1 where the state is 'Florida' and link them with their respective category from order2.",
     "Q3:Retrieve all orders where the ship_mode is 'Standard Class' and the category is 'Furniture'. ",
     "Q4:Retrieve the data from order2 to get labels,bookcases,Storage,art.",
     "Q5:Top 10 Rank products by their profit within each category.",
     "Q6:Display the top 5 orders with the highest sales_price.",
     "Q7:Calculate the overall profit margin for all orders.",
     "Q8:Calculate the total revenue generated per month.",
     "Q9:Display orders with a negative profit and suggest possible reasons based on the discount_percent or cost_price.",
     "Q10:Show orders with segment 'Corporate' and a total sales_price exceeding 500."
    ],
    placeholder="Select a query",
    index=None
    )
    
if selected_option == "Q1:List all orders with a profit greater than 50":
  st.subheader("LIST OF PROFITS")
  mycursor.execute("SELECT * FROM ORDER2 AS O2 WHERE O2.PROFIT > 50;")
  data=mycursor.fetchall()
  df=pd.DataFrame(data,columns=mycursor.column_names)
  st.dataframe(df)
elif selected_option == "Q2:Find orders from order1 where the state is 'Florida' and link them with their respective category from order2.":
  st.subheader(" STATE and CATEGORY ")
  mycursor.execute("SELECT O2.CATEGORY,O1.STATE FROM ORDER2 AS O2 INNER JOIN(SELECT * FROM ORDER1 WHERE STATE='Florida') AS O1 ON O1.ORDER_ID = O2.ORDER_ID;")
  data=mycursor.fetchall()
  df=pd.DataFrame(data,columns=mycursor.column_names)
  st.dataframe(df)
elif selected_option == "Q3:Retrieve all orders where the ship_mode is 'Standard Class' and the category is 'Furniture'. ":
  st.subheader(" SHIPMODE AND CATEGORY ")
  mycursor.execute("SELECT o1.order_id,o1.ship_mode,o2.category,o2.product_id,o2.sales_price,o2.profit FROM ORDER1 AS o1  JOIN ORDER2 AS o2 ON o1.ORDER_ID = o2.ORDER_ID where O1.ship_mode='Standard Class' AND O2.category='Furniture'; ")
  data=mycursor.fetchall()
  df=pd.DataFrame(data,columns=mycursor.column_names)
  st.dataframe(df)
elif selected_option == "Q4:Retrieve the data from order2 to get labels,bookcases,Storage,art.":
    st.subheader("LABELS,BOOKCASES,STORAGE ART")
    mycursor.execute("SELECT * FROM ORDER2 WHERE SUB_CATEGORY IN ('LABELS','BOOKCASES','STORAGE','ART');")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q5:Top 10 Rank products by their profit within each category.":
    st.subheader("TOP 10 PRODUCTS")
    mycursor.execute("SELECT CATEGORY,PROFIT,RANK() OVER (PARTITION BY category ORDER BY profit DESC) AS profit_rank FROM ORDER2 LIMIT 10;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q6:Display the top 5 orders with the highest sales_price.":
    st.subheader("TOP 5 ORDERS OF HIGHEST SALE_PRICE")
    mycursor.execute("SELECT SUB_CATEGORY,SALES_PRICE,RANK() OVER (PARTITION BY category ORDER BY sales_price DESC) AS HIGHESTSALES FROM ORDER2 LIMIT 5;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q7:Calculate the overall profit margin for all orders.":
    st.subheader("PROFIT MARGIN OF ALL ORDERS")
    mycursor.execute("SELECT SUB_CATEGORY,(SUM(sales_price) - SUM(cost_price)) / SUM(sales_price) * 100 AS profit_margin FROM ORDER2 AS O2 GROUP BY SUB_CATEGORY;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q8:Calculate the total revenue generated per month.":
    st.subheader("TOTAL REVENUE PER MONTH")
    mycursor.execute("SELECT DATE_FORMAT(`ORDER_DATE`,'%M') AS MONTH ,SUM(PROFIT) AS SUM_PROFIT FROM ORDER1 AS O1,ORDER2 AS O2 WHERE O1.ORDER_ID=O2.ORDER_ID GROUP BY DATE_FORMAT(`ORDER_DATE`,'%M');")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option == "Q9:Display orders with a negative profit and suggest possible reasons based on the discount_percent or cost_price.":
    st.subheader("THE NEGATIVE(-) PROFIT")
    mycursor.execute("SELECT o2.order_id,o2.product_id,o2.category,o2.profit,o2.discount_percent,o2.cost_price,o2.sales_price,CASE WHEN o2.discount_percent > 5 THEN 'High Discount' WHEN o2.cost_price > o2.sales_price THEN 'Cost Exceeds Sales'  ELSE 'Other Factors' END AS possible_reason FROM order2 o2 WHERE o2.profit < 0;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
elif selected_option =="Q10:Show orders with segment 'Corporate' and a total sales_price exceeding 500." :
    selected_option == "SEGMENT AND SALES_PRICE"
    st.subheader("Show orders with segment 'Corporate' and a total sales_price exceeding 500.")
    mycursor.execute("SELECT o1.order_id,o1.segment,SUM(o2.sales_price) AS total_sales_price FROM order1 o1 JOIN order2 o2 ON o1.order_id = o2.order_id WHERE o1.segment = 'Corporate' GROUP BY o1.order_id, o1.segment HAVING total_sales_price > 500;")
    data=mycursor.fetchall()
    df=pd.DataFrame(data,columns=mycursor.column_names)
    st.dataframe(df)
else :
    selected_option = None







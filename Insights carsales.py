import mysql.connector # type: ignore
import pandas as pd # type: ignore

# Establishing connection to MySQL
conn = mysql.connector.connect(host='localhost', username='root', password='@Qwerty123', database='carsales')

# Create a cursor object
mycursor = conn.cursor()

# Execute the SQL query to fetch data from 'sales' table
mycursor.execute("SELECT * FROM sales")

# Fetch all rows from the query
columns = [desc[0] for desc in mycursor.description]
data = mycursor.fetchall()

# Convert the fetched data into a pandas DataFrame
df = pd.DataFrame(data, columns=columns)

# Step 1: Check for NULL (missing) values
null_values = df.isnull().sum()
print("Null values in each column before cleaning:")
print(null_values)

# You can decide what to do with NULL values (e.g., drop rows, fill them, etc.)
# Example: You can drop rows with NULL values in any column
# df.dropna(inplace=True)

# Or you can fill NULL values with a specific value (e.g., 0, or the mean for numeric columns)
# Example: Fill NULL values with 0 for 'Annual Income' and 'Price ($)'
df['Annual Income'].fillna(0, inplace=True)
df['Price'].fillna(0, inplace=True)

# Step 2: Check and fix data types (e.g., make sure numerical columns are numbers)
df['Annual Income'] = pd.to_numeric(df['Annual Income'], errors='coerce')  # Coerce errors to NaN
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Convert to numeric, invalid values become NaN

# Step 3: Remove duplicates if any
df.drop_duplicates(inplace=True)

# Step 4: Standardize column names (e.g., remove leading/trailing spaces, convert to lowercase)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 5: Handle any other specific issues, such as fixing unexpected characters
# Example: Remove unwanted characters like "Ã‚" from the 'Engine' column
df['engine'] = df['engine'].str.replace('Ã‚', '', regex=True)

# Optional: Print the cleaned DataFrame to verify
print("\nCleaned DataFrame:")
print(df.head())

# Close the database connection
conn.close()

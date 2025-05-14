import pandas as pd

# Sample data
df = pd.DataFrame({
    'order_date': ['2025-03-01', '2025-03-02'],
    'shipping_date': ['2025-03-03', '2025-03-05'],
    'transit_days': [5, 3],  # Transit time from shipping to delivery
    'distance_km': [500, 1000],
    'shipping_cost': [2000, 3500]
})

# Convert to datetime
df['order_date'] = pd.to_datetime(df['order_date'])
df['shipping_date'] = pd.to_datetime(df['shipping_date'])

# Calculate Shipping Delay
df['shipping_delay'] = (df['shipping_date'] - df['order_date']).dt.days

# Calculate Total Delivery Time
df['total_delivery_time'] = df['shipping_delay'] + df['transit_days']

# Calculate Cost per km
df['cost_per_km'] = df['shipping_cost'] / df['distance_km']

print(df)
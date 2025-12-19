import pandas as pd
from traffic_agent import TrafficAgent
from sklearn.ensemble import RandomForestRegressor

# 读取数据
df = pd.read_csv("traffic.csv")

# 训练模型
X = df[["hour", "is_peak"]]
y = df["vehicles"]

model = RandomForestRegressor()
model.fit(X, y)

# 模拟当前时间
current_data = [[17, 1]]  # 17:00 高峰
predicted_vehicles = int(model.predict(current_data)[0])

# 智能体决策
agent = TrafficAgent()
level, strategy = agent.make_decision(predicted_vehicles)

print("预测车辆数:", predicted_vehicles)
print("拥堵等级:", level)
print("推荐策略:", strategy)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 读取数据
df = pd.read_csv("traffic.csv")

# 特征 & 预测目标
X = df[["hour", "is_peak"]]
y = df["vehicles"]

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练模型
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# 测试预测
pred = model.predict(X_test)
mae = mean_absolute_error(y_test, pred)

print("预测误差 MAE:", mae)

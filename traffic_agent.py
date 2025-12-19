class TrafficAgent:

    def __init__(self):
        pass

    def judge_level(self, vehicles):
        if vehicles < 50:
            return "一级（畅通）"
        elif vehicles < 150:
            return "二级（轻度）"
        elif vehicles < 300:
            return "三级（中度）"
        else:
            return "四级（严重）"

    def make_decision(self, vehicles):
        level = self.judge_level(vehicles)

        if level == "一级（畅通）":
            strategy = "维持现状"
        elif level == "二级（轻度）":
            strategy = "开放备用通道"
        elif level == "三级（中度）":
            strategy = "错峰放学 + 引导分流"
        else:
            strategy = "启动应急方案 + 周边协同"

        return level, strategy

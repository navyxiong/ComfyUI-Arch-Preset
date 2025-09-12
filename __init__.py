import comfy
import nodes
from nodes import MAX_RESOLUTION

class KontextArchPresetMain:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "时间": (["无", "清晨", "正午", "黄昏", "夜晚"], {"default": "无"}),
                "天气": (["无", "晴天", "阴天", "雨天", "雪天", "雾天"], {"default": "无"}),
                "建筑结构": (["无", "混凝土结构", "钢结构", "木结构", "网架结构", "膜结构"], {"default": "无"}),
                "建筑材料": (["无", "混凝土外墙", "玻璃幕墙", "木板外墙", "铝板外墙", "石材外墙"], {"default": "无"}),
                "周边环境": ([
                    "无", "城市街景", "商业中心", "住宅区", 
                    "校园", "工业区", "历史街区", "公园",
                    "乡村", "水边", "山地", "树林", "海滨",         
                ], {"default": "无"}),
                "玻璃效果": (["无", "镜面玻璃", "玻璃内透", "内透灯光"], {"default": "无"}),
                "天空效果": (["无云", "少云", "多云"],  {"default": "无"}),
                "custom_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Kontext建筑风格预设"

    def generate_prompt(self, 时间, 天气, 建筑结构, 建筑材料, 周边环境, 玻璃效果, 天空效果, custom_prompt=""):
        prompt_parts = []
        
        # 时间描述
        if 时间 == "清晨":
            prompt_parts.append("early morning, blue sky")
        elif 时间 == "正午":
            prompt_parts.append("midday, light blue sky")
        elif 时间 == "黄昏":
            prompt_parts.append("dusk, golden hour, indoor light")
        elif 时间 == "夜晚":
            prompt_parts.append("night-time, dark blue sky, warm indoor light")

        # 天气描述
        if 天气 == "晴天":
            prompt_parts.append("sunny day")
        elif 天气 == "阴天":
            prompt_parts.append("overcast")
        elif 天气 == "雨天":
            prompt_parts.append("rainy day, raining, person holding umbrella")
        elif 天气 == "雪天":
            prompt_parts.append("snowing day, buildings&floor&plants are covered in snow")
        elif 天气 == "雾天":
            prompt_parts.append("a foggy day")
  
        # 建筑结构
        if 建筑结构 == "混凝土结构":
            prompt_parts.append("concrete structure building")
        elif 建筑结构 == "钢结构":
            prompt_parts.append("steel structure building")
        elif 建筑结构 == "木结构":
            prompt_parts.append("wood frame construction")
        elif 建筑结构 == "网架结构":
            prompt_parts.append("grid structure building")
        elif 建筑结构 == "膜结构":
            prompt_parts.append("membrane structure building")

        # 建筑材料
        if 建筑材料 == "混凝土外墙":
            prompt_parts.append("concrete exterior wall")
        elif 建筑材料 == "石材外墙":
            prompt_parts.append("marble wall, meticulously crafted stonework")
        elif 建筑材料 == "铝板外墙":
            prompt_parts.append("aluminum panels exterior wall")
        elif 建筑材料 == "玻璃幕墙":
            prompt_parts.append("glass curtain wall, glass reflects the surrounding environment")
        elif 建筑材料 == "红砖外墙":
            prompt_parts.append("red brick exterior wall")
        elif 建筑材料 == "灰砖外墙":
            prompt_parts.append("gray brick exterior wall")
        elif 建筑材料 == "石头外墙":
            prompt_parts.append("natural stone wall, rugged and organic texture, irregularly shaped stones")
        elif 建筑材料 == "木饰面板外墙":
            prompt_parts.append("wooden decorative panel exterior wall")

        # 周边环境
        if 周边环境 == "城市街景":
            prompt_parts.append("urban Street Scene, motor vehicles, pedestrians")
        elif 周边环境 == "商业中心":
            prompt_parts.append("fields on a commercial area, good commercial atmosphere")
        elif 周边环境 == "住宅区":
            prompt_parts.append("fields on a residential area, beautiful green environment")
        elif 周边环境 == "校园":
            prompt_parts.append("fields on a campus, students")
        elif 周边环境 == "工业区":
            prompt_parts.append("fields on a industrial zone, surrounded by factory buildings")
        elif 周边环境 == "历史街区":
            prompt_parts.append("fields on a traditional Chinese Historical District")
        elif 周边环境 == "公园":
            prompt_parts.append("park, trees, plants, lush, bush")
        elif 周边环境 == "乡村":
            prompt_parts.append("fields on a seaside, white sand beach, sea")
        elif 周边环境 == "水边":
            prompt_parts.append("waterfront space, revetment, water surface reflects the surrounding environment")
        elif 周边环境 == "山地":
            prompt_parts.append("fields on a hill, the background is mountains")
        elif 周边环境 == "树林":
            prompt_parts.append("fields on a forest, the background is forest")
        elif 周边环境 == "海滨":
            prompt_parts.append("fields on a seaside, white sand beach, sea")

        # 玻璃效果
        if 玻璃效果 == "镜面玻璃":
            prompt_parts.append("The glass of the glass curtain wall strongly reflects")
        elif 玻璃效果 == "玻璃内透":
            prompt_parts.append("clear view into interior, transparent glass windows")
        elif 玻璃效果 == "内透灯光":
            prompt_parts.append("interior lighting through glass, illuminated interiors")

        # 天空效果
        if 天空效果 == "无云":
            prompt_parts.append("clean sky, no cloud")
        elif 天空效果 == "少云":
            prompt_parts.append("sky with few clouds")
        elif 天空效果 == "多云":
            prompt_parts.append("cloudy sky")
         
        if custom_prompt:
            prompt_parts.append(custom_prompt)
            
        full_prompt = ", ".join(prompt_parts)
        return (full_prompt,)

NODE_CLASS_MAPPINGS = {
    "KontextArchPresetMain": KontextArchPresetMain
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KontextArchPresetMain": "Kontext建筑风格预设"
}






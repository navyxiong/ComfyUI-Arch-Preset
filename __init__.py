import comfy
import nodes
from nodes import MAX_RESOLUTION

class KontextArchPresetMain:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "time": (["无", "清晨", "正午", "黄昏", "夜晚"], {"default": "无"}),
                "weather": (["无", "晴天", "阴天", "雨天", "雪天", "雾天", "多云"], {"default": "无"}),
                "structure": (["无", "混凝土结构", "钢结构", "木结构", "网架结构", "膜结构"], {"default": "无"}),
                "material": (["无", "混凝土外墙", "玻璃幕墙", "木板外墙", "铝板外墙", "石材外墙"], {"default": "无"}),
                "surrounding": ([
                    "无", "城市街景", "商业中心", "住宅区", 
                    "校园", "工业区", "历史街区", "公园",
                    "乡村", "水边", "山地", "树林", "海滨",         
                ], {"default": "无"}),
                "glass": (["无", "镜面玻璃", "玻璃内透", "内透灯光"], {"default": "无"}),
                "custom_prompt": ("STRING", {"multiline": True, "default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Kontext建筑风格预设"

    def generate_prompt(self, time, weather, structure, material, surrounding, glass, custom_prompt):
        prompt_parts = []
        
        # 时间描述
        if time == "清晨":
            prompt_parts.append("early morning, blue sky")
        elif time == "正午":
            prompt_parts.append("midday, light blue sky")
        elif time == "黄昏":
            prompt_parts.append("dusk, golden hour, indoor light")
        elif time == "夜晚":
            prompt_parts.append("night-time, dark blue sky, warm indoor light")

        # 天气描述
        if weather == "晴天":
            prompt_parts.append("sunny day, clean sky, architectural shadows")
        elif weather == "阴天":
            prompt_parts.append("overcast, cloudy sky")
        elif weather == "雨天":
            prompt_parts.append("rainy day, wet floor, person holding umbrella")
        elif weather == "雪天":
            prompt_parts.append("snowing day, building&floors&plants are covered in snow")
        elif weather == "雾天":
            prompt_parts.append("a foggy day")
        elif weather == "多云":
            prompt_parts.append("cloudy, cloudy sky")

        # 建筑结构
        if structure == "混凝土结构":
            prompt_parts.append("concrete structure building")
        elif structure == "钢结构":
            prompt_parts.append("steel structure building")
        elif structure == "木结构":
            prompt_parts.append("wood frame construction")
        elif structure == "网架结构":
            prompt_parts.append("grid structure building")
        elif structure == "膜结构":
            prompt_parts.append("membrane structure building")

        # 建筑材料
        if material == "混凝土外墙":
            prompt_parts.append("concrete exterior wall")
        elif material == "石材外墙":
            prompt_parts.append("marble wall, meticulously crafted stonework...")
        elif material == "铝板外墙":
            prompt_parts.append("aluminum panels exterior wall...")
        elif material == "玻璃幕墙":
            prompt_parts.append("glass curtain wall, glass reflects the surrounding environment...")

        # 周边环境
        if surrounding == "城市街景":
            prompt_parts.append("urban Street Scene, motor vehicles, pedestrians")
        elif surrounding == "海滨":
            prompt_parts.append("fields on a seaside, white sand beach, sea")
        # ...其他环境描述保持不变...

        # 玻璃效果
        if glass == "镜面玻璃":
            prompt_parts.append("The glass of the glass curtain wall strongly reflects...")
        elif glass == "玻璃内透":
            prompt_parts.append("clear view into interior, transparent glass windows...")
        elif glass == "内透灯光":
            prompt_parts.append("interior lighting through glass, illuminated interiors...")
         
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


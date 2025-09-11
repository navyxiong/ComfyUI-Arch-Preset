import comfy
import nodes
from nodes import MAX_RESOLUTION

class KontextArchPresetMain:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "time": (["无", "清晨", "正午", "黄昏", "夜晚"], {"default": "无"}),
                "weather": (["无", "晴天", "阴天", "雨天", "雪天", "雾天"], {"default": "无"}),
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

def generate_prompt(self, time, weather, structure, material, surrounding, custom_prompt):
    prompt_parts = []
    
    # 添加时间对应的英文描述
    if time == "清晨":
        prompt_parts.append("early morning, blue sky")
    elif time == "正午":
        prompt_parts.append("midday, light blue sky")
    elif time == "黄昏":
        prompt_parts.append("dusk, golden hour, indoor light")
    elif time == "夜晚":
        prompt_parts.append("night-time, dark blue sky, warm indoor light")

    # 添加天气对应的英文描述
    if weather == "晴天":
        prompt_parts.append("sunny day, clean sky, architectural shadows")
    elif weather == "阴天":
        prompt_parts.append("overcast, cloudy sky")
    elif weather == "雨天":
        prompt_parts.append("rainy day, wet floor, person holding umbrella")
    elif weather == "雪天":
        prompt_parts.append("snowing day, buildings, floors, and plants covered in snow")
    elif weather == "雾天":
        prompt_parts.append("a foggy day")
    elif weather == "多云":
        prompt_parts.append("cloudy, cloudy sky")

    # 添加建筑结构形式对应的英文描述
    if weather == "混凝土结构":
        prompt_parts.append("concrete structure building")
    elif weather == "钢结构":
        prompt_parts.append("steel structure building")
    elif weather == "木结构":
        prompt_parts.append("wood frame construction")
    elif weather == "网架结构":
        prompt_parts.append("grid structure building")
    elif weather == "膜结构":
        prompt_parts.append("membrane structure building")

    # 添加建筑材料对应的英文描述
    if weather == "混凝土外墙":
        prompt_parts.append("concrete exterior wall")
    elif weather == "石材外墙":
        prompt_parts.append("marble wall, meticulously crafted stonework, polished and smooth surface, elegant and luxurious texture, symmetrical and orderly stone arrangement, high-quality marble finish, refined and uniform patterns, seamless joints, clean and precise lines, rich and natural veining, durable and sophisticated appearance, premium materials")
    elif weather == "铝板外墙":
        prompt_parts.append("aluminum panels exterior wall, aluminum plate diffuse reflection surrounding environment")
    elif weather == "红砖外墙":
        prompt_parts.append("red brick exterior wall")
    elif weather == "灰砖外墙":
        prompt_parts.append("gray brick exterior wall")
    elif weather == "木饰面板外墙":
        prompt_parts.append("wooden decorative panel exterior wall")
    elif weather == "石头外墙":
        prompt_parts.append("natural stone wall, rugged and organic texture, irregularly shaped stones, carefully stacked and balanced, earthy and weathered appearance, authentic and timeless look, seamless integration with the environment, rich and natural color variations, rough-hewn surfaces, hand-crafted stone arrangement, sturdy and enduring structure")
    elif weather == "玻璃幕墙":
        prompt_parts.append("glass curtain wall, glass reflects the surrounding environment, indoor scene through the glass")

    # 添加周边环境对应的英文描述
    if weather == "城市街景":
        prompt_parts.append("urban Street Scene, motor vehicles, pedestrians")
    elif weather == "公园":
        prompt_parts.append("park, trees, plants, lush, bush")
    elif weather == "水边":
        prompt_parts.append("waterfront space, revetment, water surface reflects the surrounding environment")
    elif weather == "山地":
        prompt_parts.append("fields on a hill, the background is mountains")
    elif weather == "树林":
        prompt_parts.append("fields on a forest, the background is forest")
    elif weather == "工业区":
        prompt_parts.append("fields on a industrial zone, surrounded by factory buildings")
    elif weather == "历史街区":
        prompt_parts.append("fields on a traditional Chinese Historical District")
    elif weather == "海滨":
        prompt_parts.append("fields on a seaside, white sand beash, sea")
    elif weather == "乡村":
        prompt_parts.append("fields on a countryside farmland landscape, expansive fields,harmonious connection with nature")
    elif weather == "商业中心":
        prompt_parts.append("fields on a commercial area, through the glass on the ground floor of the building, one can see the shops, cafes, and restaurants inside, good commercial atmosphere")
    elif weather == "住宅区":
        prompt_parts.append("fields on a residential area, beautiful green environment")
    elif weather == "校园":
        prompt_parts.append("fields on a campus, students")

    # 添加玻璃对应的英文描述
    if weather == "镜面玻璃":
        prompt_parts.append("The glass of the glass curtain wall strongly reflects the surrounding environment, mirror glass")
    elif weather == "玻璃内透":
        prompt_parts.append("clear view into interior, transparent glass windows, softly illuminated interiors, detailed and well-lit indoor spaces, visible furniture arrangements, modern and elegant interior design, warm and inviting lighting, reflections on glass surfaces, seamless blend of interior and exterior, high visibility through windows, subtle glow from indoor lights, sharp and clear indoor details, true-to-life interior atmosphere, ambient light spilling through glass")
    elif weather == "内透灯光":
        prompt_parts.append("interior lighting through glass, illuminated interiors, warm glow, clear glass, light streaming out, soft ambient lighting, transparent windows, interior light reflections, cozy illumination, detailed lighting effects, visible light sources, night-time ambiance, diffused light, inviting warmth, translucent surfaces, high clarity, bright interior lights, soft shadows, radiant glow")
         
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

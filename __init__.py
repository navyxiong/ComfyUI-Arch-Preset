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
                    "无", "城市街景", "公园", "水边", "山地", 
                    "树林", "工业区", "历史街区", "海滨", "乡村",
                    "商业中心", "住宅区", "校园"
                ], {"default": "无"}),
                "custom_prompt": ("STRING", {"multiline": True, "default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Kontext建筑风格预设"

    def generate_prompt(self, time, weather, structure, material, surrounding, custom_prompt):
        prompt_parts = []
        if time != "无":
            prompt_parts.append(f"时间: {time}")
        if weather != "无":
            prompt_parts.append(f"天气: {weather}")
        if structure != "无":
            prompt_parts.append(f"建筑结构: {structure}")
        if material != "无":
            prompt_parts.append(f"建筑材料: {material}")
        if surrounding != "无":
            prompt_parts.append(f"周边环境: {surrounding}")
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

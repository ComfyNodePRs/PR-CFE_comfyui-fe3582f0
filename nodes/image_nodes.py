import comfy
import torch
import math
from .cfe_utils import find_lowest_64

class CFE_Aspect_Ratio:
    """
        Creates an empty latent image that will more easily characterize the resolution process for SD1.5, SDXL, and FLUX
    """
    def __init__(self):
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "type" : (["square", "portrait (w:h)", "landscape (h:w)"],),
                "resolution": ([
                    "1:1",
                    "2:3", 
                    "3:4", 
                    "4:7",
                    "7:9",
                    "8:15",
                    "9:16",
                    "9:21",
                ],),
                "megapixel": (["1 MP (SDXL)", "2 MP (FLUX)", ".5 MP (SD1.5)"],),
                "clip_size": ("FLOAT", {
                    "default": 1.0,
                    "min": 1.0,
                    "max": 10.0,
                    "step": 0.5,
                    "tooltip": "Multiplies the output width and height values",
                    "lazy" : True
                }),
                "batch_size": ("INT", {
                    "default": 1, 
                    "min": 1, 
                    "max": 4096, 
                    "tooltip": "The number of latent images in the batch.",
                    "lazy" : True
                }),
            },
        }

    RETURN_TYPES = ("LATENT","INT","INT")
    RETURN_NAMES = ("latent", "clip_width","clip_height")

    FUNCTION = "calculate_resolution"

    CATEGORY = "CFE/image"

   

    def calculate_resolution(self, type, resolution, megapixel, clip_size, batch_size):

        if type == "square":
            ratio = 1
        else:
            colon = resolution.find(":")
            res0 = float(resolution[:colon])
            res1 = float(resolution[colon + 1:])
            ratio = res1/ res0
        
        mp_mark = megapixel[:1]

        if mp_mark == "1":
            mp = 1024 * 1024
        elif mp_mark == "2":
            mp = 2 * 1024 * 1024
        else:
            mp = 512 * 512

        large = int(math.sqrt(math.floor(ratio * mp)))
        large = find_lowest_64(large)
        
        small =  int(large / ratio)
        small =  find_lowest_64(small)
        
        if type.find("portrait") == -1:
            clip_width = large
            clip_height = small
        else:
            clip_width = small
            clip_height = large

        latent = torch.zeros([batch_size, 4, clip_height // 8, clip_width // 8], device=self.device)

        clip_width *= clip_size
        clip_width = find_lowest_64(clip_width)
        clip_height *= clip_size
        clip_height = find_lowest_64(clip_height)



        return ({"samples":latent}, clip_width, clip_height)
    
# from .mine_nodes import *
from .nodes.flux_nodes import *
from .nodes.image_nodes import *
from .nodes.sampling_nodes import *
from .nodes.lora_nodes import *

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "CFE Aspect Ratio" : CFE_Aspect_Ratio,
    "CFE Flux In Pipe" : CFE_Flux_In_Pipe,
    "CFE Flux Out Pipe" : CFE_Flux_Out_Pipe,
    "CFE FLUX Guidance" : CFE_Flux_Guidance,
    "CFE FLUX Sampler (Pipe)" : CFE_FLUX_Pipe_Sampler,
    "CFE FLUX Sampler" : CFE_FLUX_Sampler,
    "CFE Lora Params" : CFE_Lora_Params,
    "CFE Scheduler" : CFE_Scheduler,
    "CFE Sigma Sampler" : CFE_Sigma_Scheduler,
    "CFE Sigma Sampler Strings" : CFE_Sigma_Sampler_Strings,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CFE_Aspect_Ratio":"CFE Aspect Ratio",
    "CFE_Flux_In_Pipe":"CFE Flux In Pipe",
    "CFE_Flux_Out_Pipe":"CFE Flux Out Pipe",
    "CFE_Flux_Guidance":"CFE Flux Guidance",
    "CFE_FLUX_Pipe_Sampler":"CFE Flux Sampler (Pipe)",
    "CFE_FLUX_Sampler":"CFE Flux Sampler",
    "CFE_Lora_Params":"CFE Lora Params",
    "CFE_Scheduler":"CFE Scheduler",
    "CFE_Sigma_Scheduler":"CFE Sigma Sampler",
    "CFE_Sigma_Sampler_Strings":"CFE Sigma Sampler Strings",
}

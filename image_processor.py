from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import torch

def process_image(image_path):
    processor = AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct")
    model = AutoModelForImageTextToText.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct")

    conversation = [
        {
            "role": "user",
            "content":[
                {"type": "image", "url": image_path},
                {"type": "text", "text": "Describe this image in detail."}
            ]
        }
    ]

    inputs = processor.apply_chat_template(
        conversation,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    output_ids = model.generate(**inputs, max_new_tokens=400)
    generated_texts = processor.batch_decode(output_ids, skip_special_tokens=True)
    print("OUTPUT==>",generated_texts)
    return generated_texts


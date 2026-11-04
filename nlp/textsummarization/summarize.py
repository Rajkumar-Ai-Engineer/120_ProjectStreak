from transformers import T5Tokenizer,T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained("t5-base")

text = ""

inputids = tokenizer("summarize:" + text,return_tensors = "pt",truncation=True,max_length=512).inputids

output_ids = model.generate(inputs=inputids)

summary = tokenizer.decode(output_ids[0],skip_special_tokens=True)

print(summary)
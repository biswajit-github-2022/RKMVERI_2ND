from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Downloading the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

import os
import openai

openai.api_key  = "You're API Ket"

def gpt3_Extact(input, temper=0, eng="text-davinci-002"):
  step_name = "Extract keywords"
  response = openai.Completion.create(
                    engine = eng,
                    prompt = f"{step_name} from : {input}",
                    temperature = temper,
                    top_p = 1.0,
                    max_tokens = 128,
                    )
  sentance = replace_progran(response.choices[0].text)
  prompt = response.usage.prompt_tokens
  total = response.usage.total_tokens
  similar = gpt3_similarity(sentance)
  return sentance, prompt, total, step_name, input, similar
    
def gpt3_reconstruct(input, temper=0.5, eng="text-davinci-002"):
  source = input[0]
  step_name = "Reconstruction sentance"
  response = openai.Completion.create(
                    engine = eng,
                    prompt = f"{step_name} from these keywords : {source}",
                    temperature = temper,
                    top_p = 1.0,
                    max_tokens = 128,
                    )
  sentance = replace_progran(response.choices[0].text) # code in other file
  prompt = response.usage.prompt_tokens
  total = response.usage.total_tokens
  similar = gpt3_similarity(sentance)
  return sentance, prompt, total, step_name, source, similar

def gpt3_similarity(input, eng="text-davinci-002"):
  step_name = "similarity score and semantic similarity score"
  similarity_sentance = f"{original_sentance} and {input}"
  response = openai.Completion.create(
                    engine = eng,
                    prompt = f"Give a {step_name} between: {similarity_sentance}",
                    temperature = 0,
                    top_p = 1.0,
                    max_tokens = 128,
                    )
  output = replace_progran(response.choices[0].text)
  return output

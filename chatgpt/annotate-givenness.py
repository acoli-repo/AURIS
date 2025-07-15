import requests,os,json,sys,argparse

args=argparse.ArgumentParser(description="""request annotation task from ChatGPT, defaults to Givenness Hierarchy in English

Note: We need the system variable CHATGPT_API_KEY to be set.""")

# defaults
instruction_file="initial_prompt.txt"
model="gpt-4o-mini" 
max_input_chars=int(4095*(1.5)) # token limit currently(?) at 4095 tokens, but most tokens are bigrams, I presume, by a conservative estimate, at least 50% of the tokens are bigrams or longer

# args
args.add_argument("files", type=str, nargs="+", help="One or more sentence-split txt files to be annotated; for each file, we send the instructions, first, and disable memory.")
args.add_argument("-i", "--instruction", type=str, nargs="?", help=f"file containaing the instruction prompt, defaults to {instruction_file}. Note: instruction should end with 'Annotate the following text:'", default=instruction_file)
args.add_argument("-m", "--model", type=str, nargs="?", help=f"model, defaults to {model}", default=model)
args.add_argument("-l", "--max_input_chars", type=int, nargs="?", help=f"maximum number of input characters (a conservative estimate is to set to token size * 1.5), if exceeded, we split, defaults to {max_input_chars}", default=max_input_chars)
args.add_argument("-d", "--debug", action="store_true", help="debug mode for post-processing: do not call chatGPT, instead, read json files with chatgpt responses from files")
args=args.parse_args()

# config
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+os.getenv("CHATGPT_API_KEY")
}
interrupt_end="\n(The instructions continue with the next message, do not process any data yet.)"
interrupt_start="(The instructions continue with the following text. Perform annotation only after reading the complete instructions.)\n\n"

INSTRUCTION=None
responses=[]

if args.debug:
    sys.stderr.write("debug mode\n")
    for file in args.files:
        sys.stderr.write(f"reading ChatGPT response from {file}\n")
        sys.stderr.flush()
        with open(file,"rt", errors="ignore") as input:
            responses.append(json.loads(input))
else:
    with open(args.instruction, "rt", errors="ignore") as input:
        sys.stderr.write(f"reading initial prompt from {instruction}\n")
        sys.stderr.flush()
        INSTRUCTION=input.read().strip()
    for file in args.files:
        sys.stderr.write(f"reading input text from {file}\n")
        sys.stderr.flush()
        with open(file,"rt",errors="ignore") as input:
            sentences=input.read().strip().split("\n")
            sentences=[s.rstrip() for s in sentences]
            sentences=[f"{nr+1}\t"+s.strip() for nr,s in enumerate(sentences)]
            last_line=str(len(sentences))

            query=INSTRUCTION+"\n\n"+"\n".join(sentences)
            prompts=[""]
            for line in query.split("\n"):
                if len(prompts[-1]+"\n"+line+"\n"+interrupt_end)>max_input_chars:
                    prompts[-1]+="\n"+interrupt_end
                    prompts.append(interrupt_start.strip()+"\n\n")
                prompts[-1]+="\n"+line
            prompts[-1]+="\n(End of instructions. Perform annotation now.)"

            for prompt in prompts:
                data = {
                    "model": model,
                    "store": True,
                    "messages": [
                        {"role": "user", "content": prompt } ] }

                response = requests.post(url, headers=headers, json=data).json()
                print(json.dumps(response.json()))
                responses.append(json.dumps(response.json()))
                
                while not '{"id":"'+str(last_line)+'"' in  response.json()[-1]["message"]["content"]:
                    data = {
                        "model": model,
                        "store": True,
                        "messages": [
                            {"role": "user", "content": f"Please continue annotation until input line {last_line}" } ] }
                    response = requests.post(url, headers=headers, json=data).json()
                    print(json.dumps(response.json()))
                    responses.append(json.dumps(response.json()))

for response in responses:
    print(response)
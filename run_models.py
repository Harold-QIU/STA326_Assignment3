import subprocess
import logging

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

models = ["GMF", "MLP", "NeuMF-end"]

logging.info("Task 1: Compare Models")

for model in models:
    logging.info(f"Running {model}")
    command = ["python", "main.py", "--factor_num", "8", 
               "--model", model]
    subprocess.run(command)
    
logging.info("Task 2: MLP vs number of layers")
    
model = "MLP"
for num_layers in [0, 1, 2, 3, 4]:
    logging.info(f"Layer number {num_layers}")
    command = ["python", "main.py", "--factor_num", "8", 
               "--model", model, "--num_layers", str(num_layers)]
    subprocess.run(command)
    
logging.info("Task 3: Number of Negatives")

for model in models:
    for num_ng in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        logging.info(f"Running {model} with {num_ng} negatives")
        command = ["python", "main.py", "--factor_num", "8", 
                   "--model", model, "--num_ng", str(num_ng)]
        subprocess.run(command)
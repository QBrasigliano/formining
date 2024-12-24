import csv
import subprocess

# Run find_coins.py
subprocess.run(["python3", "find_coins.py"], check=True)

# Initialize variables
alephium_block_reward = None
alephium_difficulty = None
alephium_price = None

kaspa_block_reward = None
kaspa_difficulty = None
kaspa_price = None

bitcoin_block_reward = None
bitcoin_difficulty = None
bitcoin_price = None

litecoin_block_reward = None
litecoin_difficulty = None
litecoin_price = None

etc_block_reward = None
etc_difficulty = None
etc_price = None

cout_elec = 0.05

results = []

# Read the block rewards from find_coins.csv
with open('find_coins.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        if row['Coin'] == 'alephium':
            alephium_block_reward = float(row['Block Reward'])
            alephium_difficulty = float(row['Difficulty'])
            alephium_price = float(row['Price'])
            
        elif row['Coin'] == 'kaspa':
            kaspa_block_reward = float(row['Block Reward'])
            kaspa_difficulty = float(row['Difficulty'])
            kaspa_price = float(row['Price'])

        elif row['Coin'] == 'ethereum-classic':
            etc_block_reward = float(row['Block Reward'])
            etc_difficulty = float(row['Difficulty'])
            etc_price = float(row['Price'])

        elif row['Coin'] == 'bitcoin':
            bitcoin_block_reward = float(row['Block Reward'])
            bitcoin_difficulty = float(row['Difficulty'])
            bitcoin_price = float(row['Price'])
        
        elif row['Coin'] == 'litecoin':
            litecoin_block_reward = float(row['Block Reward'])
            litecoin_difficulty = float(row['Difficulty'])
            litecoin_price = float(row['Price'])

# Check if all block rewards were found
if alephium_block_reward is None or alephium_difficulty is None or alephium_price is None:
    raise ValueError("Difficulty for alephium not found in find_coins.csv")
if kaspa_block_reward is None or kaspa_difficulty is None or kaspa_price is None:
    raise ValueError("Difficulty for kaspa not found in find_coins.csv")
if bitcoin_block_reward is None or bitcoin_difficulty is None or bitcoin_price is None:
    raise ValueError("Difficulty for bitcoin not found in find_coins.csv")
if litecoin_block_reward is None or litecoin_difficulty is None or litecoin_price is None:
    raise ValueError("Difficulty for litecoin not found in find_coins.csv")
if etc_block_reward is None or etc_difficulty is None or etc_price is None:
    raise ValueError("Difficulty for etc not found in find_coins.csv")

# Read the asic.csv file and filter rows with specific algorithms
with open('asic.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        if row['Power']:
            consommation_elec = ((float(row['Power']) * 24) / 1000) * cout_elec
        else:
            consommation_elec = 0  # ou une autre valeur par défaut appropriée
        if row['Algorithm'] == 'ALPH':
            hashrate = float(row['Hashrate'])
            reward = float((((((hashrate * 1e8) * 0.975 / alephium_difficulty) * alephium_block_reward) * alephium_price) * (90/100)) - consommation_elec)
            row['result'] = reward
            if hashrate > 1e12:
                row['hashrate_valable'] = f"{float(hashrate / 1e12)} Th/s"
            elif hashrate > 1e9:
                row['hashrate_valable'] = f"{float(hashrate / 1e9)} Gh/s"
            elif hashrate > 1e6:
                row['hashrate_valable'] = f"{float(hashrate / 1e6)} Mh/s"
            else:
                row['hashrate_valable'] = f"{float(hashrate)} h/s"

            results.append(row)

        elif row['Algorithm'] == 'KAS':
            hashrate = float(row['Hashrate'])
            reward = float((((((hashrate * 1e5) * 1.1 / kaspa_difficulty) * kaspa_block_reward) * kaspa_price) * (90/100)) - consommation_elec)
            row['result'] = reward
            if hashrate >= 1e12:
                row['hashrate_valable'] = f"{float(hashrate / 1e12)} Th/s"
            elif hashrate >= 1e9:
                row['hashrate_valable'] = f"{float(hashrate / 1e9)} Gh/s"
            elif hashrate >= 1e6:
                row['hashrate_valable'] = f"{float(hashrate / 1e6)} Mh/s"
            else:
                row['hashrate_valable'] = f"{float(hashrate)} h/s"

            results.append(row)

        if row['Algorithm'] == 'BTC':
            hashrate = float(row['Hashrate'])

            reward = float((((((hashrate * 1e-5) * 2 / bitcoin_difficulty) * bitcoin_block_reward) * bitcoin_price) * (90/100)) - consommation_elec)
            row['result'] = reward
            if hashrate >= 1e12:
                row['hashrate_valable'] = f"{float(hashrate / 1e12)} Th/s"
            elif hashrate >= 1e9:
                row['hashrate_valable'] = f"{float(hashrate / 1e9)} Gh/s"
            elif hashrate >= 1e6:
                row['hashrate_valable'] = f"{float(hashrate / 1e6)} Mh/s"
            else:
                row['hashrate_valable'] = f"{float(hashrate)} h/s"

            results.append(row)

        elif row['Algorithm'] == 'LTC':
            hashrate = float(row['Hashrate'])
            reward = float((((((hashrate / 1e7) * 1.75 / litecoin_difficulty) * litecoin_block_reward) * litecoin_price) * (90/100)) - consommation_elec)
            row['result'] = reward
            if hashrate >= 1e12:
                row['hashrate_valable'] = f"{float(hashrate / 1e12)} Th/s"
            elif hashrate >= 1e9:
                row['hashrate_valable'] = f"{float(hashrate / 1e9)} Gh/s"
            elif hashrate >= 1e6:
                row['hashrate_valable'] = f"{float(hashrate / 1e6)} Mh/s"
            else:
                row['hashrate_valable'] = f"{float(hashrate)} h/s"

            results.append(row)

        elif row['Algorithm'] == 'ETC':
            hashrate = float(row['Hashrate'])
            reward = float((((((hashrate / 1e7) * 1.75 / etc_difficulty) * etc_block_reward) * etc_price) * (90/100)) - consommation_elec)
            row['result'] = reward
            if hashrate >= 1e12:
                row['hashrate_valable'] = f"{float(hashrate / 1e12)} Th/s"
            elif hashrate >= 1e9:
                row['hashrate_valable'] = f"{float(hashrate / 1e9)} Gh/s"
            elif hashrate >= 1e6:
                row['hashrate_valable'] = f"{float(hashrate / 1e6)} Mh/s"
            else:
                row['hashrate_valable'] = f"{float(hashrate)} h/s"

            results.append(row)

# Write the results to asic_result.csv with the new "result" and "hashrate_valable" columns
# FILE: find_incomes.py
with open('asic_result.csv', mode='w', newline='') as outfile:
    fieldnames = ['Machine', 'Hashrate', 'hashrate_valable', 'Power', 'Algorithm', 'result']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        # Ensure only the expected fields are written
        filtered_result = {key: result[key] for key in fieldnames}
        # Format the 'result' field to 2 decimal places
        if 'result' in filtered_result:
            filtered_result['result'] = f"{filtered_result['result']:.2f}"
        writer.writerow(filtered_result)
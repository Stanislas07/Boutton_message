import csv
from tkinter.filedialog import askopenfilename
from pathlib import Path
from tkinter import messagebox


def select_and_extract_data(filetype):
    name_path = askopenfilename(filetypes=filetype)
    if not name_path:
        messagebox.showerror("Erreur", "Veuillez sélectionner fichier")
        return None, None
    data = []
    
    with open(name_path,mode='r',encoding='utf-8-sig') as file_in:
        csv_reader = csv.DictReader(file_in, delimiter=';')
        for line in csv_reader:
            data.append(line)   
            
    return data, Path(name_path)


def filter_data(data):
    if not data:
        print("Aucune donnée entrée")
        return None

    filtered_data = []
    name_column = ['COMPTA', 'ANNUL', 'UG', 'INT1', 'INT2', 'CLASSE', 'PRODUIT', 'CLI', 'CLI_NOM', 'POL', 'AVENANT', 'MVT', 'BRV', 'PRIME_HT', 'FRAIS', 'TAXES', 'PRIME_TTC', 'USERP']

    for row in data:
        for i in range(1, 20):     
            vp_key1 = f'VP{i:02d}'
            vp_key2 = f'VP{i}'
            emi_vp_key1 = f'EMI_VP{i}'
            emi_vp_key2 = f'EMI_VP{i:02d}'
    
            if (vp_key1 in row or vp_key2 in row) and (emi_vp_key1 in row or emi_vp_key2 in row) and row.get(vp_key1, row.get(vp_key2, '')) == '28':
                result = {key: row.get(key, '') for key in name_column}
                result['VP28'] = row.get(vp_key1, row.get(vp_key2, ''))
                result['EMI_VP28'] = row.get(emi_vp_key1, row.get(emi_vp_key2, ''))
                result['EFFET'] = row.get('EFFET', '')
                filtered_data.append(result)
                
    return filtered_data

    
    
def negate_amounts(data): 
    for row in data:
        row['EMI_VP28'] = str(-int(row.get('EMI_VP28', '')))
    return data


def Somme_EMI_VP(data):
    somme_EMI = 0
    for row in data:
        somme_EMI += int(row.get('EMI_VP28', ''))
    return somme_EMI    

def save_data(data, output_dir_path):
        with open(output_dir_path,mode='w', encoding='utf-8-sig', newline='') as file_out:
            fieldnames = ['COMPTA','ANNUL','UG','INT1','INT2','CLASSE','PRODUIT','CLI','CLI_NOM','POL','AVENANT','MVT','BRV','PRIME_HT','FRAIS','TAXES','PRIME_TTC','USERP','VP28','EMI_VP28','EFFET']
            writer_csv = csv.DictWriter(file_out, fieldnames=fieldnames, delimiter=';')
            writer_csv.writeheader()
            for d in data:
                writer_csv.writerow(d)


def process_extract_and_save(input_value, negate=False):
    if input_value == "":
        messagebox.showerror("Erreur", "Veuillez entrer un nom de fichier")
        return None, None

    filetype = [('CSV', '.csv')]
    data, input_dir_path = select_and_extract_data(filetype)
    filtered_data = filter_data(data)
    if not negate:
        for row in filtered_data:
            if int(row.get('ANNUL', '')) != 0:
                row['EMI_VP28'] = '0'
                    
    if negate:
        filtered_data = negate_amounts(filtered_data)

    sum_EMI = Somme_EMI_VP(filtered_data)
    output_dir_path = input_dir_path.parent / f"{str(input_value)}.csv"
    save_data(filtered_data, output_dir_path)
    
    return sum_EMI

sum_EMI = 0
sum_EMI_ANNUL = 0
file_more_executed = False
file_less_executed = False


import math
import json
import boto3
import os

# Configuramos el cliente de S3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Obtengo el nombre del bucket y la clave del archivo de entrada desde el evento de S3
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    input_file_path = f"/tmp/{key}"

    # Descargo el archivo .txt de S3 a la instancia temporal de Lambda
    s3_client.download_file(bucket_name, key, input_file_path)

    # Proceso el archivo
    elements, connections = process_file(input_file_path)

    # Genero el archivo .gns3 basado en el procesamiento previo
    output_data = generate_gns_file(elements, connections)
    output_file_path = "/tmp/output.gns3"
    with open(output_file_path, 'w') as file:
        file.write(json.dumps(output_data, indent=4))

    # Especifico el bucket y la clave donde se depositará el archivo .gns3
    output_bucket = 'my-output-bucket'
    output_key = f'processed/{os.path.basename(key).replace(".txt", ".gns3")}'

    # Subo el archivo .gns3 a S3
    s3_client.upload_file(output_file_path, output_bucket, output_key)

    return {
        'statusCode': 200,
        'body': json.dumps('File processed and uploaded successfully')
    }

def process_file(file_path):
    elements = []
    links = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            class_id = int(data[0])
            center_x = float(data[1])
            center_y = float(data[2])
            width = float(data[3])
            height = float(data[4])
            if class_id == 1:
                links.append({'id': f"Link_{len(links)+1}", 'x': center_x, 'y': center_y, 'width': width, 'height': height})
            else:
                element_type = {0: 'DNS', 2: 'Router', 3: 'Switch'}[class_id]
                elements.append({'id': f"{element_type}_{len(elements)+1}", 'x': center_x, 'y': center_y, 'width': width, 'height': height})

    return elements, links

def generate_gns_file(elements, connections):
    project_data = {
        'topology': {
            'nodes': [],
            'links': []
        }
    }
    for element in elements:
        node_data = {
            'id': element['id'],
            'type': element['id'].split('_')[0],
            'x': element['x'],
            'y': element['y'],
            'width': element['width'],
            'height': element['height']
        }
        project_data['topology']['nodes'].append(node_data)
    for link in connections:
        link_data = {
            'id': link['id'],
            'x': link['x'],
            'y': link['y'],
            'width': link['width'],
            'height': link['height']
        }
        project_data['topology']['links'].append(link_data)
    
    return project_data

import boto3

def lambda_handler(event, context):
    
    
    ec2 = boto3.resource('ec2')
    
    instancias = list(ec2.instances.all())
    
    for instancia in instancias:
        print(instancia)
        if instancia.state['Name'] == 'running':
            
            instancia.stop()
            
            
            
    return 0

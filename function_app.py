import azure.functions as func
import logging

#import azure.identity as identity
#import azure.keyvault.secrets as secrets
#from azure.identity import DefaultAzureCredential

from sample_file import say_hello
#from azure.keyvault.secrets import SecretClient

#def get_secret(key_vault_name: str, key_name: str) -> tuple:
#    credential = DefaultAzureCredential()
#    key_client = SecretClient(
#        vault_url=f"https://{key_vault_name}.vault.azure.net/", credential=credential
#    secret = key_client.get_secret(key_name)
#    )
#
#    return secret.properties.content_type, secret.value


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="httpQuick")
def httpQuick(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(say_hello(name))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.route(route="httpSlow")
def httpSlow(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    key_vault = "kv-eus-dev-ndg001"
    secret_name = "sampleSecret"
    content_type, secret = "taco", "bell"
    #content_type, secret = get_secret(key_vault, secret_name)

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This SLOW HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"This SLOW HTTP triggered function executed successfully. secret: {secret}, content: {content_type} Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.route(route="health", methods=["GET"])
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
             "OK",
             status_code=200
        )
import hashlib, os, json
from ape import project, networks
from web3 import Web3
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from base64 import b64decode

# Carregar o contrato FileHashRegistry
contract = project.load_contract("FileHashRegistry")

# Conectar ao nó Ethereum
w3 = networks.provider.w3

# Carregar a ABI do arquivo JSON
with open('./abi/FileHashRegistry.json') as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']

router = APIRouter()


class FileBase64(BaseModel):
    file_base64: str

@router.post("/assign-document")
async def assign_upload_file(file_base64: FileBase64):
    contents = b64decode(file_base64.file_base64)
    file_hash = hashlib.sha256(contents).hexdigest()
    file_name = "file.bin"
    file_size = len(contents)
    
    # Chamar a função registerFileHash do contrato FileHashRegistry
    assignment_result = contract.registerFileHash(file_hash, file_name, file_size, sender=networks.accounts[0])
    
    return {
        "file_hash": file_hash,
        "file_name": file_name,
        "file_size": file_size,
        "transaction_address": assignment_result.txid,
        "timestamp": w3.eth.get_block('latest').timestamp,
        "comment": "Certificado através de ZapSign"
    }

@router.get("/verify-document")
async def verify_document(file_hash: str):
    # Chamar a função getFileEntryByHash do contrato FileHashRegistry
    verification_result = contract.getFileEntryByHash(file_hash)
    
    return {
        "file_name": verification_result[0],
        "file_size": verification_result[1],
        "timestamp": verification_result[2],
        "block_number": verification_result[3],
        "comment": "Certificado através de ZapSign"
    }
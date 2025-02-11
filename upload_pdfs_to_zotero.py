from pyzotero import zotero
import os

# Zotero API credentials
library_id = '15666438'
api_key = 'Jji2SQPgp8nKraPwwQAELRn0'
library_type = 'user'  # Use 'group' if accessing a group library

# Initialize Zotero connection
zot = zotero.Zotero(library_id, library_type, api_key)

# Define the collection name and local directory
collection_name = 'A Lire'
local_directory = r'C:\Users\juliendubois\Desktop\lu'

# Get the collection ID
collections = zot.collections()
collection_id = next((col['key'] for col in collections if col['name'] == collection_name), None)

if collection_id:
    # Get all PDF files in the local directory
    pdf_files = [f for f in os.listdir(local_directory) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(local_directory, pdf_file)

        # Create a new item in Zotero
        item = zot.create_items([{
            'itemType': 'attachment',
            'title': os.path.splitext(pdf_file)[0],
            'linkMode': 'imported_file',
            'contentType': 'application/pdf'
        }])

        # Upload the PDF file
        with open(pdf_path, 'rb') as file:
            zot.attach_file(item['key'], file)

        # Add the item to the collection
        zot.add_to_collection(collection_id, item['key'])

        print(f"Uploaded: {pdf_file}")
else:
    print(f"Collection '{collection_name}' not found.")

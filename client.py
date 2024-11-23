import os
from pymongo import MongoClient

# Kết nối tới MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

# Chọn database và collection
db = client['test']
collection = db['mycollection']

# Thêm tài liệu mới
new_document = { "name": "David", "age": 40, "city": "Da Nang" }
result = collection.insert_one(new_document)
print(f"Inserted document ID: {result.inserted_id}")

# Đọc tài liệu
print("\nAll documents in the collection:")
for doc in collection.find():
    print(doc)

# Cập nhật tài liệu
query = { "name": "David" }
update = { "$set": { "age": 41 } }
updated_result = collection.update_one(query, update)
print(f"\nMatched {updated_result.matched_count} document(s), modified {updated_result.modified_count} document(s).")
# Đọc tài liệu
print("\nAll documents in the collection:")
for doc in collection.find():
    print(doc)
# Xóa tài liệu
delete_query = { "name": "David" }
deleted_result = collection.delete_one(delete_query)
print(f"\nDeleted {deleted_result.deleted_count} document(s).")

# Đọc tài liệu sau khi xóa
print("\nDocuments after deletion:")
for doc in collection.find():
    print(doc)

# Đóng kết nối
client.close()

import json
import csv

def extract_replies_recursive(replies_list, post_id, writer):
    """This function keeps calling itself to dig through infinite layers of replies."""
    if not isinstance(replies_list, list):
        return

    for comment in replies_list:
        # Skip AutoModerator
        if comment.get("author") == "AutoModerator":
            continue
        
        # 1. Save the current comment's body if it exists
        if "body" in comment:
            # We use the 'depth' field if it exists to show how deep the reply is
            depth = comment.get("depth", "Unknown")
            writer.writerow([post_id, f"Reply (Depth {depth})", comment["body"]])
            
        # 2. If this comment has its own replies, dig deeper!
        if "replies" in comment and comment["replies"]:
            extract_replies_recursive(comment["replies"], post_id, writer)

# Load your JSON data
with open('reddit-thread-ixp2s8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a new CSV file to store the extracted bodies
with open('extracted_reddit-thread-ixp2s8.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Write headers for your columns
    writer.writerow(["Post ID", "Type", "Body Text"])
    
    # 1. Grab the main post dictionary safely
    post_data = data.get("post", {})
    post_id = post_data.get("id", "Unknown_ID")
    
    if "body" in post_data:
        writer.writerow([post_id, "Main Post", post_data["body"]])
        
	# 2. Process the top-level comments and all their hidden replies
        comments_list = data.get("comments", [])
        extract_replies_recursive(comments_list, post_id, writer)

print("Done! All nested replies have been successfully extracted.")
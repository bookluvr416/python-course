contents = ['All carrots are to be sliced.',
            'The carrots were sliced appropriately.',
            "I sliced them very fine and in multiple "
            "batches."]

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    file.close()
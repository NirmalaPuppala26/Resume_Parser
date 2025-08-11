from pyresparser import ResumeParser

data = ResumeParser('sample_resume.pdf').get_extracted_data()

print("Extracted Skills:")
print(data.get('skills'))
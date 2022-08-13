

import aspose.words as aw

#load the PDF document from your disc drive (C://Users/USER/document.pdf.....Make sure the PDf document is in this (C://Users/USER/ PATH)

doc = aw.Document("POWER_CV.pdf") 

#save the document to DOCX format
doc.save("POWER_CV.docx")

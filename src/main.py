from docquery import document, pipeline
import gradio as gr


def query(file, input: list):
    """Takes a file and a list of questions and returns a an answer in JSON"""

    # when you run this for the first time, it will pull the model from huggingface hub.
    p = pipeline('document-question-answering')

    # initialize the document object
    doc = document.load_document(file.name)

    # run the document through the pipeline, 
    list = []
    for q in input:
        list.append({
            q: p(question=q, **doc.context)
            })
    
    # return list as structured object
    return list


def doc(file):
    """Called by the Gradio interface. Takes a file and returns a list of answers to preset questions"""

    # check if the file extension is valid
    if file.name.endswith('.pdf') or file.name.endswith(('.jpg', '.jpeg', '.png')):
        
        # if so, run the query on the file with questions. You can ask any question.
        list = query(file, [
            'what is the supplier name?', 
            'what is the invoice total?', 
            'what is the invoice date?', 
            'what is the invoice number?'
            ])

        # return list as structured object
        return list
    
    # else return error (invalid file type) 
    else:
        return 'Invalid file type. Please upload a PDF or image file.'

# define the Gradio interface. Runs on localhost:7860 (web). In production you probably want to use a different API.
demo = gr.Interface(
    fn=doc,
    inputs=[gr.components.File(label='Upload a PDF or image file')],
    outputs=gr.components.Textbox(label='Results'),
    title='Document Query',
    description='Upload a PDF or image file and get answers to common questions about the document.'
)

# run the interface
demo.launch()
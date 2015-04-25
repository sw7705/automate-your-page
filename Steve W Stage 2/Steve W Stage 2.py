Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # The use of Notes and Components terms in this way makes sense to me, not sure about others, but I hope my use and the continuation of that scheme given I used the same references in my HTML and CSS, is not going to cause me extra work or grief in future lessons. 
def generate_notes_HTML(notes_title, components_description):
    html_text_1 = '''
<div class="notes">
    <div class="components">
        ''' + notes_title
    html_text_2 = '''
    </div>
    <div class="components-description">
        ''' + components_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(notes):
    notes_title = notes[0]
    components_description = notes[1]
    return generate_notes_HTML(notes_title, components_description)

SAMPLE_LIST_OF_NOTES = [ ['Webpage', 'A web page is a text document written in a language called HTML. Web browsers read these documents, and then interpret and display them.'],['DOM', 'Document Object Model - The "tree-like" structure comes from the fact that HTML elements can have other elements inside of them.'],['String', 'A string is a sequence of characters surrounded by quotes. The quotes can be either single or double quotes, but the quotes at both ends of the string must be the same type.'] ]


def make_HTML_for_several_notes(list_of_notes):
    HTML = ""
    for notes in list_of_notes:
        notes_HTML = make_HTML(notes)
        HTML = HTML + notes_HTML
    return HTML

print make_HTML_for_several_notes(SAMPLE_LIST_OF_NOTES)

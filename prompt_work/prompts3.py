from langchain import PromptTemplate

template = "Tell me a {adjective} joke about {content}."

prompt_template = PromptTemplate.from_template(template)
prompt_template.input_variables
# -> ['adjective', 'content']
prompt_template.format(adjective="mad", "chickens")
# -> Tell me a funny joke about mad chickens



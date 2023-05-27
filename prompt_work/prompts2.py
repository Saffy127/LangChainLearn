from langchain import PromptTemplate

# An example prompt with no input variables
no_input_prompt = PromptTemplate(input_variables=[], template="Tell me a story about a man trying to escape a single person simulation.")
print(no_input_prompt.format())

# An example prompt with one input variable
one_input_prompt = PromptTemplate(input_variables=["pet_name"], template="Tell me a story about a pet named {pet_name} .")

one_input_prompt.format(pet_name="Skyler")

# An example prompt with multiple input variables
multiple_input_prompt = PromptTemplate(
  input_variables=["adjective", "content"]
  template="Tell me a {adjective} joke about {content}."
)

multiple_input_prompt.format(adjective="sad", content="cars")





                                  

from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain import FewShotPromptTemplate, PromptTemplate

example_formatter_template = """Word: {word}
Antonym: {antonym}
"""
example_prompt = PromptTemplate(
  input_variables=["word", "antonym"],
  template=example_formatter_template,
)

# These are a lot of examples of a pretend task of creating antonyms.
examples = [
  {"word": "happy", "antonym": "sad"},
  {"word": "tall", "antonym": "short"},
  {"word": "energetic", "antonym": "lethargic"},
  {"word": "sunny", "antonym": "gloomy"},
  {"word": "windy", "antonym": "calm"},
]

# We'll use the 'LengthBasedExampleSelector' to select the examples.
example_selector = LengthBasedExampleSelector(
  # These are the examples it has available to choose from.
  examples=examples,
  # This is the PromptTemplate being used to format the examples.
  example_prompt=example_prompt,
  # This is the maximum length that the formatted examples should be
  # Length is measured by the get_text_length function below.
  max_length=25
  # This is the function used to get the length of a string, which is used 
  # to determine which examples to include. It is commented out because
  #it is provided as a default value if none is specified
  # get_text_length: Callable[[str], int] = lambda x: len(re.split("\n| ", x))
)

# We can no use the 'example_selector' to create a 'FewShotPromptTemplate'.
dynamic_prompt = FewShotPromptTemplate(
  # We provide an ExampleSelector insted of examples.
  example_selector=example_selector,
  example_prompt=example_prompt,
  prefix="Give the antonym of every input",
  suffix="Word: {input}\nAntonym:",
  input_variables=["input"],
  example_separator="\n\n",
)


# we can now generate a prompt using the 'format' method.
print(dynamic_prompt.format(input="big"))
# -> Give the antonym of every input
# ->
# -> Word: happy
# -> Antonym: sad
# ->
# -> Word: tall
# -> Antonym: short
# ->
# -> Word: energetic
# -> Antonym: lethargic
# ->
# -> Word: sunny
# -> Antonym: gloomy
# ->
# -> Word: windy
# -> Antonym: calm
# ->
# -> Word: big
# -> Antonym:

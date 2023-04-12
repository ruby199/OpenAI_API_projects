import inspect
import os
from pathlib import Path

import openai

# get your openai API key
openai.api_key = os.getenv('OPENAI_KEY')


def docstring_prompt(code):
    prompt = f"# A high quality python docstring of the above python function:\n\"\"\"\n{code}\n\"\"\""
    return prompt


def merge_docstring_and_function(function_string, docstring):
    split = function_string.split('\n')
    first_part, second_part = split[0], split[1:]
    merged_function = first_part + '\n    """' + docstring + '    """' + '\n'.join(second_part)

    return merged_function


def get_all_functions(module):
    """
    Returns a list of all the functions defined in the specified module.
    """
    return [mem for mem in inspect.getmembers(module, inspect.isfunction)
            if mem[1].__module__ == module.__name__]


def get_openai_completion(prompt):
    response = openai.Completion.create(
        model='text-davinci-002',
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        stop=["\"\"\""]
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    # Change this to the name of your module
    module_name = "example_module"
    
    # Import the module dynamically
    module = __import__(module_name)
    
    all_functions = get_all_functions(module)

    functions_with_prompts = []
    for func in all_functions:
        code = inspect.getsource(func[1])
        prompt = docstring_prompt(code)
        response = get_openai_completion(prompt)

        merged_code = merge_docstring_and_function(code, response)
        functions_with_prompts.append(merged_code)

    with open(f"{module_name}_withdocstring.py", "w") as f:
        f.write('\n\n'.join(functions_with_prompts))

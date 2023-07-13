def add_exclamation_mark(your_function):
  def inner(*args, **kwargs):
    return your_function(*args, **kwargs)
  return inner

@add_exclamation_mark
def greet(name):
  return f'hello {name}'

print(greet('tim'))     # hello tim!
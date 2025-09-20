# Rune

Rune is a markdown like language which can compile down to bytecode to render a terminal CLI

## How Rune compiles

The process is just like any regular programming language and is separated into 4 phases:

- ### Lexer (Tokenization)

- ### Parsing (Building the AST)

- ### Semantic Analysis (Validating the AST)

- ### Execution

## Setup development environment

```shell
    python3 -m venv venv

    source ./venv/bin/activate

    # If requirements NOT up to date
    pip freeze > requirements.txt

    pip install -r requirements.txt
```

## Future implementations

- [ ] Have a live preview editor open up on browser
- [ ] Add custom elements which users can make:
  - Ex: Adding an image
    - importing: `add 'image'` to add an image block
    - to use it would look like: `image[]`
- [ ] Add theme support:
  - Ex: `theme 'name'` to add the theme with specified name

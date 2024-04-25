## Components
- React functional components are functions that return JSX objects (html-like code)
- Rect component names **must be capitalized** to function properly
  - `quot;` can be used as a quotation mark in html to avoid linter errors
- Rules of JSX:
  - Return a single root element: must return a single top-level element, but can wrap multiple child elements in it
    - Can use a React fragment `<>` if you do not want the child elmements to have a container
  - Close all tags
  - camelCase **most** things:
    - Can't use dashes or reserved words like "class"
- Use curly braces {} to reference a dynamic property inside the markup
  - Can also use this to call functions directly in the markup
  - Use curly braces as text or as attributes only in the markup
  - Double curly braces {{ }} are used to contain JacaScript objects

## Rendering
- `.map` method is useful for iterating over an array of data and returning a list of elements
- Use conditional operator "?" to filter returned components based on some criteria
- Keys are used to track specific items in a list
  - If a component in the list has changed, rather than re-rendering the entire list we use a key to only re-render the component that has changed
- [Uuid] (https://www.npmjs.com/package/uuid) package can be used to generate a unique id or key

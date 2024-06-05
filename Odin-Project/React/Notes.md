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
  - [Uuid](https://www.npmjs.com/package/uuid) package can be used to generate a unique id or key
  - Do not generate a unique id for the key during the rendering process, will lead to a new key each render (which defeats the point of a unique key tied to a specific component)

## Properties (Props)
- Data passes from parent to child componenets via props
  - Data flow is unidirectional (data modified in a child will no propogate back to the parent)
- [Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) data objects (props) in Javascript leads to more concise/readable code 
- Default properties can be defined where a explicit prop is absent
  - This can be combined with prop destructuring syntax
- Functions can also be supplied as props as well
- When you nest content inside a JSX tag, the parent component will reieve that content in a prop called "children"
  - Parent does not care what type or content is in the child component, its essentially a hole that is filled by the child (can be simply text too)

## State
- `useState` hook is built-in hook that allows you to define state in a component
  - Syntax: `const [stateValue, setStateValue] = useState(initialValue);`
- Hooks let you use React features and are only available while React is rendering
  - All hooks begin with the "use" prefix
  - Hooks can only be called from the top level of a functional component
  - Cannot be called inside loops or conditionals
- Components can have multiple state variables
  - If they are related, better to combine them into a single state variable that holds an object
    - Must update all variable objects together
    - If you want to update only one, use the syntax: `setPosition({ ...position, x: 100 })`
- [Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure)
- State rendering:
  - Same inputs must always return the same JSX
  - It should not change any objects or variables that existed before rendering
  - "Strict mode" renders each component twice, to catch bugs due to unpredictable or poorly defined behavior
- When updating Objects in state:
  - Must create a new object from the current object's values, update that object's value of interest, and set the state using the new object
  - If we set the state by updating the old object, the page is not guaranteed to re-render!
- Updating nested objects involves making copies of objects all the way up from the part that changed, which can be very verbose
  - Better to make a "flat" or "normalized" structure to make updating nested items easier
  - https://react.dev/learn/choosing-the-state-structure
- Updating a state multiple times in the same event handler using setState(val + 1) will not work
  - The current value is set when the component renders, and is not updated by the setState call, only when the component re-renders
  - To achieve this functionality, pass a callback to the setState function to invoke the state updater function
    - When a callback is passed to the setState function, it ensures that the latest state is passed in as an argument to the callback
- If you want to share state variables between two instances of the same component, that state must be defined in the closest shared parent (called lifting their state up)
  - States are private/local to that component instance, but can be passed to thier children via props
  - Passing event handlers and data as props to the children allows the child component to toggle the state defined in the parent via a button or other event trigger
- Single source of truth:
  - For each piece of state, there is a specific component that holds that piece of information
  - State can be propogated down to child components (when necessary) using props
  - It's often necessary to lift the state up or move it down during development as an application scope grows/changes
  - It’s useful to consider components as “controlled” (driven by props) or “uncontrolled” (driven by state).

## Side Effects
- When components in React need to interact/synchronize with an interface outside of the framework
  - API call to a server for example
- This is accomplished through the `useEffect` hook
- `useEffect` hook runs on every render; but using a dependency array as a second argument allows us to re-render only when those dependencies are changed
  - Leaving the dependency array blank will only run the effect on initial render
  - Can also put in state variables to run effect on initial render or when state variables change
- A cleanup function can be used to run each time before the next effect is ran, and one final time when the component is unmounted
- Do not use an effect when not necessary:
  - Not necessary when caluclating something based on other state variables; just caluclate the value and set it during render
- Lifecycle of a component:
  - A component mounts when it’s added to the screen
  - A component updates when it receives new props or state, usually in response to an interaction
  - A component unmounts when it’s removed from the screen
- Effect lifecycle is independent of component
  - It can either start synchronizing, or later stop synchronizing
  - Body of the effect specifies how to start synchronizing, cleanup function specifies how to stop synchronizing
- Each Effect in your code should represent a separate and independent synchronization process
  - Do not combine effects in order to simplify logic, as dependencies change this could result in unintended synchronizations
- React linter should check taht all reactive values used in the Effect are declared as dependencies

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
- Can use `&&` to conditionally render a section of jsx in the return statement of a component (checking against a boolean flag)

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
  - Transforming data for rendering
  - To handle user events
- Lifecycle of a component:
  - A component mounts when it’s added to the screen
  - A component updates when it receives new props or state, usually in response to an interaction
  - A component unmounts when it’s removed from the screen
- Effect lifecycle is independent of component
  - It can either start synchronizing, or later stop synchronizing
  - Body of the effect specifies how to start synchronizing, cleanup function specifies how to stop synchronizing
- Each Effect in your code should represent a separate and independent synchronization process
  - Do not combine effects in order to simplify logic, as dependencies change this could result in unintended synchronizations
- React linter should check that all reactive values used in the Effect are declared as dependencies
- useRef() is another React hook that stores information that can be retrieved later in the program
  - The major difference from useState is it <ins>does not</ins> trigger a re-render
  - Update or access the ref property through <ref_name>.current
- Cache/memoize expensive computations using the `useMemo` hook
- Generally it is **not** a good idea to set the state inside of an effect, this will cause the entire component to render twice
- Choosing whether to put logic in an Effect or Event Handler:
  - If logic is caused by a particular interaction, keep it in the event handler
  - If it’s caused by the user seeing the component on the screen, keep it in the Effect
- The hook `useSyncExternalStore` can be a more efficient way to sync an external data store with a React component
  - It is also recommended to use a framework's built-in data fetching method rather than implementing Effects for efficiency
- UseEffect can lead to infinite loops in the following scenarios:
  - Using `useEffect` hook to update the state with no dependencies
    - Can also break this loop by using a reference in the `useRef` hook
  - Using objects as dependencies; a change to an object actually creates a new object, leading to rerender
    - Use a specific value of an object as a dependency instead

## Type Checking with PropTypes
- `npm install --save prop-types`
- Can use this to enforce warnings on props that do not match a specified type
- Can also provide default values for props when they are not supplied
- https://legacy.reactjs.org/docs/typechecking-with-proptypes.html
- This is **development only** and will not run in production

## React Router
- Library used to facilitate client-side routing for Single-Page Apss (SPAs)
  - This will allow us to specify components to re-render based on the route (which would not happen otherwise for SPAs)
- A router specifies which componets to render when a route is visited
- A `Link` element can be used in place of the `a` tag to visit a route without refreshing the browser window
- Nested routes can be used in conjunction with `Outlet` to render child components along with the parent
  - `Outlet` will get replaced by the child element specified in the nested route
- A default component can also be added by specifying the `index: true` argument in the children routes
- You can also utilize information from the url route itself within the component using dynamic segments
  - Prefacing part of a route with a ":" indicates that the path after that section is a dynamic segment
  - They can be used in the component with the `useParams()` hook
- An `errorElement` can be used as the default element in case of a bad url
- Generally the routes portion is factored out into its own file
- To pass data from a parent element to its child using `Outlet` we can use the context prop
  - All outlets have a context prop built in
  - We can pass anything to this prop (including objects)
  - To access this state from within any child (or grandchild...) component of the parent, use the `useOutletContext()` hook
- The [`<Navigate />` component](https://reactrouter.com/en/main/components/navigate) can be used to reroute the user to a desire URL or go back down the user's history

## Fetching Data
- `useEffect` can be used to populate component with data upon mounting
- Have ability to set error and loading logic (as shown in API example in SideEffects.js)
- It is often better to lift up the data fetching requests outside of the child component to avoid waterfall requests
  - This can lead to performance impacts where a request is not fired until its parent component is done requesting data and has rendered
  - By moving the request outside of the child and passing the data down as a prop, we can fire all requests simultaneously
- Optimizing performance for data rendering depends on the application
  - Prioritize rendering the most important information first and build application style/loading around that
- Requests have to be managed as browsers are limited to **6 parallel requests** at any given time
- Waterfall requests can be handled by:
  - `Promise.all` can be used to fire multiple requests simultaneously from a high level component and pass the data down as props
    - Can lead to confusing architecture/poor readability
  -  Can also fire requests in parallel and await promises independently to render components as the data becomes available
    -  Drawback to this it will cause the application to rerender multiple times
    -  These approaches also hurt app architecture by not collocating data with the component
  -  Can use data provider pattern to solve this problem: https://www.developerway.com/posts/how-to-fetch-data-in-react#part7.3
  -  Can also move data fetching outside the component and save the data to a const object
    - This will fetch the data before any app renders, and the promise can then be resolved in the `useEffect` hook
    - Drawback to this is the browser limit on number of simultaneous fetch requests
    - Use cases:
      - Pre-fetching critical application data
      - Lazy-loaded components, where fetching is only done when components end up in the render tree
  - Axios and SWR are common fetching libraries that work with React
  - `AbortController` can help avoid race conditions in `useEffect`
    - Race conditions occur due to network lag, where responses may return in a different order than they were requested, leading to inconsistencies
    - `AbortController` will cancel requests before subsequent ones are initiated (example shown in SideEffects.js)

## Styling in React
- [CSS modules](https://www.makeuseof.com/react-components-css-modules-style/) allow locally scoped style classes to avoid name collisions
  - They also provide the ability to extend css classes in other css classes using "compose" key word
- JavaScript extends css and allows us to write styling logic based on state directly in the program
  - [styled-components](https://styled-components.com/) is a common solution
  - [CSSm utility frameworks](https://tailwindcss.com/) are made to work with React/jsx
- Component libraries like [Material UI](https://mui.com/) provide styled components for direct use
  - Some examples include:  dropdowns, drawers, calendars, toggles, and tabs
- Sass provides additional features to add to CSS
- Performance concerns:
  - The more CSS, the longer the page takes to render on the first paint
  - Large css libraries that contain unused styles can further impact performance
  - Partitioning the styles into local css modules along with its respective component can help
  - CSS-in-JS helps with this, but can cause delays due to lack of caching

## Context API
- Used to hold data objects that can reduce the complexity of component-based frameworks
  - Simplifies the process of passing data down to components
  - Helps to eliminate prop "drill down"
- `createContext`: takes in a number, string, or object and returns a context object that can be passed down to components
- `useContext`: retrieve data stored through the createContext call; accepts context object as an argument
- `ContextObject.Provider`: context object comes with Provider component that accepts a prop called value
  - By wrapping child components in `ContextObject.Provider`, it allows the object to be available to the children
  - In the children, call `useContext` to get the data
- Drawbacks:
  - Can lead to performance issues; all components using context re-render when context changes, even if the part of the context they used has not changed
  - Code can be harder to follow if not well organized (less tracability without props)
- Solution: use several smaller contexts instead of one large one

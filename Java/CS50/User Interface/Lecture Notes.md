Single Page Applications:
- entire webage is a single webpage, and user Javascript to modify the DOM (strucutre of the webpage)
- allows us to only modify parts of the page that are changing
- use django and javascript to dynamically load information only when you need it
  - django server stores all information
  - javascript fetches section information from django server and displays it to the user based on user input
- "history.pushState" API to add element to browser history and make changes to the url based on user interaction despite staying on the same webpage 
- "window.onpopstate" to support going "back" on webpage to load previous browser state

Window Object in Javascript:
- window is the physical window screen that displays the webpage
  - window.innerHeight: height of window
  - window.scrollY: how many pixels down you've scrolled
  - window.onscroll: detects when user scrolls
- document is all of the displayed information, which may be larger than a window can fit
  - document.body.offsetHeight: height of entire document 
- using javascript to detect when a user has scrolled to the bottom of the page, we can load the next set of posts and implement an infinite scroll
- shown in scroll.html

Animation:
- css supports animating html features
- can support intermediate frames of the animation using x%
- shown in animate.html
- can further control animations using javascript

More Event Listeners:
- event.target gives information about the target of an event (ie what you clicked on)
- can use <element>.parentElement.remove() to remove parent of that element
  
React:
- javascript library to facilitate interfacing with the user
- defines components that can be used as variables in html and be updated
- include React, ReactDOM, Babel javascript libraries in
  - React: allows us to define components and how they behave
  - ReactDOM: takes react components and inserts them into the DOM of the page
  - Babel: translates between languages (we write react code in jsx, an extension of javascript)
  - illustrated in react.html
  - can create react components and reuse them multiple times rather than type the same html multiple times
  - React.useState(initial value): allows us to set a state of a variable and define a funciton to update that state
  - can combine react states into a javascript object
  - event.target.value sets the value based on an event trigger
  - use spread handler (...state,) in setState as shorthand to skip over parts of the state that aren't being updated

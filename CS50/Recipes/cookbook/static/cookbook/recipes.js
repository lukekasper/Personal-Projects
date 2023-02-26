document.addEventListener('DOMContentLoaded', function() {

    // default load all recipes
    load_recipes();

    // run when search icon is clicked or 'Enter' key is pressed
    document.querySelector('#search-button').addEventListener('click', search_ingredients);
    document.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
          search_ingredients();
        }
    });
});

function load_recipes() {

    // hide recipe view and show all recipes
    document.querySelector('#all_recipes').style.display = 'block';
    document.querySelector('#recipe-view').style.display = 'none';
    document.querySelector('#matched_recipes-view').style.display = 'none';

    // clear all recipes html
    document.querySelector('#all_recipes').innerHTML = '';

    // Send API request to get all posts
    fetch('/all_recipes')
    .then(response => response.json())
    .then(data => {

        // render a div for each post, displaying relevant info
        data["recipes"].forEach(recipe => {

            // run function to generate html
            make_recipe_html(recipe);
        });
    });
}

function make_recipe_html(recipe) {

    // create an outer div for to contain image and post's info
    const outerDiv = document.createElement('div');
    outerDiv.setAttribute('id', 'outer-div');
    outerDiv.innerHTML = '';

    const imageDiv = document.createElement('div');
    imageDiv.setAttribute('id', 'image-div');
    imageDiv.innerHTML = '';

    const infoDiv = document.createElement('div');
    infoDiv.setAttribute('id', 'info-div');
    infoDiv.innerHTML = '';

    // create star rating system
    const stars = document.createElement('p');
    const s1 = document.createElement('span');
    const s2 = document.createElement('span');
    const s3 = document.createElement('span');
    const s4 = document.createElement('span');
    const s5 = document.createElement('span');

    let span_list = [s1, s2, s3, s4, s5];

    // loop through the star spans, and check the number based on the recipe rating
    for (let i=0; i<5; i++) {
        if (i+1 <= Math.round(recipe.rating)) {
            span_list[i].setAttribute('class', 'fa fa-star checked');
        }
        else {
            span_list[i].setAttribute('class', 'fa fa-star');
        }
        span_list[i].setAttribute('id', recipe.title+'_star_'+i);

        span_list[i].addEventListener('mouseover', () => color_stars(recipe.title, i, span_list));
        span_list[i].addEventListener('mouseout', () => uncolor_stars(recipe.title, recipe.rating, span_list));
        span_list[i].addEventListener('click', () => update_rating(recipe.title, i, span_list, recipe.rating));
        stars.append(span_list[i]);
    }

    // make html
    const line_hr = document.createElement('hr');
    const title = make_html_element(recipe.title, 'title', 'p');
    const image = make_image_html(recipe.image, 'image');
    const rating = make_html_element(recipe.rating, recipe.title+'_rating', 'span');

    // append info to outer div
    imageDiv.append(image);
    infoDiv.append(title);
    infoDiv.append(make_html_element("Cuisine: " + recipe.category, 'category', 'p'));
    infoDiv.append(make_html_element(recipe.timestamp, 'timestamp', 'p'));
    infoDiv.append(rating);
    infoDiv.append(stars);
    outerDiv.append(imageDiv);
    outerDiv.append(infoDiv);
    document.querySelector("#all_recipes").append(outerDiv);
    document.querySelector("#all_recipes").append(line_hr);

    // add event listener for poster to change color when moused over
    title.addEventListener('mouseover', () => {title.style.color = "Blue";});
    title.addEventListener('mouseout', () => {title.style.color = "Black";});

    // do the same for for clicking image or title of recipe
    title.addEventListener('click', () => load_recipe(recipe.title));
    image.addEventListener('click', () => load_recipe(recipe.title));
}

// make standard html text element
function make_html_element(text, id, element_type) {

    const element = document.createElement(element_type);
    element.innerHTML = text;
    element.setAttribute('id', id);
    return element
}

// make image html element
function make_image_html(image_src, id) {

    const element = document.createElement('img');
    element.src = image_src;
    element.setAttribute('id', id);
    return element
}

//update rating in django model and style css accordingly
function update_rating(title, i, span_list, rating) {

    // update the rating on the backend
    fetch('/update_rating/'+title, {
        method: 'PUT',
        body: JSON.stringify({
            rating: i+1
        })
    })

    .then(response => response.json())
    .then(data => {

        // update avg rating html for selected recipe
        document.querySelector('#'+title+'_rating').innerHTML = data.avg_rating

        // style stars according to user rating to provide front-end feedback and remove event listener
        for (j=0; j<5; j++) {

            if (j<=i) {
                span_list[j].style.color = 'Blue';
            }
            else {
                span_list[j].style.color = 'Black';
            }
            document.querySelector('#'+title+'_star_'+j).removeEventListener('mouseover', color_stars);
            document.querySelector('#'+title+'_star_'+j).removeEventListener('mouseout', uncolor_stars);
        }

        load_recipes();
    });
}

// color stars when mouse over
function color_stars(title, i, span_list) {

    // style stars according to user rating to provide front-end feedback and remove event listener
    for (j=0; j<5; j++) {

        if (j<=i) {
            span_list[j].style.color = 'RoyalBlue';
        }
        else {
            span_list[j].style.color = 'Black';
        }
    }
}

//uncolor stars when mouse is off stars
function uncolor_stars(title, rating, span_list) {

    // style stars according to user rating to provide front-end feedback and remove event listener
    for (j=0; j<5; j++) {

        if (j<=rating) {
            span_list[j].style.color = 'Orange';
        }
        else {
            span_list[j].style.color = 'Black';
        }
    }
}

// load recipe page
function load_recipe(title) {

    // show user profile view and hide others
    document.querySelector('#all_recipes').style.display = 'none';
    document.querySelector('#recipe-view').style.display = 'block';
    document.querySelector('#matched_recipes-view').style.display = 'none';

    document.querySelector('#recipe-image').innerHTML = '';
    document.querySelector('#recipe-info">?').innerHTML = '';

    // send API request to get recipe info
    fetch('/recipe_page/'+title)
    .then(response => response.json())
    .then(recipe => {

        // add title to page header
        document.querySelector('#recipe-title').innerHTML = recipe.title;

        // create recipe html
        const image = make_image_html(recipe.image, 'recipe-image');
        const poster = make_html_element(recipe.poster, 'recipe-poster', 'p');
        const category = make_html_element(recipe.category, 'recipe-category', 'p');
        const cooktime = make_html_element(recipe.cooktime, 'recipe-cooktime', 'p');
        const timestamp = make_html_element(recipe.timestamp, 'recipe-timestamp', 'p');

        // split strings into lists
        const ingredients_list = recipe.ingredients.split(',');
        const directions_list = recipe.instructions.split(',');
        const notes_list = recipe.note.split(',');

        // make outer list html
        const ing_ul = make_html_element('', 'ing_ul', 'ul');
        const dir_ol = make_html_element('', 'dir_ol', 'ol');
        const notes_ul = make_html_element('', 'notes_ul', 'ul');

        // append ingredients to ul
        ingredients_list.forEach(ingredient => {

            // trim off extra " and ] characters
            ingredient = trim_chars(ingredient);
            ing_ul.append(make_html_element(ingredient, 'ing_li', 'li'));
        })

        // append directions to ol
        directions_list.forEach(direction => {
            direction = trim_chars(direction);
            dir_ol.append(make_html_element(direction, 'dir_li', 'li'));
        })

        // append notes to ul
        notes_list.forEach(note => {

            // if note is not empty
            if (note != '') {
                note = trim_chars(note);
                notes_ul.append(make_html_element(note, 'note_li', 'li'));
            }
        })

        // append recipe info and image to index layout
        document.querySelector("#recipe-image").append(image);
        document.querySelector("#recipe-info").append(poster);
        document.querySelector("#recipe-info").append(category);
        document.querySelector("#recipe-info").append(cooktime);
        document.querySelector("#recipe-info").append(timestamp);
        document.querySelector("#recipe-info").append(ing_ul);
        document.querySelector("#recipe-info").append(dir_ol);
        document.querySelector("#recipe-info").append(notes_ul);
    });
}

// trim off extra characters
function trim_chars(text) {

    // trim off extra " and ] characters
    text = text.slice(1, -1);
    if (text[0] == '"') {
        text = text.slice(1,);
    }
    if (text.charAt(text.length-1) == '"') {
        text = text.slice(0,-1);
    }
    return text
}

// send API request to search for recipes with listed ingredients
function search_ingredients() {

    // get list of ingredients from search input box
    const ing_list = document.querySelector("#search_box").value;

    // send API request to get recipes with listed ingredients
    fetch('/search_recipes', {
        method: 'POST',
        body: JSON.stringify({
            ingredients: `${ing_list}`
        })
    })

    .then(response => response.json())
    .then(data => {

        // show matched recipes view
        document.querySelector('#all_recipes').style.display = 'none';
        document.querySelector('#recipe-view').style.display = 'none';
        document.querySelector('#matched_recipes-view').style.display = 'block';

        // display ingredients in header
        document.querySelector('#ing_header').append(ing_list)


        const rec1 = document.querySelector("#rec1");
        const rec2 = document.querySelector("#rec2");
        rec1.innerHTML = '';
        rec2.innerHTML = '';
        let recipe_num = 0;

        // loop through matched recipes
        data.matched_recipes.forEach(recipe => {

            // make html li elements for recipe and append to matched recipes div
            let recipe_el = make_html_element(recipe, recipe+"_li", "li")

            // split into two columns
            if (recipe_num <= 10) {
                rec1.append(recipe_el);
            }
            else {
                rec2.append(recipe_el);
            }

            recipe_el.setAttribute('class', 'matched_recipe-list');

            // add event listener to link to clicked recipes page and change color when mouseover
            recipe_el.addEventListener('mouseover', () => {recipe_el.style.color = "Blue";});
            recipe_el.addEventListener('mouseout', () => {recipe_el.style.color = "Black";});

            // load that recipes page when name is clicked
            recipe_el.addEventListener('click', () => load_recipe(recipe));
        });
    });
}
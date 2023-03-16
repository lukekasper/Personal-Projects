document.addEventListener('DOMContentLoaded', function() {

    // default load all recipes
    load_recipes(user='', cuisine='');

    // run when username is clicked
    if (document.querySelector('#usrname')) {
        document.querySelector('#usrname').addEventListener('click', () => {
            const usrname = document.querySelector('#name').innerHTML;
            load_recipes(user=usrname, cuisine='');
            history.pushState({}, '', usrname);
        });
    }

    // run when cuisines is clicked
    document.querySelector('#Cuisines-link').addEventListener('click', () => {
        generate_page('Cuisines', '/cuisines', '#cuisines');
        history.pushState({}, '', "categories");
    });

    // run when favorites is clicked
    document.querySelector('#Favoirtes-link').addEventListener('click', () => {
        generate_page('My Favorites', '/favorites', '#favorites');
        history.pushState({}, '', "favorites");
    });

    // run when search icon is clicked
    document.querySelector('#search-button').addEventListener('click', search_recipes);
    if (document.querySelector('#search_box').value != '') {
        document.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
              search_recipes();
            }
        });
    }
});

function generate_page(title, api_path, id) {

    // update page title
    document.querySelector("#recipes-title").innerHTML = title;

     // send API request to get cuisine info
    fetch(`${api_path}`)
    .then(response => response.json())
    .then(data => {

        // show cuisines view and hide all others
        document.querySelector('#all_recipes').style.display = 'none';
        document.querySelector('#recipe-view').style.display = 'none';
        document.querySelector('#matched_recipes-view').style.display = 'none';

        if (title == "Cuisines") {
            document.querySelector('#cuisines-view').style.display = 'block';
            document.querySelector('#favorites-view').style.display = 'none';
        }
        else {
            document.querySelector('#cuisines-view').style.display = 'none';
            document.querySelector('#favorites-view').style.display = 'block';
        }

        // clean div
        document.querySelector(id).innerHTML = '';

        data.list.forEach(object => {

            // set the content depending upon search
            let content = object.title;
            if (title == "Cuisines") {
                content = object;
            }

            // make list html and append to ul
            let element = make_html_element(content, content+'_li', 'li_item', 'li');
            document.querySelector(id).append(element);

            // add event listener to link to clicked recipes page and change color when mouseover
            element.addEventListener('mouseover', () => {element.style.color = "Blue";});
            element.addEventListener('mouseout', () => {element.style.color = "Black";});

            if (title == "Cuisines") {
                // load all recipes with that category
                element.addEventListener('click', () => load_recipes(user='', cuisine=content));
            }
            else {
                // load that recipes page when name is clicked
                element.addEventListener('click', () => load_recipe(content));
            }
        });
    })
}

function load_recipes(user, cuisine) {

    // hide recipe view and show all recipes
    document.querySelector('#all_recipes').style.display = 'block';
    document.querySelector('#recipe-view').style.display = 'none';
    document.querySelector('#matched_recipes-view').style.display = 'none';
    document.querySelector('#cuisines-view').style.display = 'none';
    document.querySelector('#favorites-view').style.display = 'none';

    // clear all recipes html
    document.querySelector('#all_recipes').innerHTML = '';

    // get requested recipes and generate html (user recipes, recipes by cuisine, or all recipes)
    if (user != '') {
        query_recipes('/my_recipes', 'user_recipes', user+"'s Recipes")
    }

    else if (cuisine != '') {
        query_recipes('/cuisine_recipes/'+cuisine, 'cuisine_recipes', '"' + cuisine + '" Recipes')
    }

    else {
        query_recipes('/all_recipes', 'recipes', 'All Recipes')
    }
}

// query recipes and generate html
function query_recipes(api_path, key, title) {

    // Send API request to get recipes
    fetch(`${api_path}`)
    .then(response => response.json())
    .then(data => {

        // render a div for each post, displaying relevant info
        data[key].forEach(recipe => {

            // run function to generate html
            make_recipe_html(recipe);
        });

        // update page title
        document.querySelector('#recipes-title').innerHTML = title;
    });
}

function make_recipe_html(recipe) {

    // create an outer div for to contain image and post's info
    const outerDiv = make_html_element('', 'outer-div_'+recipe.title, 'outer-div', 'div');
    const imageDiv = make_html_element('', 'image-div_'+recipe.title, 'image-div', 'div');
    const infoDiv = make_html_element('', 'info-div_'+recipe.title, 'info-div', 'div');

    // make comments div
    const commentsDiv = make_html_element('', 'comments-div_'+recipe.title, 'comments-div', 'div');
    commentsDiv.append(make_html_element('Comments:', '', 'comments-header', 'h7'));
    commentsDiv.append(make_html_element('', 'comments-inner_'+recipe.title, 'comments-inner', 'div'));

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

    // create comments button
    const comments_button = make_html_element('Show Comments', 'comments-button_'+recipe.title, 'comments-button', 'button');
    comments_button.addEventListener('click', () => show_comments(recipe.comments, recipe.title));

    // make html
    const line_hr = document.createElement('hr');
    const title = make_html_element(recipe.title, 'title_'+recipe.title, 'title', 'p');
    const image = make_image_html(recipe.image, 'image');
    const rating = make_html_element(recipe.rating, recipe.title+'_rating', 'rating', 'span');

    // append info to outer div
    imageDiv.append(image);
    infoDiv.append(title);
    infoDiv.append(make_html_element("Category: " + recipe.category, recipe.title+'_category', 'category', 'p'));
    infoDiv.append(make_html_element(recipe.timestamp, recipe.title+'_timestamp', 'timestamp', 'p'));
    infoDiv.append(rating);
    infoDiv.append(stars);
    infoDiv.append(comments_button);
    outerDiv.append(imageDiv);
    outerDiv.append(infoDiv);
    document.querySelector("#all_recipes").append(outerDiv);
    document.querySelector("#all_recipes").append(commentsDiv);
    document.querySelector("#all_recipes").append(line_hr);

    // default to hiding comments
    document.querySelector('#comments-div_'+recipe.title).style.display = 'none';

    // add event listener for poster to change color when moused over
    title.addEventListener('mouseover', () => {title.style.color = "Blue";});
    title.addEventListener('mouseout', () => {title.style.color = "Black";});

    // do the same for for clicking image or title of recipe
    title.addEventListener('click', () => load_recipe(recipe.title));
    image.addEventListener('click', () => load_recipe(recipe.title));
}

// create html for showing comments section or hiding it
function show_comments(comments, title) {

    if (document.querySelector('#comments-button_'+title).innerHTML == 'Show Comments') {

        // show comments div
        document.querySelector('#comments-div_'+title).style.display = 'block';
        document.querySelector('#comments-inner_'+title).innerHTML = '';

        if (comments != null) {
            comments.forEach(comment => {
                // make html for each comment and append to comments div
                make_comment_html(comment, title);
            });
        }

        // make textarea to add a comment
        const add_comment_box = make_html_element('', 'add_comment-box'+title, 'add_comment_box', 'textarea');
        add_comment_box.setAttribute('placeholder','Add a comment...');
        document.querySelector('#comments-inner_'+title).append(add_comment_box);

        // if the user has something written in the textarea, submit comment when enter key is struck
        if (add_comment_box.value != '') {

            add_comment_box.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') {
                    add_comment(add_comment_box.value, title);
                }
            });
        }

        // change button html
        document.querySelector('#comments-button_'+title).innerHTML = 'Hide Comments';
    }

    else {
        // hide comments div
        document.querySelector('#comments-div_'+title).style.display = 'none';
        document.querySelector('#comments-button_'+title).innerHTML = 'Show Comments'
    }
}

function make_comment_html(comment, title) {
    const comment_p = make_html_element('', 'comment-p_'+comment.id, 'comment-p', 'p');
    const poster = make_html_element(comment.poster + ': ', comment.poster+'comment', 'comment-poster', 'span');
    const comment_txt = make_html_element(comment.comment, 'comment_txt', comment.id, 'span');
    comment_p.append(poster);
    comment_p.append(comment_txt);
    document.querySelector('#comments-inner_'+title).append(comment_p);
}

// update comment model on backend
function add_comment(comment_txt, title) {

    fetch('/add_comment/'+title, {
        method: 'POST',
        body: JSON.stringify({
            comment: `${comment_txt}`
        })
    })

    .then(response => response.json())
    .then(data => {
        make_comment_html(data.comment, title);
    })
}

// make standard html text element
function make_html_element(text, id, cls, element_type) {

    const element = document.createElement(element_type);
    element.innerHTML = text;
    element.setAttribute('id', id);
    element.setAttribute('class', cls);
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

        load_recipes(user='', cuisine='');
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
    document.querySelector('#cuisines-view').style.display = 'none';
    document.querySelector('#favorites-view').style.display = 'none';

    // send API request to get recipe info
    fetch('/recipe_page/'+title)
    .then(response => response.json())
    .then(data => {

        document.querySelector('#recipe-image').innerHTML = '';
        document.querySelector('#recipe-info').innerHTML = '';

        // add title to page header
        document.querySelector('#recipe-title').innerHTML = data.recipe.title;

        // create recipe html
        const image = make_image_html(data.recipe.image, 'recipe-image');
        const poster = make_html_element(data.recipe.poster, 'recipe-poster', '', 'p');
        const category = make_html_element(data.recipe.category, 'recipe-category', '', 'p');
        const cooktime = make_html_element(data.recipe.cooktime, 'recipe-cooktime', '', 'p');
        const timestamp = make_html_element(data.recipe.timestamp, 'recipe-timestamp', '', 'p');

        // split strings into lists
        const ingredients_list = data.recipe.ingredients.split(',');
        const directions_list = data.recipe.instructions.split(',');
        const notes_list = data.recipe.note.split(',');

        // make outer list html
        const ing_ul = make_html_element('', 'ing_ul', '', 'ul');
        const dir_ol = make_html_element('', 'dir_ol', '', 'ol');
        const notes_ul = make_html_element('', 'notes_ul', '', 'ul');

        // append ingredients to ul
        ingredients_list.forEach(ingredient => {

            // trim off extra " and ] characters
            ingredient = trim_chars(ingredient);
            ing_ul.append(make_html_element(ingredient, 'ing_li', '', 'li'));
        })

        // append directions to ol
        directions_list.forEach(direction => {
            direction = trim_chars(direction);
            dir_ol.append(make_html_element(direction, 'dir_li', '', 'li'));
        })

        // append notes to ul
        notes_list.forEach(note => {

            // if note is not empty
            if (note != '') {
                note = trim_chars(note);
                notes_ul.append(make_html_element(note, 'note_li', '', 'li'));
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

        // widget to add/remove recipe from favorites
        if (data.favorite_flag == "None") {

            // hide favorites button if user is not signed in
            document.querySelector('#favorites-div').style.display = 'none';
        }
        else {

            // show favorites button
            document.querySelector('#favorites-div').style.display = 'block';

            // determine if recipe is already in user's favorited list
            if (data.favorite_flag == "True") {
                document.querySelector('#favorites-button').innerHTML = "Remove from Favorites";
            }
            else {
                document.querySelector('#favorites-button').innerHTML = "Add to Favorites";
            }

            // update user's favorites when button is clicked
            document.querySelector('#favorites-button').addEventListener('click', () =>
            update_favorites(data.recipe.title, data.favorite_flag), true);
        }
    });
}

// update user's favorite recipes
function update_favorites(title) {

    // send API request to update user's favorite recipes list
    fetch('/update_favorites/'+title)

    // reload recipe page
    .then(response => response.json())
    .then(data => {
        document.querySelector('#favorites-button').removeEventListener('click', () =>
        update_favorites(title, flag), true);

        // update button logic to opposite state
        if (data.flag == "True") {
            document.querySelector('#favorites-button').innerHTML = "Remove from Favorites";
        }
        else {
            document.querySelector('#favorites-button').innerHTML = "Add to Favorites";
        }
    })
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
function search_recipes() {

    // get list of ingredients from search input box
    const search = document.querySelector("#search_box").value;

    // send API request to get recipes with listed ingredients
    fetch('/search_recipes', {
        method: 'POST',
        body: JSON.stringify({
            search: `${search}`
        })
    })

    .then(response => response.json())
    .then(data => {

        // show matched recipes view
        document.querySelector('#all_recipes').style.display = 'none';
        document.querySelector('#recipe-view').style.display = 'none';
        document.querySelector('#matched_recipes-view').style.display = 'block';
        document.querySelector('#cuisines-view').style.display = 'none';
        document.querySelector('#favorites-view').style.display = 'none';

        document.querySelector("#ul1").innerHTML = '';
        document.querySelector("#ul2").innerHTML = '';

        let rec1 = document.querySelector("#ul1");
        let rec2 = document.querySelector("#ul2");
        let recipe_side = 1;

        // display html block and add search to header
        document.querySelector('#header').innerHTML = search;

        // show matched ingredients view if API request returns elements
        if (data.matched_recipes.length != 0) {

            // loop through matched recipes
            data.matched_recipes.forEach(recipe => {

                // make html li elements for recipe and append to matched recipes div
                let recipe_el = make_html_element(recipe, recipe+'_li', 'matched_recipe-list', 'li');

                // split into two columns
                if (recipe_side == 1) {
                    rec1.append(recipe_el);
                }
                else {
                    rec2.append(recipe_el);
                }

                recipe_side *= -1;

                // add event listener to link to clicked recipes page and change color when mouseover
                recipe_el.addEventListener('mouseover', () => {recipe_el.style.color = "Blue";});
                recipe_el.addEventListener('mouseout', () => {recipe_el.style.color = "Black";});

                // load that recipes page when name is clicked
                recipe_el.addEventListener('click', () => load_recipe(recipe));
            });
        }

        // clear search bar
        document.querySelector('#search_box').value = '';
    });
}
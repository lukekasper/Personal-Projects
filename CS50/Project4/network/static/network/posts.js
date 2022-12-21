document.addEventListener('DOMContentLoaded', function() {

    all_posts_page = 0;
    following_page = 0;
    profile_page = 0;

    // run when post is submitted
    document.querySelector('#new_post-form').onsubmit = () => {
        new_post();
    };

    // default load all posts
    load_posts();

    // run when All Posts is clicked
    document.querySelector('#allPosts-link').addEventListener('click', load_posts);

    // run when Following link is clicked
    document.querySelector('#Following-link').addEventListener('click', () => following_view());

});

// create new post
function new_post() {

    // get info from input field
    const content = document.querySelector('#new_content').value;

    // send POST request to /new_post API
    fetch('/posts', {
        method: 'POST',
        body: JSON.stringify({
            content: `${content}`
        })
    })
    .then(response => response.json())
    .then(response => {
        document.querySelector('#new_content').value = '';
        load_posts();
    })

    return false;
}

function load_posts() {

    // show all posts view and hide others
    document.querySelector('#all_posts-view').style.display = 'block';
    document.querySelector('#profile-view').style.display = 'none';
    document.querySelector('#following-view').style.display = 'none';

    document.querySelector('#all_posts').innerHTML = '';

    // Send API request to get all posts
    fetch('/posts/all')
    .then(response => response.json())
    .then(data => {

        // render a div for each post, displaying relevant info
        data.page_structure[all_posts_page].forEach(post => {

            // run function to generate html
            make_posts_html(post, "all", data.signed_user);
        });

        make_pagination('#all_posts','',data.num_pages);
    });
}

function make_posts_html(post, page, username) {

    // create an outer div for to contain post's info
    const postDiv = document.createElement('div');
    postDiv.setAttribute('id', 'post-div');
    postDiv.innerHTML = '';

    // create paragraph elements to contain the info
    const poster = document.createElement('p');
    poster.innerHTML = post.poster;
    poster.setAttribute('id', 'poster');

    const content = document.createElement('p');
    content.innerHTML = post.content;
    content.setAttribute('id', 'content');

    const timestamp = document.createElement('p');
    timestamp.innerHTML = post.timestamp;
    timestamp.setAttribute('id', 'timestamp');

    const likes_outer = document.createElement('div');
    likes_outer.innerHTML = '';
    likes_outer.setAttribute('id', 'likes_outer');

    const heart = document.createElement('span');
    heart.innerHTML = '&hearts;';
    heart.setAttribute('id', 'heart');
    likes_outer.append(heart);

    const likes = document.createElement('span');
    likes.innerHTML = post.likes;
    likes.setAttribute('id', 'likes');
    likes_outer.append(likes);

    // append info to post div
    postDiv.append(poster);
    postDiv.append(content);
    postDiv.append(timestamp);
    postDiv.append(likes_outer);

    // append html to appropriate page
    if (page == "profile") {
        document.querySelector('#user_posts').append(postDiv);
    }

    else if (page == "following") {
        document.querySelector('#following-posts').append(postDiv);
    }

    else {
        document.querySelector('#all_posts').append(postDiv);
    }

    if (page != "profile") {

        // add event listener for poster to change color when moused over
        poster.addEventListener('mouseover', () => link_style(poster));
        poster.addEventListener('mouseout', () => link_reg(poster));

        // do the same for for clicking to load user's profile page view
        const poster_username = poster.innerHTML
        poster.addEventListener('click', () => load_profile(poster_username));
    }

    // add event listener to like button
    heart.addEventListener('click', () => {

        // send API request to determine if user likes post or not
        fetch(`/like/${post.id}`)
        .then(response => response.json())
        .then(data => {

            // update the number of likes the post has
            likes.innerHTML = data.post.likes

            // update the color of the heart to give feedback
            if (data.liked_flag == true) {
                heart.style.color = "Red";
            }

            else {
                heart.style.color = "Gray";
            }
        })
    })

    // if the post is from the signed-in user, allow ability to edit
    if (post.poster == username) {

        // create an edit button
        const editButton = document.createElement('button');
        editButton.setAttribute('class', 'btn btn-sm btn-outline-primary');
        editButton.setAttribute('id', 'edit-button');
        editButton.innerHTML = "Edit"
        postDiv.append(editButton);

        // run function when button is clicked
        editButton.addEventListener('click', () => edit_post(content, post.content, post.id, editButton));
    }
}

function link_style(poster) {
    poster.style.color = "Blue";
}

function link_reg(poster) {
    poster.style.color = "RoyalBlue";
}

function load_profile(poster_username) {

    // show user profile view and hide others
    document.querySelector('#all_posts-view').style.display = 'none';
    document.querySelector('#profile-view').style.display = 'block';
    document.querySelector('#following-view').style.display = 'none';

    // send API request to get user info
    fetch('/profile/'+poster_username)
    .then(response => response.json())
    .then(user_info => {

        // add username to page header
        document.querySelector('#profile-header').innerHTML = user_info.profile_username;

        // create paragraph elements to contain follower/following info
        document.querySelector('#followers').innerHTML = user_info.follow_info.num_followers
        const followers = document.createElement('span');
        followers.innerHTML = "&nbsp;Followers";
        followers.setAttribute('id', 'followers_text');
        document.querySelector('#followers').append(followers);

        document.querySelector('#following').innerHTML = user_info.follow_info.num_following
        const following = document.createElement('span');
        following.innerHTML = "&nbsp;Following";
        following.setAttribute('id', 'following_text');
        document.querySelector('#following').append(following);

        // clean the user's post div
        document.querySelector('#user_posts').innerHTML = '';

        // run for each of the user's posts
        user_info.page_structure[profile_page].forEach(post => {

            // generate html to display on profile page
            make_posts_html(post, "profile", user_info.signed_user);
        });

        if (user_info.user_relations.signed_in && !user_info.user_relations.no_button) {

            // create button to follow/unfollow user
            const followButton = document.createElement('button');
            followButton.setAttribute('class', 'btn btn-sm btn-outline-primary');
            followButton.setAttribute('id', 'follow-button');

            // determine if signed in user is following profile user to set button logic
            if (!user_info.user_relations.following_flag) {
                followButton.innerHTML = "+&nbsp;Follow";
            }
            else {
                followButton.innerHTML = "-&nbsp;Unfollow";
            }

            // clear the follow button and re-append new button with updated display
            document.querySelector('#follow-div').innerHTML = '';
            document.querySelector('#follow-div').append(followButton);
            document.querySelector('#follow-button').addEventListener('click', () => update_relations(user_info));
        }

        make_pagination('#user_posts',poster_username, user_info.num_pages);
    });
}

function update_relations(user_info) {

    // make a PUT request to add profile user to signed in users following list
    // also will add signed in user to profile users follower list
    fetch('/follower_relation', {
        method: 'PUT',
        body: JSON.stringify({
            follow: user_info.profile_username
        })
    })

    .then(() => {
        load_profile(user_info.profile_username);
    })
    document.querySelector('#follow-button').removeEventListener('click', () => update_relations(user_info));
}

function following_view() {

    document.querySelector('#all_posts-view').style.display = 'none';
    document.querySelector('#profile-view').style.display = 'none';
    document.querySelector('#following-view').style.display = 'block';

    document.querySelector('#following-posts').innerHTML = '';

    // send API request to followers' posts
    fetch('/following')
    .then(response => response.json())
    .then(data => {

        // render a div for each post, displaying relevant info
        data.page_structure[following_page].forEach(post => {

            // run function to generate html
            make_posts_html(post, "following",data.signed_user);
        });
        make_pagination('#following-posts','',data.num_pages);
    })
}

function edit_post(content_element, content, post_id, button) {

    // create a textarea element and form to submit
    const form = document.createElement('form');
    form.setAttribute('id', 'edit-form');

    const text = document.createElement('TEXTAREA');
    text.innerHTML = content;
    text.setAttribute('id', 'edit-text');

    const input = document.createElement('input');
    input.setAttribute('id', 'submit-edit');
    input.setAttribute('class', 'btn btn-primary');
    input.setAttribute('value', 'Submit');
    input.setAttribute('type', 'submit');

    content_element.innerHTML = '';
    form.append(text);
    form.append(input);
    content_element.append(form);

    // run when edit form is submitted
    form.onsubmit = () => {

        new_content = text.value;
        submit_edits(new_content, post_id)
        button.removeEventListener('click', () => edit_post(content_element, new_content, post_id, button));
        return false;
    };
}

function submit_edits(content,post_id) {

    // send POST request to /edit_post API
    fetch("/posts/edit/"+post_id, {
        method: 'PUT',
        body: JSON.stringify({
            content: `${content}`
        })
    })
    .then(response => response.json())
    .then(response => {
        load_posts();
    })
}

function make_pagination(container_id, profile_username, num_pages) {

    // make html for pagination
    const navElement = document.createElement('nav');
    navElement.setAttribute('aria-label', 'nav-container');
    navElement.setAttribute('id', 'nav-id');

    const ulElement = document.createElement('ul');
    ulElement.setAttribute('class', 'pagination justify-content-center');
    ulElement.setAttribute('id', 'pagination-ul');

    const prevElement = document.createElement('li');
    prevElement.setAttribute('class', 'page-item');
    prevElement.setAttribute('id', 'li-prev');

    const prevA = document.createElement('a');
    prevA.setAttribute('class', 'page-link');
    prevA.setAttribute('href', '#');
    prevA.setAttribute('id', 'a-prev');
    prevA.setAttribute('aria-label', 'Previous');
    prevElement.append(prevA);

    const prevIcon = document.createElement('span');
    prevIcon.setAttribute('aria-hidden', 'true');
    prevIcon.setAttribute('id', 'prev');
    prevIcon.innerHTML = "&laquo;";
    prevA.append(prevIcon);

    const nextElement = document.createElement('li');
    nextElement.setAttribute('class', 'page-item');
    nextElement.setAttribute('id', 'li-next');

    const nextA = document.createElement('a');
    nextA.setAttribute('class', 'page-link');
    nextA.setAttribute('href', '#');
    nextA.setAttribute('id', 'a-next');
    nextA.setAttribute('aria-label', 'Next');
    nextElement.append(nextA);

    const nextIcon = document.createElement('span');
    nextIcon.setAttribute('aria-hidden', 'true');
    nextIcon.setAttribute('id', 'next');
    nextIcon.innerHTML = "&raquo;";
    nextA.append(nextIcon);

    ulElement.append(prevElement);
    ulElement.append(nextElement);
    navElement.append(ulElement);
    document.querySelector(`${container_id}`).append(navElement);

    prevIcon.addEventListener('click', () => {
        if (container_id == '#all_posts') {
            if (all_posts_page != 0) {
                all_posts_page--;
                load_posts();
            }
        }

        else if (container_id == '#following-posts') {
            if (following_page != 0) {
                following_page--;
                following_view();
            }
        }

        else {
            if (profile_page != 0) {
                profile_page--;
                load_profile(profile_username);
            }
        }
    });

    nextIcon.addEventListener('click', () => {

        if (container_id == '#all_posts') {
            if (all_posts_page != num_pages-1) {
                all_posts_page++;
                load_posts();
            }
        }

        else if (container_id == '#following-posts') {
            if (following_page != num_pages-1) {
                following_page++;
                following_view();
            }
        }

        else {
            if (profile_page != num_pages-1) {
                profile_page++;
                load_profile(profile_username);
            }
        }
    });
}
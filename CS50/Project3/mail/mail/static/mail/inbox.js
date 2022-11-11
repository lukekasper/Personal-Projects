document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => compose_email(false,{}));

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(reply,email) {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#single-email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    if (reply === false) {
        document.querySelector('#compose-recipients').value = '';
        document.querySelector('#compose-subject').value = '';
        document.querySelector('#compose-body').value = '';
    }
    else {
        // add sender as the recipient of the reply
        document.querySelector('#compose-recipients').value = email.sender;

        // check to see if subject begins with "Re: ", if so do not duplicate it
        if (email.subject.substring(0,4) === 'Re: ') {
            document.querySelector('#compose-subject').value = email.subject;
        }
        else {
            document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
        }

        // add a p element for the previous email header
        document.querySelector('#compose-body').value = `\n\nOn ${email.timestamp} ${email.sender} wrote:\n${email.body}`;
    }

    // run when the compose email form is submitted
    document.querySelector('#compose-form').onsubmit = () => {

        // get info from input fields
        const recipients = document.querySelector('#compose-recipients').value;
        const subject = document.querySelector('#compose-subject').value;
        const body = document.querySelector('#compose-body').value;

        // send POST request to /emails API
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: `${recipients}`,
                subject: `${subject}`,
                body: `${body}`
            })
        })

        // log the response in the console
        .then(response => response.json())
        .then(result => {
            // Print result
            console.log(result);

            // load user's sent mailbox
            load_mailbox('sent');
        });

        return false;
    };
}

function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#single-email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    // Get the appropriate mailbox
    fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
        // Print emails
        console.log(emails);

        // render a div for each email in the inbox, displaying relevant info
        emails.forEach(email => {

            // create an outer div for to contain email's info
            const emailDiv = document.createElement('div');
            emailDiv.setAttribute('id', 'email-div');
            emailDiv.innerHTML = '';


            // create in paragraph elements to contain the info
            const sender = document.createElement('p');
            sender.innerHTML = email.sender;
            sender.setAttribute('id', 'sender');

            const subject = document.createElement('p');
            subject.innerHTML = email.subject;
            subject.setAttribute('id', 'subject');

            const timestamp = document.createElement('p');
            timestamp.innerHTML = email.timestamp;
            timestamp.setAttribute('id', 'timestamp');

            // append info to email div
            emailDiv.append(sender);
            emailDiv.append(subject);
            emailDiv.append(timestamp);
            document.querySelector('#emails-view').append(emailDiv);

            // if email has been read, make background gray
            if (email.read === true) {
                emailDiv.style.backgroundColor = "#E8E8E8";
            }
            else {
                emailDiv.style.backgroundColor = "White";
            }

            // when an email is clicked, call view_email function
            emailDiv.addEventListener('click', function() {
                const id = email.id;
                fetch(`/emails/${id}`)
                .then(response => response.json())
                .then(email => {
                    view_email(email,mailbox);
                });
            });
        });
    });
}

// function to view email and mark as "read"
function view_email(email,mailbox) {
    // Show single-email view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#single-email-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    // call function to create paragraph elements to contain email info
    const emailInfoDiv = document.createElement('div');
    email_info(emailInfoDiv, "From: ", email.sender);
    email_info(emailInfoDiv, "To: ", email.recipients);
    email_info(emailInfoDiv, "Subject: ", email.subject);
    email_info(emailInfoDiv, "Timestamp: ", email.timestamp);
    document.querySelector('#email-info').innerHTML = emailInfoDiv.innerHTML;

    // add email body
    const emailBodyDiv = document.createElement('div');
    email_info(emailBodyDiv, "", email.body);
    document.querySelector('#email-body').innerHTML = emailBodyDiv.innerHTML;

    // mark clicked email as "read"
    fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
    })

    if (mailbox != 'sent') {

        // make button elements for Archive and Unread
        const archiveButton = document.createElement('button');
        archiveButton.setAttribute('class', 'btn btn-sm btn-outline-primary');
        archiveButton.setAttribute('id', 'archive');
        const readButton = document.createElement('button');
        readButton.setAttribute('class', 'btn btn-sm btn-outline-primary');
        readButton.setAttribute('id', 'unread');

        // Display "Archive" or "Unarchive" based on state of email
        archiveButton.innerHTML = email.archived ? "Unarchive" : "Archive";
        readButton.innerHTML = "Mark as Unread";

        document.querySelector('#email-body').append(archiveButton);
        document.querySelector('#email-body').append(readButton);

        // monitor buttons for user selection and run appropriate function
        document.querySelector('#archive').addEventListener('click', () => change_status(email, "archive"));
        document.querySelector('#unread').addEventListener('click', () => change_status(email, "unread"));
    }

    document.querySelector('#reply').addEventListener('click', () => reply(email));
}

// create html elements for email info
function email_info(div, title, content) {

    // create outer p element and inner span elements
    const line = document.createElement('p');
    line.setAttribute('class', 'line');
    const title_span = document.createElement('span');
    const content_span = document.createElement('span');

    // fill content with input parameters
    title_span.innerHTML = title;
    title_span.setAttribute('class', 'title');
    content_span.innerHTML = content;

    // append spans to line element and line to overall email info div
    line.append(title_span);
    line.append(content_span);
    div.append(line);
}

// mark email as archive/unarchive or read/undread
function change_status(email, flag) {

    // if archive button clicked, archive or unarchive email
    if (flag === 'archive') {
        fetch(`/emails/${email.id}`, {
            method: 'PUT',
            body: JSON.stringify({
                archived: !email.archived
            })
        })
        .then(() => {
            load_mailbox('inbox');
        })
        document.querySelector('#archive').removeEventListener('click', () => change_status(email, "archive"));
    }

    // same logic for read
    else {
        fetch(`/emails/${email.id}`, {
            method: 'PUT',
            body: JSON.stringify({
                read: false
            })
        })
        .then(() => {
            load_mailbox('inbox');
        })
        document.querySelector('#unread').removeEventListener('click', () => change_status(email, "unread"));
    }
}

function reply(email) {
    compose_email(true,email);
}
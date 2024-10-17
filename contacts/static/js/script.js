
const params = new URLSearchParams(window.location.search);
const newContactPk = params.get('new_contact_pk');
const updatedContactPk = params.get('updated_contact_pk');
const success = params.get('success');

const alertSuccessNew = `
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                        Success! Your contact has been added.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>`;

const alertSuccessUpdate = `
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                        Success! Your contact has been updated.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>`;


const deletedContactPk = params.get('deleted_contact_pk');
const deleteSuccess = params.get('delete_success');

if (deleteSuccess === "1") {
    const alertSuccessDelete = `
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            Your contact was deleted successfully.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`;
    document.getElementById('contact-content').insertAdjacentHTML('afterbegin', alertSuccessDelete);
    history.replaceState({}, document.title, window.location.pathname);
}

if (deleteSuccess === "0") {
    showContactDetail(deletedContactPk, deleteSuccess, 0);
}


if (newContactPk) {
    showContactDetail(newContactPk, success, 1);
}

if(updatedContactPk) {
    showContactDetail(updatedContactPk, success, 0);
}

function showContactDetail(pk, showSuccess, isNew) {
    fetch(`/contact/${pk}`)
        .then(response => response.text())
        .then(html => {
            document.getElementById('contact-content').innerHTML = html;

            if (showSuccess === "1") {
                if (isNew) {
                    document.getElementById('contact-content').insertAdjacentHTML('afterbegin', alertSuccessNew);
                }
                else {
                    document.getElementById('contact-content').insertAdjacentHTML('afterbegin', alertSuccessUpdate);
                }
            }
            history.replaceState({}, document.title, window.location.pathname);


        })
        .catch(error => {
            console.error('Error:', error);
        });
}




function editContact(pk) {
    fetch(`/contact/${pk}/edit`)
        .then(response => response.text())
        .then(html => {
            document.getElementById('contact-content').innerHTML = html;

            const form = document.querySelector('form');
            form.addEventListener('submit', function(event) {
                event.preventDefault();
                const formData = new FormData(form);
                fetch(`/contact/${pk}/edit`, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                })
                .then(response => {
                    if (response.ok) {
                        window.location.href = `/?updated_contact_pk=${pk}&success=1`;
                    } else {
                        console.error('Error while updating contact');
                    }
                });
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function cancelEdit(pk) {
    window.location.href = `/?updated_contact_pk=${pk}&success=0`;
}

function cancelDelete(pk) {
    window.location.href = `/?deleted_contact_pk=${pk}&delete_success=0`;
}


function deleteContact(pk) {
    fetch(`/contact/${pk}/delete`)
    .then(response => response.text())
    .then(html => {
        document.getElementById('contact-content').innerHTML = html;

        const form = document.querySelector('form');
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(form);
            fetch(`/contact/${pk}/delete`, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = `/?deleted_contact_pk=${pk}&delete_success=1`;
                } else {
                    console.error('Error while deleting contact');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function closeContact(pk) {


}

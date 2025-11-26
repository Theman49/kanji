function searchFocus(fieldName){
    const elField = document.querySelector(`input[name="${fieldName}"]`)

    window.addEventListener('keydown', (event) => {
        if(event.key === '/'){
            event.preventDefault();
            elField.focus();
        }
    })
}

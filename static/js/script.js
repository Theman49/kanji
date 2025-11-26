function searchFocus(fieldName){
    const elField = document.querySelector(`input[name="${fieldName}"]`)

    window.addEventListener('keydown', (event) => {
        if(event.metaKey && event.key === '/'){
            elField.focus();
        }
    })
}
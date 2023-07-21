function add_date(){
    var elem = document.getElementById('add');
    
    var divElem = document.getElementById('myDIV2'); 
    if(elem.checked == true){
        divElem.style.display = 'block'  ; 
    }else{
        divElem.style.display = 'none'  ;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const formCopyTarget = document.getElementById('extra-form-list');
    const addMoreExtra = document.getElementById('add-extra');
    const totalNewForms = document.getElementById('id_form-TOTAL_FORMS');

    function addMoreForm(formId, currentFormCount) {
        const copyEmptyFormElt = document.getElementById(formId).cloneNode(true);
        const regex = new RegExp('__prefix__', 'g');
        copyEmptyFormElt.setAttribute('class', 'extra-form input-group mb-3');
        copyEmptyFormElt.setAttribute('id', `form-${currentFormCount}`);
        copyEmptyFormElt.innerHTML = copyEmptyFormElt.innerHTML.replace(regex, currentFormCount);
        copyEmptyFormElt.querySelectorAll('input, select, textarea').forEach(input => {
            input.value = '';
        });

        const removeButton = copyEmptyFormElt.querySelector('.remove-extra');
        removeButton.addEventListener('click', () => {
            formCopyTarget.removeChild(copyEmptyFormElt);
            updateTotalForms(); // Mettre à jour le nombre total de formulaires
        });

        //copyEmptyFormElt.querySelector('.input-group-append').appendChild(removeButton);
        formCopyTarget.append(copyEmptyFormElt);
    }

    addMoreExtra.addEventListener('click', () => {
        const currentExtraForms = document.getElementsByClassName('extra-form');
        const currentFormCount = currentExtraForms.length;
        addMoreForm('extraEmpty-form', currentFormCount);
        totalNewForms.setAttribute('value', currentFormCount + 1);
    });

    function updateTotalForms() {
        const currentExtraForms = document.getElementsByClassName('extra-form');
        const currentFormCount = currentExtraForms.length;
        totalNewForms.setAttribute('value', currentFormCount);
    }

    // Gérer les boutons de suppression existants
    /*const removeButtons = document.getElementsByClassName('remove-extra');
    for (let i = 0; i < removeButtons.length; i++) {
        const removeButton = removeButtons[i];
        removeButton.addEventListener('click', () => {
            const parentForm = removeButton.closest('.extra-form');
            formCopyTarget.removeChild(parentForm);
            updateTotalForms(); // Mettre à jour le nombre total de formulaires
        });
    }*/
});
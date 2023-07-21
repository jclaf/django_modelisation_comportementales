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

    const addMoreExtra = document.getElementById('add-extra');


    const formCopyTarget = document.getElementById('extra-form-list');

    addMoreExtra.addEventListener("click", (event) => {
        if(event){
            event.preventDefault();
        }
        const copyEmptyFormElt = document.getElementById('extraEmpty-form').cloneNode(true); 
        
        const currentExtraForms = document.getElementsByClassName('extra-form');
        const currentFormCount = currentExtraForms.length + 1;

        copyEmptyFormElt.setAttribute('class', 'input-group extra-form');
        copyEmptyFormElt.setAttribute('id',`form-${currentFormCount}`);
        const regex = new RegExp('__prefix__','g');
        copyEmptyFormElt.innerHTML = copyEmptyFormElt.innerHTML.replace(regex,currentFormCount);
        
        copyEmptyFormElt.querySelectorAll('input, select, textarea').forEach(input => {
            input.value = '';
        });

        formCopyTarget.append(copyEmptyFormElt);

        //version 2
        const removeButtons = copyEmptyFormElt.getElementsByClassName('remove-extra');
        if (removeButtons.length > 0) {
            for (let i = 0; i < removeButtons.length; i++) {
                const removeButton = removeButtons[i];
                removeButton.addEventListener('click', () => {
                    const parentForm = removeButton.closest('.extra-form');
                    const deleteField = parentForm.querySelector('[name$="-DELETE"]');
                    if (deleteField) {
                        deleteField.checked = true;
                    } else {
                        formCopyTarget.removeChild(parentForm);
                    }
                    updateTotalForms(); // Mettre à jour le nombre total de formulaires
                });
            }
        }

        updateTotalForms();
        /*
        //version 1
        const removeButton = document.createElement('button');
        removeButton.setAttribute('class', 'btn btn-danger remove-button');
        removeButton.setAttribute('type', 'button');
        removeButton.innerText = '-';
        removeButton.addEventListener("click",()=>{
            formCopyTarget.removeChild(copyEmptyFormElt);
            updateTotalForms(); // Optionally update the total form count
        });

        copyEmptyFormElt.querySelector('.input-group-append').appendChild(removeButton)
        
        totalNewForms.setAttribute('value', currentFormCount+1)
        */
    });

    function updateTotalForms() {
        const currentExtraForms = document.getElementsByClassName('extra-form');
        const currentFormCount = currentExtraForms.length;
        const totalNewForms = document.getElementById('id_form-TOTAL_FORMS');
        totalNewForms.setAttribute('value', currentFormCount);
    }
  
    
    // Handle remove button clicks for existing forms
    /*const removeButtons = document.getElementsByClassName('remove-button');
    if (removeButtons.length > 0) {
        for (let i = 0; i < removeButtons.length; i++) {
            const removeButton = removeButtons[i];
            removeButton.addEventListener('click', () => {
                const parentForm = removeButton.closest('.extra-form');
                formCopyTarget.removeChild(parentForm);
                updateTotalForms(); // Optionally update the total form count
                
            });
        }
    }*/

});

/*
const deleteMoreExtra = document.getElementById('remove-extra');
deleteMoreExtra.addEventListener("click",(event)=>{
    if(event){
        event.preventDefault();
    }
    print("ici");
});
*/


/*
function addFormRow() {
    var container = $('#formset-container');
    var row = $('<div class="form-row"></div>');

    // Create a new form instance with a unique prefix
    var formPrefix = 'form-' + formCount;
    var formHtml = $('#empty-form').html().replace(/__prefix__/g, formPrefix);
    row.html(formHtml);
    container.append(row);

    // Increment the form count
    formCount++;
  }*/
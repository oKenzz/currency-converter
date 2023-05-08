function SelectStateChanged()
    const selectElem = document.getElementsbyId('rate')
    selectElem.addEventListener('submit', (event) => {
        event.preventdefault();

        const selecetedValue =selectElem.elements['rate'].value;

        fetch('/rate', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value: selectedValue })
          })
          .then(response => {
            if (response.ok) {
              console.log('Success');
            } else {
              console.error('Error');
            }
          })
          .catch(error => console.error(error));
    });
new Autocomplete('#autocomplete',{
    
    search : input => {
        const url = `/autocomplete_busca_componente?componente=${input}`       
        return new Promise(resolve => {
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data.data)
                resolve(data.data)
            
            })
        })  
        
    },

    getResultValue: result => result.nome,


    renderResult: (result, props) => `
    <li ${props}>
      <div>
        ${result.nome}
      </div>
    </li> `,


    onSubmit : result => {
        console.log(result.id)
    }


})

new Autocomplete('#autocomplete2',{
    
    search : input => {
        const url = `/autocomplete_busca_componente?componente=${input}`       
        return new Promise(resolve => {
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data.data)
                resolve(data.data)
                
            })
        })   
    },
    getResultValue: result => result.nome,


    renderResult: (result, props) => `
    <li ${props}>
      <div>
        ${result.nome}
      </div>
    </li> `,


    onSubmit : result => {
        console.log(result.id)
    }

})
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

    onSubmit : result => {
        console.log(result.id)
    }

})
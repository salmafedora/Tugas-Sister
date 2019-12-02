const form = document.querySelector('form')
const search = document.querySelector('input')
const template = document.querySelector('#template').innerHTML
const result = document.querySelector('#result')

form.addEventListener('submit', async (e) => {
    e.preventDefault()

    const name = search.value

    try {
        while (result.firstChild) result.removeChild(result.firstChild);

        url = `/users?name=${name}`
        const response = await fetch(url)
        const data = await response.json()
        
        if (data.error) {
        } else {
            const html = Mustache.render(template, {users:data})
            result.insertAdjacentHTML('beforeend', html)
        }
    } catch (error) {
        console.error(error);
    }
})

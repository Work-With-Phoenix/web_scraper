const search = document.getElementById('search');
const matchList = document.getElementById('match-list');

// get products and filter
const searchProducts = async searchText => {
    const res = await fetch ('../data/tvs.json');
    const products = await res.json();
    // testing on console
    // console.log(products)

    // get matches to current text input
    let matches = products.filter(product => {
        const regex = RegExp(`^${searchText}`, 'gi');
        return product.name.match(regex) || product.discount.match(regex);
    });

    if(searchText.length === 0){
        matches = [];
        matchList.innerHTML = '';

    }

    outputHtml(matches);

};

// showing results in HTML
const outputHtml = matches =>{
    if(matches.length > 0){
        const html = matches.map(match => `
        <div class="card card-body mb-1 px-6 py-2 w-full bg-white rounded shadow">
        <h4>${match.name} <span class="text-yellow-500">(${match.discount})</span> <span>${match.currentprice}</span></h4>
        <div class="flex flex-row space-x-3">
        <span>Ratings: ${match.rating}</span>
        <span class="text-green-500 line-through">Original Price: ${match.originalprice}</span>
        </div>
        <div>
        <h4>Product Features:</h4>
        <span>${match.features}</span>
        </div>
        </div>
        
        `)
        .join('');

        matchList.innerHTML = html
    }
}

search.addEventListener('input', () => searchProducts(search.value));
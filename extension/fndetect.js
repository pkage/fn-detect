console.log('hello from content script')

document.querySelector('body').addEventListener('click', () => {
	console.log('patching all dropdowns')
	patchAllDropdowns()
})


const patchDropdown = (dd) => {
	if (dd.querySelector('li.fn-detect') !== null) return;

	let username = dd.querySelector('.username').querySelector('b').textContent

	let btn = document.createElement('button')
	btn.className = 'dropdown-link'
	btn.setAttribute('type', 'button')

	let a = document.createElement('a')
	a.setAttribute('href', 'http://fn-detect.io:5000/dox/load/' + username)
	a.setAttribute('target', '_blank')
	a.textContent = 'Scan @' + username
	a.style.text_decoration = 'none'
	
	let li = document.createElement('li')
	li.className = 'fn-detect'
	btn.appendChild(a)
	li.appendChild(btn)

	dd.querySelector('ul').appendChild(li)
}
const patchAllDropdowns = () => {
	let dds = document.querySelectorAll('.dropdown-menu')
	for (let dd of dds) {
		try {
			patchDropdown(dd)
		} catch (e) {
		}
	}

}
setInterval(patchAllDropdowns, 3000);

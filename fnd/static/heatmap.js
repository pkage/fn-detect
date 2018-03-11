const heatmap = sel => {
	let data = document.querySelector(sel).text
	data = JSON.parse(data)
	data = data.timemap

	let hm = d3.select('#heatmap-container')
		.append('svg')

	let row = hm
		.data(Object.keys(data))
		.enter()
		.append('g')

}

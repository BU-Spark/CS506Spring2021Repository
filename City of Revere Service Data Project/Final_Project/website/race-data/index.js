let files = [
    "all-white-alone",
    "all-black-or-african-american-alone",
    "all-american-indian-and-alaska-native-alone",
    "all-asian-alone",
    "all-native-hawaiian-and-other-pacific-islander-alone",
    "all-some-other-race-alone",
    "all-hispanic-or-latino",
    "all-two-or-more-races"
];


function newPlot(fileName, mapName) {
    //console.log(fileName);
    fetch('./out/' + fileName + '.div')
        .then(function (response) {
            return response.text();
        })
        .then(function (body) {
	    let wrapper = document.querySelector("#wrapper-"+mapName);
	    if(!wrapper) {
		let root = document.querySelector("#root");
		wrapper = document.createElement("div");
		wrapper.id = "wrapper-"+mapName;
		root.appendChild(wrapper);
	    }
            let removeMe = wrapper.querySelector("div.map");
            if(removeMe) removeMe.remove();

            var div = document.createElement("div");
            div.innerHTML = body;
            div.className = 'map';

            wrapper.appendChild(div);
            runScripts(wrapper.querySelector("div.map"));
        });
}


function initCategoryClicker(files, mapName) {
    let cats = new Set();
    for (let file of files) {
	cats.add(file.split("-")[0]);
    }

    let wrapper = document.querySelector("#wrapper-"+mapName);
    if(!wrapper) {
	let root = document.querySelector("#root");
	wrapper = document.createElement("div");
	wrapper.id = "wrapper-"+mapName;
	root.appendChild(wrapper);
    }
    let categoryContainer = document.createElement("form");
    categoryContainer.id = "categoryContainer";
    wrapper.appendChild(categoryContainer);
    // create the container for the subcategories
    let radioContainer = document.createElement("form");
    radioContainer.id = "radioContainer";
    wrapper.appendChild(radioContainer);

    for (let cat of cats) {
	let radio = document.createElement("input");
	let label = document.createElement("label");
	cat = cat.replace('all-', '');
	radio.type = "radio";
	radio.id = cat;
	radio.name = "cats";
	radio.value = cat;
	label.setAttribute("for", cat);
	label.innerHTML = cat;

	categoryContainer.appendChild(radio);
	categoryContainer.appendChild(label);
    }

    categoryContainer.addEventListener("change", function () {
	let catSelected = document.querySelector('input[name = "cats"]:checked')
	    .value;

	let catFiles = files.filter((f) => f.split("-")[0] == catSelected);
	radioContainer.innerHTML = "";

	for (file of catFiles) {
	    let radio = document.createElement("input");
	    let label = document.createElement("label");
	    file = file.replace('all-', '');
	    radio.type = "radio";
	    radio.id = file;
	    radio.name = "files";
	    radio.value = file;
	    label.setAttribute("for", file);
	    label.innerHTML = file;

	    radioContainer.appendChild(radio);
	    radioContainer.appendChild(label);
	}
	// auto-select the first radio
	radioContainer.children[0].click();
    });

    radioContainer.addEventListener("change", function () {
	let selected = document.querySelector('input[name = "files"]:checked').value;
	newPlot(selected);
    });
    // auto-select the first category
    categoryContainer.children[0].click();
}


initCategoryClicker(files, "race-data");

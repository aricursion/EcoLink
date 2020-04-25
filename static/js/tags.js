var tags = [];
function addTag(val) {
	if (val.length > 0 && val.length < 16) {
		tags.push(val);
		console.log(tags);
		$("#tags").append(
			`<h4 class="tag" onclick='deleteElem(this)'><span class='badge badge-secondary'>${$(
				"#tag-gen"
			).val()} </span></h4>`
		);
		setVal(tags);
	}
}

$("#tag-gen").keydown(function (event) {
	if (event.which == 32) {
		//Space character
		event.preventDefault();
		addTag($("#tag-gen").val()); //Add a new tag
		$("#tag-gen").val(""); //Clear input prompt
	}
});

function getElementList() {
	elemList = $("#tags").text().split(" ");
	elemList.pop();
	return elemList;
}

function deleteElem(el) {
	$(el).addClass("yeet");
	tags.splice(tags.indexOf($(el).text()), 1);
	console.log(tags);
	setTimeout(function () {
		el.remove();
	}, 300);
}

function setVal(arr) {
	str = ""
	for (i in arr) {
		console.log(arr[i])
		str+= arr[i] +",";
	}
	document.getElementById("tag-gen").value = str;
	console.log(document.getElementById("tag-gen").value);
}
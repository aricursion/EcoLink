function addTag(val){
  if (val.length > 0 && val.length < 16){
    $("#tags").append(`<h4 class="tag" onclick='deleteElem(this)'><span class='badge badge-secondary'>${$('#tag-gen').val()} </span></h4>`)
  }
}

$("#tag-gen").keydown(function( event ) {
  if ( event.which == 32 ) { //Space character
   event.preventDefault();
   addTag($("#tag-gen").val()) //Add a new tag
   $("#tag-gen").val("") //Clear input prompt
  }
});

function getElementList(){
  elemList =  $("#tags").text().split(" ")
  elemList.pop()
  return elemList
}

function deleteElem(el){
  $(el).addClass("yeet")
  setTimeout(function(){
    el.remove()
  }, 300);
}
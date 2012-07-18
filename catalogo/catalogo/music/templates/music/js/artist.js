$("#nav #artistList").on("click", "a.artist", function(){
	var link = this.name;
	var id = "#" + this.id;
	$.ajax({
		url: link,
		cache: false,
		beforeSend: function(){
			$(id + "_list").html("<strong>Buscando albuns...</strong>");
		},
		success: function(data){
			$(id + "_list").html(data);
		}
	});
	$("#information").html($(this).html());
	$(id + "_list").hide();
	$(id + "_list").fadeIn('slow');
	console.log(this);
	return false;
});

$("#nav #artistList").on("click", "a.artist-edit", function(){
	var link = this.name;
	var id = "#artist" + this.id;
	$.ajax({
		url: link,
		cache: false,
		beforeSend: function(){
			$(id + "_header").html("<strong>Carregando</strong>");
		},
		success: function(data){
			$(id + "_header").html(data);
		}
	});
	return false;
});

$("#nav #artistList").on("click", "a.album", function(){
	var link = this.name;
	$.ajax({
		url: link,
		cache: false,
		beforeSend: function(){
			$("#post").html("<strong>Buscando músicas...</strong>");
		},
		success: function(data){
			$("#post").html(data);
		}
	});
	$("#information").html(' > ' + $(this).html());
	$("#post").hide();
	$("#post").fadeIn('slow');
});

$("#addArtist").click(function(){
	$.ajax({
		url: "{% url save_artist 0 %}",
		cache: false,
		success: function(data){
			$("#artistAdd_list").html(data);
		}
	});
	$("#artistAdd_list").hide();
	$("#artistAdd_list").fadeIn('slow');
	return false;
});
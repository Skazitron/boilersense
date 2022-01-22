
$( document ).ready(function() {
	
	var bannerHead = ['<div class="navbar navbar-inverse blackbar" role="navigation">',
					'<div class="container"><div class="navbar-header">',
					'<button class="navbar-toggle" data-target=".black" data-toggle="collapse" type="button">',
					'<span class="icon-bar"></span>',
					'<span class="icon-bar"></span>',
					'<span class="icon-bar"></span>',
					'</button>',
					'<p>Menu</p>',
					'</div>',
					'<div class="collapse navbar-collapse black">',
					'<ul class="nav navbar-nav">'];
	var bannerTail = ['</ul>',
					'</div>',
					'<!--/.nav-collapse -->',
					'</div>',
					'</div>',
					'<a name="skip_Module_Navigation_Links_H"></a>',
					'</div>'];
	var submenuHead = ['<div class="submenu">',
						'<ul class="nav navbar-nav">'];
	var submenuTail = ['</ul>',
					'</div>'];

	$("body").css("position", "absolute");
	$("body").css("background-color", "white");
	
	
	$('.pageheaderdiv1').remove();
	$('.bgtabon img').remove();
	$('.bgtaboff img').remove();
	$('.tabon img').remove();
	$('.taboff img').remove();
	
	var selected = $('.tabon a').html()
	
	//added map to eliminate submenu items on finaid tab
	menuItems = $('map .pldefault .plaintable tbody td a').get();
	mainMenuHTML = rebuildMenu(bannerHead, bannerTail, menuItems, selected);

	if($('.pagetitlediv').css('display') == 'none'){
		$('.pagebodydiv').css('top','0px');
	}

	//now grab the submenu items id #SubTab is present
	if ($('#subTabs').length > 0){
		var selected = $('.tabon a');
		if(selected[1] != null){
			selected = $(selected[1]).html()
		}
		subMenuItems = $('.pldefault .plaintable tbody td a').get();
		//drop mainMenuHTML items
		subMenuItems = subMenuItems.splice(menuItems.length)
		subMenuHTML = rebuildMenu(submenuHead, submenuTail, subMenuItems, selected);

		var subMenuTarget = $('.pagebodydiv')
		$(subMenuTarget).prepend(subMenuHTML);
	}

	//give an id to the navbar
	var navbar = $('.plaintable')[0]
	$(navbar).attr("id", "ssbNavBar")
	
	var mainMenuTarget = $('.pageheaderlinks2')
	$(mainMenuTarget).html(mainMenuHTML);

	//Clean up remaining menu residue
	$('.bgtabon, .bgtaboff, .taboff, .tabon').remove()

	rel = $('.pagefooterdiv').remove();
	$('.globalfooterdiv').append("<div class='releasewrapperdiv'></div>");
	$('.releasewrapperdiv').html(rel);
	
	$('head').append('<link href="../static_resources/portal/css/ssbLum5StyleSplashOverride.css" rel="stylesheet">');
	
	//Because we are moving all SSB content up 55px, the document body would run long.  So, let's shorten it.
	var h = $('body').height();
	$('body').height(h - 55);

	//create wrapper for all footer divs
	footerArray = $('.pagebodydiv').nextAll().detach();
	var footerHtml = ''; 
	for(i=0;i<footerArray.length;i++){footerHtml += footerArray[i].outerHTML}
	sf = '<div class="footerWrapper">'+ footerHtml +'</div>';
	$('body').append(sf);

	//adjust footer placement
	$('.banner_copyright').prepend($('.infotext_globalfooter').detach());
	$('.banner_copyright').prepend($('.releasetext').detach());

	ieDraw();
	
});

function rebuildMenu(headHtml, tailHtml, menuItems, selected){
	var newMenu = []
	
	newMenu = headHtml;

	for(i=0;i<menuItems.length;i++){
		var href = $(menuItems[i]).attr('href')
		var text = $(menuItems[i]).html()
		if ( i == 0 ){
			if (selected == text){
				newMenu.push('<li class="first selected"><a href="' + href + '">' + text + '</a></li>')
			}else{
				newMenu.push('<li class="first"><a href="' + href + '">' + text + '</a></li>')
			} 
		}else{
			if (selected == text){
				newMenu.push('<li class="selected"><a href="' + href + '">' + text + '</a></li>')
			}else{
				newMenu.push('<li><a href="' + href + '">' + text + '</a></li>')
			}
		}
	}

	newMenu.concat(tailHtml)
				
	return newMenu.join("");
}

function ieDraw(){
	for(i = 1; i<30; i++){
		setTimeout(function() {$('body').prepend('<div class="deleteMe" style="height:0px; width:0px"></div>')}, i * 10 );
	}
	setTimeout(function() {$('.deleteMe').remove()}, 500 );
}

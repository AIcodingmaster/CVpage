//nav바 추적
var lastScrollTop = 0; 
var delta = 5; // 동작의 구현이 시작되는 위치
var navbarHeight = 70; // 영향을 받을 요소를 선택
var didScroll; // 스크롤시에 사용자가 스크롤했다는 것을 알림 
$(window).scroll(function(event){ didScroll = true; }); // hasScrolled()를 실행하고 didScroll 상태를 재설정 
setInterval(function() { if (didScroll) { hasScrolled(); didScroll = false; } }, 250); 
function hasScrolled() { 
    var st = $(this).scrollTop();
    if (Math.abs(lastScrollTop - st) <= delta) return;
    // If current position > last position AND scrolled past navbar... 
    if (st > lastScrollTop && st > navbarHeight){ 
        // Scroll Down
        if($(`#navbarHeader`).hasClass(`show`))
        {
            n=$(`#navbarHeader`);
            n.removeClass(`show`);

        }
         $(`header`).removeClass(`nav-down`).addClass(`nav-up`); 
        } 
    else { // Scroll Up 
        // If did not scroll past the document (possible on mac)... 
        if($(`#navbarHeader`).hasClass(`show`))
        {
            n=$(`#navbarHeader`)
            n.removeClass(`show`)
            return
        }
        if(st + $(window).height() < $(document).height()) 
        { 
            $(`header`).removeClass(`nav-up`).addClass(`nav-down`); 
        } 
    }
    lastScrollTop = st;

}
const navbutton=document.querySelector('.navButton')
const maindiv=document.querySelector('.belowHeader')
navbutton.addEventListener('onclick',pushMain)
function pushMain(){
    maindiv.style.transform="translate3d(0px, px, 0px)";
}
function zoomIn(event) {
    event.target.style.transform = "scale(1.1)";
    event.target.style.zIndex = 1;
    event.target.style.transition = "all 0.5s";
    div=event.target.parentNode.parentNode;
    content=div.querySelector(`.card-body`);
    content.style.transform = "translate3d(0px, -150px, 0px)";
    content.style.transition = "all 0.5s";
}

function zoomOut(event) {
    event.target.style.transform = "scale(1)";
    event.target.style.zIndex = 1;
    event.target.style.transition = "all 0.5s";
    div=event.target.parentNode.parentNode;
    content=div.querySelector(`.card-body`);
    content.style.transform = "translate3d(0px, 0px, 0px)";
    content.style.transition = "all 0.5s";
}

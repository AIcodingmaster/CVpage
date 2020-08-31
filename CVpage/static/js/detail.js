const strong=document.querySelector('strong.textblack')
const card=document.querySelector('svg.bi-card-list')
const playBtn=document.querySelector('svg.bi-file-play')

strong.classList.remove('textblack')
strong.classList.add('text-white')
card.setAttribute('fill','white')
function playBtnOverHandler(){
    playBtn.setAttribute('fill','black');
    playBtn.style.transform= "scale(1.3)";
    playBtn.style.transition= 'all 0.3s';
}
function playBtnOutHandler(){
    playBtn.setAttribute('fill','white');
    playBtn.style.transform= "scale(1.0)";
    playBtn.style.transition= 'all 0.3s';
}
playBtn.addEventListener("mouseover",playBtnOverHandler)
playBtn.addEventListener("mouseout",playBtnOutHandler)
//playBtn.addEventListener("onclick",playBtnHandler)어디서 컨트롤할지 안정함
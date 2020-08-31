$(".box").each(function(){
    var box=$(this)
    var boxImgs=$(this).children('img')
    var myAnimation = new hoverEffect({
        parent: box[0],
        intensity: 1.0,
        speedIn:1.3,
        speedOut:1.3,
        angle:Math.PI/2,
        image1: boxImgs[0].getAttribute('src'),
        image2: boxImgs[1].getAttribute('src'),
        displacementImage: box[0].getAttribute('displacementImage')
    });
})
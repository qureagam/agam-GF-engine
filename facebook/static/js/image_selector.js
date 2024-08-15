function timing(){
    let date = new Date();
    let hour = date.getHours();

    let day = date.getUTCDate();
    let mnt = date.getUTCMonth();
    let monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    document.querySelector('.today').innerHTML =`Today is ${monthNames[Number(mnt)]} ${day}`;
}

setInterval(timing(),1)


let meta = false;
const setting = document.querySelector('.img');
setting.addEventListener('click',()=>{
    const settinf = document.querySelector('.set');
    if (meta){
        settinf.style.visibility = 'hidden'
        meta = false;
    }
    else{
        settinf.style.visibility = 'visible'
        meta = true;
    }
});



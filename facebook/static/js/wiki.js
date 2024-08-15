function year(){
    const dt = new Date();
    let years = dt.getFullYear();

    document.querySelector('.spn').innerHTML +=years;
}

setInterval(year(),1000)


document.querySelector('.back').addEventListener('click',()=>{
    window.location.pathname ='/wiki';
});
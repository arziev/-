const timerBtn = document.querySelector('.time-btn');

timerBtn.addEventListener('click', function(event){
    event.preventDefault();
    if(timerBtn.value === 'Start'){
        timerBtn.style.backgroundColor = '#e71616f7';
        timerBtn.style.boxShadow = '0px 0px 40px 0px rgb(196 35 95 / 75%)';
        timerBtn.value = "End";
    }else{
        
        timerBtn.style = 'inhert';
        timerBtn.value = "Start";
    }
});
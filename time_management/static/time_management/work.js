const timerBtn = document.querySelector('.time-btn');
const timerHidden = document.querySelector('.timer-hidden');
const timerForm = document.getElementById('timer-form');

timerBtn.addEventListener('click', function(event){
    event.preventDefault();
    if(timerBtn.value === 'Start'){
        // document.getElementById('timer-form').action = "{% url 'timer' %}";

        // document.action = "{% url 'timer' %}"

        timerBtn.style.backgroundColor = '#d60000';
        timerBtn.style.boxShadow = '0px 0px 40px 0px rgb(196 35 95 / 75%)';
        timerBtn.value = "End";
    }else{
        // document.getElementById('timer-form').action = ""
        // document.getElementById('timer-form').action = "";
        timerHidden.value = 'count';
        timerBtn.style = 'inherit';
        timerBtn.value = "Start";
    }
});
const timerBtn = document.querySelector('.time-btn');
const timerForm = document.getElementById('timer-form');

timerBtn.addEventListener('click', function(event){
    event.preventDefault();
    console.log("one");
    console.log(timerBtn.value);
    if(timerBtn.innerHTML === 'Start'){
        console.log("two");
        timerBtn.style.backgroundColor = '#d60000';
        timerBtn.style.boxShadow = '0px 0px 40px 0px rgb(196 35 95 / 75%)';
        timerBtn.innerHTML = "End";

        let formData = new FormData()
        formData.append("timer", "start")
    
        fetch('/main', { // it should send to this site, like a <form method="post" acction=""> does
            method: 'POST',
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: formData
        })

    }else {
        console.log('three');

        let formData = new FormData()
        formData.append("timer", "end")
    
        fetch('/main', { // it should send to this site, like a <form method="post" acction=""> does
            method: 'POST',
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: formData
        })
        
        
        
        timerBtn.style = 'inherit';
        timerBtn.innerHTML = "Start";
    }
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}



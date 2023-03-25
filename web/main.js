const setProgram = (CamNumber) => {
    for (let i = 1; i<=3; i++) {
        if (i==CamNumber)
            document.getElementById(`program-${i}`).classList.replace("deactiveButton", "activeButton");
        else 
            document.getElementById(`program-${i}`).classList.replace("activeButton", "deactiveButton");
    }
    // document.getElementById(`program-${CamNumber}`).classList.replace("deactiveButton", "activeButton");
}

const setPreview = (CamNumber) => {
    for (let i = 1; i<=3; i++) {
        if (i==CamNumber)
            document.getElementById(`preview-${i}`).classList.replace("deactiveButton", "activeButton");
        else 
            document.getElementById(`preview-${i}`).classList.replace("activeButton", "deactiveButton");
    }
    // document.getElementById(`preview-${CamNumber}`).classList.replace("deactiveButton", "activeButton");
}

const buttonProgram = (CamNumber) => {
    setProgram(CamNumber)
    // eel.setProgram(CamNumber);
}

const buttonPreview = (CamNumber) => {
    setPreview(CamNumber)
    // eel.setPreview(CamNumber);
}

document.addEventListener('keydown', function(event) {
    if (event.code == 'Digit1' && (event.shiftKey)){
        buttonProgram(1);
        return;
    }
    if (event.code == 'Digit2' && (event.shiftKey)){
        buttonProgram(2);
        return;
    }
    if (event.code == 'Digit3' && (event.shiftKey)){
        buttonProgram(3);
        return;
    }
    if (event.code == 'Digit1') {
        buttonPreview(1);
        return;
    }
    if (event.code == 'Digit2') {
        buttonPreview(2);
        return;
    }
    if (event.code == 'Digit3') {
        buttonPreview(3);
        return;
    }
    if (event.code == 'Space') {
        eel.swap();
        return;
    }
    if (event.code == 'Enter') {
        eel.smoothSwap();
        return;
    }
});

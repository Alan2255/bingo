function changeColor() {
    var random = '#'+(0x1000000+Math.random()*0xffffff).toString(16).substr(1,6);
    const celdas = Array.from(document.getElementsByClassName('ocupada'));
    celdas.forEach(celda => {
    celda.style.backgroundColor = random;
    });
}

function download () {
    var makepdf = document.getElementById("makepdf");
    html2pdf().from(makepdf).save("bingo.pdf");
}

function reload(){
    window.location.reload();
}

var colorButton = document.getElementById("color-button");
colorButton.addEventListener("click", changeColor);

var downloadButton = document.getElementById("download-button");
downloadButton.addEventListener("click", download);

var reloadButton = document.getElementById("reload-button");
reloadButton.addEventListener("click", reload);


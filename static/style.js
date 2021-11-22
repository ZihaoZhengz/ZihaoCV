// to make a changeColor button change the bacground color randomly

const button =document.querySelector(".target");
const makeRandColor = () => {
    const r = Math.floor(Math.random() * 255);
    const g = Math.floor(Math.random() * 255);
    const b = Math.floor(Math.random() * 255);
    return `rgb(${r}, ${g}, ${b})`;
}
button.addEventListener("click",()=>{
    const newColor = makeRandColor();
    document.body.style.backgroundColor = newColor;
});



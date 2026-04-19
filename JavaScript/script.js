const datepicker = document.querySelector('.datepicker');
const dateInput = document.querySelector('.date-input');
const yearInput = document.querySelector('.year-input');
const monthInput = document.querySelector('.month-input');

const cancelButton = document.querySelector('.cancelar');
const applyButton = document.querySelector('.aceptar');

const sigButton = document.querySelector('.sig');
const antButton = document.querySelector('.ant');

const fechas = document.querySelector('.fechas');

let fechaSeleccionada = new Date();
let anyo = fechaSeleccionada.getFullYear();
let mes = fechaSeleccionada.getMonth();

dateInput.addEventListener('click', () => {
    datepicker.hidden = false;
});

cancelButton.addEventListener('click', () => {
    datepicker.hidden = true;
});

applyButton.addEventListener('click', () => {
    dateInput.value = fechaSeleccionada.toLocaleDateString("es-ES", { year: 'numeric', 
                                                                    month: '2-digit', 
                                                                    day: '2-digit', });

    datepicker.hidden = true;
});


sigButton.addEventListener('click', () => {
    if (mes === 11) anyo++;
    mes = (mes + 1) % 12 ;
    mostrarFechas();
});

antButton.addEventListener('click', () => {
    if (mes === 0) anyo--;
    mes = (mes - 1 + 12) % 12 ;
    mostrarFechas();
});

monthInput.addEventListener('change', () => {
    mes = monthInput.selectedIndex;
    mostrarFechas();
});

yearInput.addEventListener('change', () => {
    anyo = yearInput.value;
    mostrarFechas();
});

const actAnyoMes = () => {
    monthInput.selectedIndex = mes;
    yearInput.value = anyo;
    mostrarFechas();
};

const handleDateClick = (e) => {
    const button = e.target;

    const seleccionado = fechas.querySelector('.seleccionado');
    seleccionado && seleccionado.classList.remove('seleccionado');

    button.classList.add('seleccionado');

    fechaSeleccionada = new Date(anyo, mes, parseInt(button.textContent));
};

const mostrarFechas = (params) => {
    fechas.innerHTML = '';
    actAnyoMes();

    const ultsMesAnt= new Date(anyo, mes, 0);
    for(let i=0; i < ultsMesAnt.getDay(); i++){
        const text = ultsMesAnt.getDate() - ultsMesAnt.getDay() + i;
        const button = crearBotones(i, true);
        fechas.appendChild(button);
    }

    const ultimosMes = new Date(anyo, mes + 1, 0);
    for (let i = 1; i <= ultimosMes.getDate(); i++) {

        
        const button = crearBotones(i, false);
        button.addEventListener('click', handleDateClick);
        fechas.appendChild(button);

    }

    const primerMesSig = new Date(anyo, mes + 1, 1);
    for(let i=primerMesSig.getDay(); i < 7; i++){
        const text = primerMesSig.getDate() - primerMesSig.getDay() + i;
        const createButton = crearBotones(text, true);
        fechas.appendChild(createButton);
    }

};

const crearBotones = (text, isDisabled = false) => {
    const diaActual = new Date();

    const isToday = diaActual.getDate() === text && 
                    diaActual.getMonth() === mes && 
                    diaActual.getFullYear() === anyo;

    const seleccion = fechaSeleccionada.getDate() === text && 
                    fechaSeleccionada.getMonth() === mes && 
                    fechaSeleccionada.getFullYear() === anyo;

    const button = document.createElement('button');
    button.textContent = text;
    button.disabled = isDisabled;
    button.classList.toggle('hoy', isToday);
    button.classList.toggle('seleccionado', seleccion);
    return button;
};


mostrarFechas();
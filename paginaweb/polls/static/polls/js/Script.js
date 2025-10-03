const personajes = {
  Astarion: { raza: "Elfo", subrazas: "Alto Elfo, Elfo de los Bosques", clase: "Pícaro" },
  ShadowHeart: { raza: "Semielfo", subrazas: "Altos, Bosques, Drows", clase: "Clérigo" },
  Laezel: { raza: "Githyanki", subrazas: "Githyanki puro", clase: "Guerrera" },
  Gale: { raza: "Humano", subrazas: "Humano estándar", clase: "Mago" }
};

function mostrarDetalle(personaje) {
  const data = personajes[personaje];
  if (!data) return;
  const detalleDiv = document.getElementById('detalle');
  if (detalleDiv.style.display === 'block' && detalleDiv.dataset.personaje === personaje) {
    detalleDiv.style.display = 'none';
    detalleDiv.innerHTML = '';
    detalleDiv.dataset.personaje = '';
    return;
  }
  detalleDiv.innerHTML = `<h2>${personaje}</h2>
                          <p><strong>Raza:</strong> ${data.raza}</p>
                          <p><strong>Subrazas:</strong> ${data.subrazas}</p>
                          <p><strong>Clase:</strong> ${data.clase}</p>`;
  detalleDiv.style.display = 'block';
  detalleDiv.dataset.personaje = personaje;
}

function mostrarToast(mensaje, tipo='error', duracion=3000) {
  const toast = document.getElementById('toast');
  toast.textContent = mensaje;
  toast.style.background = tipo === 'success' ? 'green' : 'red';
  toast.style.display = 'block';
  setTimeout(() => { toast.style.display = 'none'; }, duracion);
}

window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('#personajes img').forEach(img => {
    img.addEventListener('click', () => mostrarDetalle(img.id));
  });
});

function abrirBanco(id) {
  const modal = document.querySelector('body.banco-jade #' + id);
  if(modal) modal.style.display = "flex";
}

function cerrarBanco(id) {
  const modal = document.querySelector('body.banco-jade #' + id);
  if(modal) modal.style.display = "none";
}

window.addEventListener('click', function(e) {
  document.querySelectorAll('body.banco-jade .ventana').forEach(v => {
    if(e.target === v) v.style.display = "none";
  });
});

let indiceBanco = 0;
const imagenesBanco = document.querySelectorAll('body.banco-jade .carrusel img');

function mostrarBanco(n) {
  imagenesBanco.forEach(img => img.classList.remove("activa"));
  indiceBanco = (n + imagenesBanco.length) % imagenesBanco.length;
  imagenesBanco[indiceBanco].classList.add("activa");
}

function cambiarBanco(direccion) {
  mostrarBanco(indiceBanco + direccion);
}

setInterval(() => cambiarBanco(1), 5000);
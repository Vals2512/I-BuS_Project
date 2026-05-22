document.addEventListener('DOMContentLoaded', function () {
    function getJsonData(id) {
        const script = document.getElementById(id);
        if (!script) return null;
        try {
            return JSON.parse(script.textContent);
        } catch (e) {
            console.error('Error parseando JSON de', id, e);
            return null;
        }
    }

    // Gráfico línea (total pasajeros por día y empresa)
    const labelsLine = getJsonData('labels-data');
    const datasetsLine = getJsonData('datasets-data');
    if (labelsLine && datasetsLine) {
        const ctxLine = document.getElementById('graficoEmpresas').getContext('2d');
        new Chart(ctxLine, {
            type: 'line',
            data: { labels: labelsLine, datasets: datasetsLine },
            options: { responsive: true, plugins: { legend: { position: 'top' }, title: { display: true, text: 'Total pasajeros por día y empresa' } } }
        });
    }

    // Gráfico torta (número de rutas por empresa)
    const labelsPie = getJsonData('data-rutas-labels');
    const dataPie = getJsonData('data-rutas-values');
    if (labelsPie && dataPie) {
        const ctxPie = document.getElementById('graficoRutasEmpresa').getContext('2d');
        new Chart(ctxPie, {
            type: 'pie',
            data: {
                labels: labelsPie,
                datasets: [{
                    label: 'Rutas por empresa',
                    data: dataPie,
                    backgroundColor: ['#36a2eb', '#ff6384', '#ffce56', '#4bc0c0', '#9966ff', '#f67019'],
                    borderWidth: 1
                }]
            },
            options: { responsive: true, plugins: { legend: { position: 'bottom' }, title: { display: true, text: 'Número de rutas por empresa' } } }
        });
    }

    // Gráfico barras (total pasajeros por empresa)
    const labelsBar = getJsonData('data-pasajeros-labels');
    const dataBar = getJsonData('data-pasajeros-values');
    if (labelsBar && dataBar) {
        const ctxBar = document.getElementById('graficoPasajerosEmpresa').getContext('2d');
        new Chart(ctxBar, {
            type: 'bar',
            data: {
                labels: labelsBar,
                datasets: [{
                    label: 'Pasajeros',
                    data: dataBar,
                    backgroundColor: '#4bc0c0',
                    borderColor: '#36a2eb',
                    borderWidth: 1
                }]
            },
            options: { responsive: true, plugins: { legend: { display: false }, title: { display: true, text: 'Total pasajeros por empresa' } }, scales: { y: { beginAtZero: true }, x: {} } }
        });
    }
});

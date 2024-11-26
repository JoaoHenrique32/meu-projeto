document.getElementById("fetch-weather").addEventListener("click", async () => {
    const location = document.getElementById("location").value;
    const resultDiv = document.getElementById("result");

    try {
        const response = await fetch(`http://localhost:8000/weather?location=${location}`);
        if (!response.ok) throw new Error("Erro ao consultar o clima");
        const data = await response.json();
        resultDiv.innerHTML = `<h3>Clima em ${data.location}</h3><pre>${JSON.stringify(data.data, null, 2)}</pre>`;
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red;">${error.message}</p>`;
    }
});

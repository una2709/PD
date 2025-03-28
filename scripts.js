function toggleDetails(pos) {
    const details = document.getElementById("details-" + pos);
    const image = document.getElementById("image-" + pos);
    if (details.style.display === "none" || details.style.display === "") {
        details.style.display = "block";
        image.style.display = "block";
    } else {
        details.style.display = "none";
        image.style.display = "none";
    }
}

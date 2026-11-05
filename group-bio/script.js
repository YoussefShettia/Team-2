function toggleBio(bioId) {
    const bio = document.getElementById(bioId);
    if (bio.style.display === "none" || bio.style.display === "") {
        bio.style.display = "block";
    } else {
        bio.style.display = "none";
    }
}

function showSection(sectionId) {
    const biosSection = document.getElementById("bios");
    const visionSection = document.getElementById("vision");

    if (sectionId === "bios") {
        biosSection.style.display = "flex";
        visionSection.style.display = "none";
    }
    else if (sectionId === "vision") {
        biosSection.style.display = "none";
        visionSection.style.display = "block";
    }
}

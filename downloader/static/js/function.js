var video_btn = document.querySelector("#video-btn");
var audio_btn = document.querySelector("#audio-btn");
var video_table = document.querySelector(".video-table");
var audio_table = document.querySelector(".audio-table");
video_btn.addEventListener('click', function () {
    video_table.style.display = "block";
    audio_table.style.display = "none";
});
audio_btn.addEventListener('click', function () {
    video_table.style.display = "none";
    audio_table.style.display = "block";
});

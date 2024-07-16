let video_btn = document.querySelector<HTMLButtonElement>("#video-btn");
let audio_btn = document.querySelector<HTMLButtonElement>("#audio-btn");
let video_table = document.querySelector<HTMLTableElement>(".video-table");
let audio_table = document.querySelector<HTMLTableElement>(".audio-table");

video_btn.addEventListener('click', function(){
  video_table.style.display = "block";
  audio_table.style.display = "none";
})

audio_btn.addEventListener('click', function(){
  video_table.style.display = "none";
  audio_table.style.display = "block";
})
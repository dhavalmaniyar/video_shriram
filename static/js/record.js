const start = document.getElementById("start");
const stop = document.getElementById("stop");
const video = document.getElementById("videoPlayer");
let recorder, stream;

async function startRecording() {
  stream = await navigator.mediaDevices.getDisplayMedia({
    video: { mediaSource: "screen" },
    audio: true
  });
  recorder = new MediaRecorder(stream);

  const chunks = [];
  recorder.ondataavailable = e => chunks.push(e.data);
  recorder.start();

  recorder.onstop = e => {
    const completeBlob = new Blob(chunks, { type: chunks[0].type });
    console.log("3>>>>>>>>>", video.src);
    video.src = URL.createObjectURL(completeBlob);
    console.log("1>>>>>>>>> ", video.src);
  };
}

start.addEventListener("click", () => {
  start.setAttribute("disabled", true);
  stop.removeAttribute("disabled");

  startRecording();
});

stop.addEventListener("click", () => {
  stop.setAttribute("disabled", true);
  start.removeAttribute("disabled");

  recorder.stop();
  stream.getVideoTracks()[0].stop();
});

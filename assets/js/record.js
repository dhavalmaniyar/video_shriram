const start = document.getElementById("start");
const stop = document.getElementById("stop");
const dwd = document.getElementById("dwd");
const video = document.getElementById("videoPlayer");

let recorder, stream;

const mergeAudioStreams = (desktopStream, voiceStream) => {
  const context = new AudioContext();
  const destination = context.createMediaStreamDestination();
  let hasDesktop = false;
  let hasVoice = false;
  if (desktopStream && desktopStream.getAudioTracks().length > 0) {
    // If you don't want to share Audio from the desktop it should still work with just the voice.
    const source1 = context.createMediaStreamSource(desktopStream);
    const desktopGain = context.createGain();
    desktopGain.gain.value = 0.7;
    source1.connect(desktopGain).connect(destination);
    hasDesktop = true;
  }

  if (voiceStream && voiceStream.getAudioTracks().length > 0) {
    const source2 = context.createMediaStreamSource(voiceStream);
    const voiceGain = context.createGain();
    voiceGain.gain.value = 0.7;
    source2.connect(voiceGain).connect(destination);
    hasVoice = true;
  }

  return hasDesktop || hasVoice ? destination.stream.getAudioTracks() : [];
};

async function startRecording() {
  const audio = true;
  const mic = true;
  desktopStream = await navigator.mediaDevices.getDisplayMedia({
    video: true,
    audio: audio,
  });

  if (mic === true) {
    voiceStream = await navigator.mediaDevices.getUserMedia({
      video: false,
      audio: mic,
    });
  }

  const tracks = [
    ...desktopStream.getVideoTracks(),
    ...mergeAudioStreams(desktopStream, voiceStream),
  ];

  console.log("Tracks to add to stream", tracks);
  stream = new MediaStream(tracks);

  // video.srcObject = stream;
  video.muted = true;

  recorder = new MediaRecorder(stream, {
    mimeType: "video/webm; codecs=vp8,opus",
  });

  const chunks = [];
  recorder.ondataavailable = (e) => chunks.push(e.data);
  recorder.start();

  recorder.onstop = (e) => {
    const completeBlob = new Blob(chunks, {
      type: chunks[0].type,
    });
    console.log("3>>>>>>>>>", video.src);
    video.src = URL.createObjectURL(completeBlob);
    dwdUrl(URL.createObjectURL(completeBlob));
    console.log("1>>>>>>>>> ", video.src);
  };
}

async function stopRecording() {
  recorder.stop();
}

async function dwdUrl(a) {
  dwd.href = a;
  dwd.removeAttribute("disabled");
}

start.addEventListener("click", () => {
  start.setAttribute("disabled", true);
  stop.removeAttribute("disabled");

  startRecording();
});

stop.addEventListener("click", () => {
  stop.setAttribute("disabled", true);
  start.removeAttribute("disabled");

  stopRecording();
  stream.getVideoTracks()[0].stop();
});
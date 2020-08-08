export default class Audio {
    stopped: boolean = true;

    shouldStop: boolean = false;

    recordedChunks: Blob[] = [];

    mediaRecorder = null;

    handleStart = () => {
        this.shouldStop = false;
        this.recordedChunks = [];
        const constraints = {
            audio: {
                echoCancellation: true,
            },
            video: false
        };
        navigator.mediaDevices.getUserMedia(constraints).then(this._handleSuccess);
    }

    _handleSuccess = (stream)  => {
        if (this.stopped) {
            this.recordedChunks = [];
            this.mediaRecorder = new MediaRecorder(stream);
            this.mediaRecorder.ondataavailable = this._handleDataAvailable;
            this.stopped = false;
            this.mediaRecorder.start(1000);
        }
    }

    _handleDataAvailable = (e) => {
        if (e.data && e.data.size > 0) {
            this.recordedChunks.push(e.data);
        }

        if (this.shouldStop === true && this.stopped === false) {
            this.mediaRecorder.stop();
            this.stopped = true;

        }
    }

    handleStop = () => {
        this.shouldStop = true;
    }

    handlePlay = (element) => {
        console.log(this.recordedChunks.length);
        if (this.recordedChunks.length > 0) {
            const buffer = new Blob(this.recordedChunks);
            element.src = null;
            element.srcObject = null;
            element.src = window.URL.createObjectURL(buffer);
            element.play();
        }
    }

    get recordedData()  {
        return this.recordedChunks;
    }
}

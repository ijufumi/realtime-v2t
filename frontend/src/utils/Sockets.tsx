import io from "socket.io-client";

export default class Sockets {
  socket;
  url: string;

  constructor(url: string) {
    this.url = url;
    this._connect();
  }

  _connect = () => {
    this.socket = io(this.url);
  }

  get isConnected() {
    return this.socket && this.socket.connected;
  }

  on = (event, callback) => {
    if (this.isConnected) {
      this.socket.on(event, callback);
    }
  }

  sendText = (event, data) => {
    if (this.isConnected) {
      this.socket.emit(event, data);
    }
  }

  sendBinary = (event, data)  => {
    if (this.isConnected) {
      this.socket.binary(true).emit(event, data);
    }
  }
}

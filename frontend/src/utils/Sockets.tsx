import io from "socket.io-client";

export default class Sockets {
  socket: ;
  url: string;
  constructor(url: string) {
    this.url = url;
    this._connect();
  }

  _connect = () => {
    this.socket = io(this.url);
  }

  get isConnected() {
    return this.socket && this.socket.is_connected;
  }
}

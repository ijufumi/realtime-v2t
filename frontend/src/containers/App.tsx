import React from 'react';
import styled, { keyframes } from 'styled-components';
import { faMicrophoneAlt, faPlayCircle, faStopCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import FiberManualRecordIcon from '@material-ui/icons/FiberManualRecord';

import { Table } from 'semantic-ui-react';
import 'semantic-ui-css/semantic.min.css';

import Audio from "../utils/Audio";
import Sockets from "../utils/Sockets";
import { API_ENDPOINT } from "../constants/hosts";

import './App.css';

enum Status {
  STARTED,
  STOPPED
}


class App extends React.Component<any, any> {
  state = {
    status: Status.STOPPED,
    results: []
  }

  audio = new Audio();
  sockets = new Sockets(API_ENDPOINT);

  componentDidMount() {
    // this.sockets.on("connect", () => console.log("connected"));
    // this.sockets.sendText("connect", "hello");
    console.log(this.sockets.isConnected);
    this.sockets.on("send_results", this.handleReceiveResults);
    this.sockets.on("send_result", this.handleReceiveResult);
  }

  handleReceiveResults = (results) => {
    this.setState({
      results
    })
  }

  handleReceiveResult = (result) => {
    const check = this.state.results.find(v => v.id === result.id);
    if (!check) {
      this.setState(prev => {
        const newResults = prev.results;
        newResults.push(result);
        return {
          results: newResults
        }
      });
    }
  }

  handleStartRecord = () => {
    this.audio.handleStart();
    this.sockets.sendText('message', "start");
    this.setState ({
      status: Status.STARTED
    });
  }

  handleStopRecord = () => {
    this.audio.handleStop();
    this.setState ({
      status: Status.STOPPED
    });
    this.sockets.sendText('message', "end");
    this.sockets.sendBinary('voice_message', this.audio.recordedData);
  }

  renderResults = () => {
    if (this.state.results.length === 0) {
      return null;
    }
    return <ResultContainer>
      <Table celled>
        <Table.Header>
          <Table.Row>
            <Table.HeaderCell width={10} textAlign={"center"}>Text</Table.HeaderCell>
            <Table.HeaderCell width={1} textAlign={"center"}>Voice</Table.HeaderCell>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {this.state.results.map((d, idx) => {
            return <Table.Row key={`row-key-${idx}`}>
              <Table.Cell>
                {d.texts}
              </Table.Cell>
              <Table.Cell textAlign={"center"}>
                <Player id={d.id} src={d.url} />
              </Table.Cell>
            </Table.Row>
          })}
        </Table.Body>
      </Table>
    </ResultContainer>;
  }

  render() {
    return (
      <Container>
        <StopButtonContainer isVisible={this.state.status == Status.STARTED}>
          <RecLabel>
            <FiberManualRecordIcon htmlColor={'red'} />
            REC
          </RecLabel>
          <StopButtonBlock onClick={this.handleStopRecord} >
            <FontAwesomeIcon icon={faStopCircle} size={'2x'} color={'#FFFFFF'}/>
          </StopButtonBlock>
        </StopButtonContainer>
        <MicrophoneContainer onClick={this.handleStartRecord}>
          <FontAwesomeIcon icon={faMicrophoneAlt} size={'10x'}/>
        </MicrophoneContainer>
        { this.renderResults() }
      </Container>
    );
  }
}

const Container = styled.div`
  background-color: #EDF6FF;
  min-width: 650px;
  width: 100vw;
  min-height: 700px;
  height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family:  Helvetica,Arial,sans-serif;
`;

const MicrophoneContainer = styled.div`
  background-color: #FFFFFF;
  margin: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 250px;
  max-height: 250px;
  min-width: 400px;
  max-width: 400px;
  border: 1px solid #DFDFDF;
  border-radius: 10px;
  cursor: pointer;
`;

const StopButtonContainer = styled.div<{ isVisible: boolean }>`
  width: 100vw;
  height: 100vh;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  top: 0;
  left: 0;  
  background-color: rgb(0, 0, 0, 0.5);
  z-index: 10;
  visibility: ${({ isVisible }) => (isVisible ? 'visible'  : 'hidden')};
`;

const StopButtonBlock = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000000;
  width: 100px;
  height: 70px;
  border: 2px solid #FFFFFF;
  border-radius: 5px;
`;

const RecLabelAnimation = keyframes`
    0% {
      opacity:0;
    }
    100% {
      opacity:1;
    }
`;

const RecLabel = styled.div`
  position: absolute;
  top: 20px;
  left: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 10px;
  color: #FFFFFF;
  animation: ${RecLabelAnimation} 1s ease-in-out infinite alternate;
`;

const ResultContainer = styled.div`
  background-color: #FFFFFF;
  display: flex;
  flex-direction: column;
  min-width: 650px;
`;

const Title = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  font-size:  20px;
  height: 30px;
  width: 100px;
`;

const VoiceCell = styled.div`
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

class Player extends React.Component<any, any> {
  state = {
    playing: false
  }

  audioRef = null;

  doPlay = ()  => {
    this.audioRef.play();
    this.setState({
      playing: true
    });

  }

  doStop = () => {
    this.audioRef.pause();
    this.setState({
      playing: false
    });
  }

  handleOnPause = () => {
    this.setState({
      playing: false
    });
  }

  render() {
    return (
      <>
        <VoiceCell>
          {this.state.playing
            ? <FontAwesomeIcon icon={faStopCircle} size={'2x'} onClick={this.doStop} />
            : <FontAwesomeIcon icon={faPlayCircle} size={'2x'} onClick={this.doPlay} />
          }
        </VoiceCell>
        <audio
          key={`key-${this.props.id}`}
          id={this.props.id}
          ref={dom => this.audioRef = dom}
          onPause={this.handleOnPause}
        >
          <source src={this.props.src} />
        </audio>
      </>
    );
  }
}

export default App;

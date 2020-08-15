import React from 'react';
import styled, { keyframes } from 'styled-components';
import { faMicrophoneAlt, faPlayCircle, faStopCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import FiberManualRecordIcon from '@material-ui/icons/FiberManualRecord';

import Audio from "../utils/Audio";
import Sockets from "../utils/Sockets";

enum Status {
  STARTED,
  STOPPED
}


class App extends React.Component<any, any> {
  state = {
    status: Status.STOPPED
  }

  audio = new Audio();
  sockets = new Sockets("http://localhost:8080");

  componentDidMount() {
    // this.sockets.on("connect", () => console.log("connected"));
    // this.sockets.sendText("connect", "hello");
    console.log(this.sockets.isConnected);
  }

  handleStartRecord = () => {
    this.audio.handleStart();
    this.sockets.sendText('message', { message: "start" });
    this.setState ({
      status: Status.STARTED
    });
  }

  handleStopRecord = () => {
    this.audio.handleStop();
    this.setState ({
      status: Status.STOPPED
    });
    this.sockets.sendText('message', this.audio.recordedData);
  }

  handlePlay = () => {
    const audioElement = document.getElementById("player");
    if (audioElement) {
      this.audio.handlePlay(audioElement);
    }
  }

  render() {
    const data = [
      {
        "text": "aaaaaaa"
      },
      {
        "text": "bbbbbbbbb"
      },
      {
        "text": "cccccccccccccccccccccccccccccccccccc"
      }
    ];

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
        <ResultContainer isVisible={data.length !== 0}>
          <Title>Results</Title>
          <ResultTable>
            {data.map((d, idx) => {
              return <Row key={`row-key-${idx}`}>
                <TextCell>{d.text}</TextCell>
                <VoiceCell>
                  <FontAwesomeIcon icon={faPlayCircle} size={'2x'} onClick={this.handlePlay} />
                </VoiceCell>
              </Row>
            })}
          </ResultTable>
        </ResultContainer>
        <audio id={"player"} />
      </Container>
    );
  }
}

const Container = styled.div`
  background-color: #EDF6FF;
  width: 100vw;
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
  height: 250px;
  width: 400px;
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

const ResultContainer = styled.div<{ isVisible: boolean }>`
  background-color: #FFFFFF;
  display: flex;
  flex-direction: column;
  width: 600px;
  visibility: ${({ isVisible }) => (isVisible ? 'visible'  : 'hidden')};
`;

const Title = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  font-size:  24px;
  height: 50px;
  width: 100px;
`;

const ResultTable = styled.div`
  display: flex;
  flex-direction: column;
  width: 100%;
  padding: 5px;
`;

const Row = styled.div`
  display: flex;
  align-items: center;
  width: calc(100% - 10px);
  border-bottom: 1px solid #DFDFDF;
  height: 50px;
`;

const TextCell = styled.div`
  width: 560px;
`;

const VoiceCell = styled.div`
  width: 30px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;


export default App;

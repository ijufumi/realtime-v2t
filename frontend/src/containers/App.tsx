import React from 'react';
import styled from 'styled-components';
import { faMicrophoneAlt, faPlayCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import FiberManualRecordIcon from '@material-ui/icons/FiberManualRecord';

enum Status {
  STARTED,
  STOPPED
}


class App extends React.Component<any, any> {
  state = {
    status: Status.STOPPED
  }

  handleStartRecord = () => {
    // const recordedChunks = [];
    // const player = document.getElementById('player');
    //
    // const handleSuccess = function(stream) {
    //   const mediaStream = new MediaStream(stream)
    //
    //   const mediaRecorder = new MediaRecorder(stream, options);
    //
    //   mediaStream.addEventListener('dataavailable', function(e) {
    //     if (e.data.size > 0) {
    //       recordedChunks.push(e.data);
    //     }
    //
    //     if(shouldStop === true && stopped === false) {
    //       mediaStream.stop();
    //       stopped = true;
    //     }
    //   });
    // };
    //
    // navigator.mediaDevices.getUserMedia({ audio: true, video: false }).then(handleSuccess);

    this.setState ({
      status: Status.STARTED
    });
  }

  handleStopRecord = () => {
    this.setState ({
      status: Status.STOPPED
    });
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
          <StopButtonBlock>
            <FiberManualRecordIcon htmlColor={'red'} onClick={this.handleStopRecord} />
          </StopButtonBlock>
        </StopButtonContainer>
        <MikeContainer onClick={this.handleStartRecord}>
          <FontAwesomeIcon icon={faMicrophoneAlt} size={'10x'}/>
        </MikeContainer>
        <ResultContainer>
          <Title>Result</Title>
          <ResultTable>
            {data.map((d, idx) => {
              return <Row key={`row-key-${idx}`}>
                <TextCell>{d.text}</TextCell>
                <VoiceCell>
                  <FontAwesomeIcon icon={faPlayCircle} size={'2x'} />
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

const MikeContainer = styled.div`
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
  display: ${({ isVisible }) => (isVisible ? ''  : 'none')};
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

const ResultContainer = styled.div`
  background-color: #FFFFFF;
  display: flex;
  flex-direction: column;
  width: 600px;
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

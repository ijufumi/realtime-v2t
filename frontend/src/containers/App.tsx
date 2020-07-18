import React from 'react';
import styled from 'styled-components';
import {faMicrophoneAlt, faVoicemail} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";


class App extends React.Component<any, any> {
  handleStartRecord = () => {

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
        <MikeContainer onClick={this.handleStartRecord}>
          <FontAwesomeIcon icon={faMicrophoneAlt} size={'10x'}/>
        </MikeContainer>
        <ResultContainer>
          <Title>Result</Title>
          <ResultTable>
            {data.map(d => {
              return <Row>
                <TextCell>{d.text}</TextCell>
                <VoiceCell>
                  <FontAwesomeIcon icon={faVoicemail}/>
                </VoiceCell>
              </Row>
            })}
          </ResultTable>
        </ResultContainer>
      </Container>
    );
  }
}

const Container = styled.div`
  background-color: #EDF6FF;
  width: 100vw;
  height: 100vh;
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
  height: 30px;
`;

const TextCell = styled.div`
  width: 560px;
`;

const VoiceCell = styled.div`
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
`;


export default App;

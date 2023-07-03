import Message from "./Message";
import React, { useState, useEffect } from "react";
import backgroundImg from ".././img/scene_1/1.png";
import "./MessagesContainer.css";
import Scene from "./Check";
import { FcSalesPerformance, FcLike, FcPlus } from "react-icons/fc";
import { TransitionGroup, CSSTransition } from 'react-transition-group';

// const content = {
//   "background_image": "./img/scene_1/1.png",
//   "id": 1,
//   "choices": [
//     {
//       "choice_text": "持ってこれるだけ持ってこいよ！",
//       "scene_id": 1,
//       "id": 1,
//       "text_sets_id":[2]
//     },
//     {
//       "choice_text": "いやぁ、無理しない範囲で大丈夫だよ",
//       "scene_id": 1,
//       "id": 2,
//       "text_sets_id":[2,3]
//     }
//   ],
//   "text_sets": [
//     {
//       "id": 1,
//       "scene_id": 1,
//       "texts": [
//         {
//           "progress": 0,
//           "text": "ひらちん：「お、今日夕方から同伴予定の女の子Aから連絡だ。」",
//           "background_image": "1.png",
//           "mental": 0,
//           "satisfaction": 0,
//           "id": 1,
//           "gender": "male",
//           "money": 0,
//           "text_set_id": 1
//         },
//         {
//           "progress": 0,
//           "text": "女性A：「今日Takuyaに会えるの楽しみー！どれくらいお金持っていけばいいかな？」",
//           "background_image": "2.png",
//           "mental": 0,
//           "satisfaction": 0,
//           "id": 2,
//           "gender": "female",
//           "money": 0,
//           "text_set_id": 1
//         },
//         {
//           "progress": 0,
//           "text": "女性A：「今日Takuyaに会えるの楽しみー！どれくらいお金持っていけばいいかな？」",
//           "background_image": "3.png",
//           "mental": 0,
//           "satisfaction": 0,
//           "id": 3,
//           "gender": "female",
//           "money": 0,
//           "text_set_id": 1
//         }
//       ]
//     },
//     {
//       "id": 2,
//       "scene_id": 1,
//       "texts": [
//         {
//           "progress": 20,
//           "text": "Takuya：「無理しない範囲で大丈夫だよ」",
//           "background_image": "4.png",
//           "mental": 0,
//           "satisfaction": 0,
//           "id": 4,
//           "gender": "male",
//           "money": -50,
//           "text_set_id": 2
//         }
//       ]
//     },
//     {
//       "id": 3,
//       "scene_id": 1,
//       "texts": [
//         {
//           "progress": 20,
//           "text": "Takuya：「無理しない範囲で大丈夫だよ」",
//           "background_image": "Example background",
//           "mental": 0,
//           "satisfaction": 0,
//           "id": 4,
//           "gender": "male",
//           "money": -50,
//           "text_set_id": 2
//         },
//         {
//           "progress": 20,
//           "text": "Takuya：「無理しない範囲で大丈夫だよ」",
//           "background_image": "5.png",
//           "mental": 0,
//           "satisfaction": 0,
//           "id": 4,
//           "gender": "male",
//           "money": -50,
//           "text_set_id": 2
//         }
//       ]
      
//     }
//   ],

// };



const ProgressBar = ({ progress }) => (
  <div style={{ display: 'flex', alignItems: 'center', width: '100%'}}>
    <div style={{ fontWeight: 'bold' }}>課題進捗:{progress} %</div>
    <progress style={{ width: '70%', height: '2em'  }} max="100" value={progress}></progress>
  </div>
);


const StatusDisplay = ({ Icon, value }) => (
  <div className="status-item" style={{ fontSize: '2em' }}>
    <Icon className="icon" size="2em"/>
    <TransitionGroup>
      {value != null && (
        <CSSTransition
          key={value}
          timeout={2000}
          classNames="fade"
        >
          <div className={`colorChange textGlow`}>{value}</div>
        </CSSTransition>
      )}
    </TransitionGroup>
  </div>
);

// 状態を表示するコンポーネント
const Status = ({ progress, money, mental, satisfaction }) => (
  <div className="status-container">
    <ProgressBar progress={progress} />
    <div className="status-subcontainer">
    <StatusDisplay Icon={FcSalesPerformance} value={money} />
    <StatusDisplay Icon={FcLike} value={mental} />
    <StatusDisplay Icon={FcPlus} value={satisfaction} />
    </div>
  </div>
);



const Messages = ({ content }) => {
  const [message, setMessage] = useState(null);
  const [choices, setChoices] = useState([]);
  const [currentMessageIndex, setCurrentMessageIndex] = useState(0);
  const [isDisplayingChoices, setIsDisplayingChoices] = useState(false);
  const [currentTextSetIndex, setCurrentTextSetIndex] = useState(0);
  const [hasDisplayedChoices, setHasDisplayedChoices] = useState(false);
  const [borderColor, setBorderColor] = useState('white');
  const [progress, setProgress] = useState(0);
  const [money, setMoney] = useState(300);
  const [mental, setMental] = useState(50);
  const [satisfaction, setSatisfaction] = useState(50);
  // const [backgroundImg, setBackgroundImg] = useState(null);

  useEffect(() => {
    console.log(content);
}, [content]);

  const handleChoiceClick = (textSetIds) => {
    const randomTextSetId = textSetIds[Math.floor(Math.random() * textSetIds.length)];
    const newTextSetIndex = content.text_sets.findIndex(text_set => text_set.id === randomTextSetId);
    setCurrentTextSetIndex(newTextSetIndex);
    setCurrentMessageIndex(0);
    setIsDisplayingChoices(false);
    setMessage(null);
  };

  useEffect(() => {
    if (currentMessageIndex < content.text_sets[currentTextSetIndex].texts.length+1) {
      const timer = setTimeout(() => {
        setMessage(content.text_sets[currentTextSetIndex].texts[currentMessageIndex]);
        setCurrentMessageIndex(currentMessageIndex => currentMessageIndex + 1);
      }, 3000); 

      return () => clearTimeout(timer);
    } else if (!isDisplayingChoices && !hasDisplayedChoices) {
      setChoices(content.choices);
      setIsDisplayingChoices(true);
      setHasDisplayedChoices(true);
    }
  }, [currentMessageIndex, isDisplayingChoices, hasDisplayedChoices, currentTextSetIndex]);
  useEffect(() => {
    if (message) {
      setBorderColor(message.gender === 'male' ? 'blue' : 'red');
    }
  }, [message]); 

  // useEffect(() => {
  //   if (message && message.background_image) {
  //     setBackgroundImg(`.././img/scene_1/${message.background_image}`);
  //   }
  // }, [message]);

  useEffect(() => {
    if (message) {
      setProgress(prevProgress => prevProgress + message.progress);
      setMoney(prevMoney => prevMoney + message.money);
      setMental(prevMental => prevMental + message.mental);
      setSatisfaction(prevSatisfaction => prevSatisfaction + message.satisfaction);
    }
  }, [message]);

  const messageBoxStyle = {
    borderColor, 
  };
  const backgroundStyle = {
    backgroundImage: `url(${backgroundImg})`,
  };


  return (
    <div className="MessagesContainer" style={{ ...backgroundStyle }}>
    <Status progress={progress} money={money} mental={mental} satisfaction={satisfaction} />
      <div className="MessageBox" style={messageBoxStyle}>
        {message && <Message key={message.id} content={message.text}/>}
      </div>
      {isDisplayingChoices && 
      <div className="ChoicesBox">
          {choices.map((choice, index) =>
            <button className="ChoiceButton" key={index} onClick={() => handleChoiceClick(choice.text_sets_id)}>{choice.choice_text}</button>
          )}
        </div>
      }
    </div>
  );
};

export default Messages;
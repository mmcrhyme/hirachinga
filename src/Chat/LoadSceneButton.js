import React, { useState } from 'react';
import Scene from "./Check";
import './LoadSceneButton.css';
import { TransitionGroup, CSSTransition } from 'react-transition-group';

function LoadSceneButton() {
  // ボタンがクリックされたらこのstateが更新され、それによりSceneコンポーネント内のuseEffectがトリガーされます。
  const [clicked, setClicked] = useState(false);

  return (
      <div className="background">
          <button className= {`load-button ${clicked && 'hide'}`} onClick={() => setClicked(!clicked)}>入学する</button>
          <Scene shouldFetch={clicked} />
      </div>
  );
}

export default LoadSceneButton;
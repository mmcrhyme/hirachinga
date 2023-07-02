import React from "react";
import Messages from "./Messages";
import Scene from "./Check";


const Chat = ({content}) => {
  return (
    <Messages  content={content}/>
  );
};

export default Chat;

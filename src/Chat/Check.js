import React, { useState, useEffect } from 'react';
import Chat from './Chat';

function Scene() {
    // 状態を初期化します。
    const [scene, setScene] = useState(null);

    useEffect(() => {
        // APIからデータを取得します。
        fetch('http://0.0.0.0:8000/scenes/1', {
            method: 'GET',
            headers: {
                'Accept': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => setScene(data)) 
        .catch(error => console.error('Error:', error));
    }, []);  // 空の依存配列を渡して、コンポーネントのマウント時にのみfetchが実行されるようにします。

    // sceneがnullのとき（データがまだ取得できていないとき）は、ローディングメッセージを表示します。
    if (!scene) {
        return <div>Loading...</div>;
    }

    // 取得したデータを表示します。
    return (
        // <div>
        //     <h2>Scene Information</h2>


        //     <p>Text: {scene.text}</p>
        //     <p>ID: {scene.id}</p>

        //     <h2>Choices</h2>

        //     {scene.choices.map((choice, index) => (
        //         <div key={index}>
        //             <h3>Choice {index + 1}</h3>
        //             <p>Choice Text: {choice.choice_text}</p>
        //             <p>Scene ID: {choice.scene_id}</p>
        //             <p>ID: {choice.id}</p>
        //         </div>
        //     ))}
        // </div>
    <Chat content={scene} />
    );
}

export default Scene;
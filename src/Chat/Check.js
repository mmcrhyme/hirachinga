import React, { useState, useEffect } from 'react';
import Chat from './Chat';

function Scene({ shouldFetch }) {
    // 状態を初期化します。
    const [scene, setScene] = useState(null);

    useEffect(() => {
        if (!shouldFetch) return;

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
    }, [shouldFetch]);  // shouldFetchが更新されるたびにこのeffectが実行されます。

    // sceneがnullのとき（データがまだ取得できていないとき）は、ローディングメッセージを表示します。
    if (!scene) {
        return <div>Loading...</div>;
    }

    // 取得したデータを表示します。
    return <Chat content={scene} />;
}

export default Scene;
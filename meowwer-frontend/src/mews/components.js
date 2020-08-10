import React, { useEffect, useState } from 'react';
import { loadMews } from '../lookup'

export function MewList(props) {
    const [mews, setMews] = useState([]);

    useEffect(() => {
        const mycallback = (response, status) => {
            if (status === 200) {
                setMews(response);
            } else {
                alert("There was an error");
            }
        };
        loadMews(mycallback);
    }, []);

    return mews.map((mew, index) => {
        return <Mew mew={mew} key={index} />;
    })
}

export function ActionBtn(props) {
    const { mew, action } = props;
    const [likes, setLikes] = useState(mew.likes ? mew.likes : 0)
    const [userLike, setUserLike] = useState(mew.userLike === true ? true : false)
    const className = props.className ? props.className : "btn btn-primary btn-sm";
    const actionDisplay = action.display ? action.display : "Action"
    const handleClick = (event) => {
        event.preventDefault()
        if (action.type === 'like') {
            if (userLike === true) {
                setLikes(likes - 1)
                setUserLike(false)
            } else {
                setLikes(likes + 1)
                setUserLike(true)
            }
        }
    }
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
    return <button className={className} onClick={handleClick}>{display}</button>
}

export function Mew(props) {
    const mew = props.mew;
    const className = props.className ? props.className : "col-10 mx-auto col-md-6";
    return (
        <div className={className}>
            <p>
                {mew.id} - {mew.content}
            </p>
            <div>
                <ActionBtn mew={mew} action={{ type: "like", display: "likes" }} />
                <ActionBtn mew={mew} action={{ type: "unlike", display: "unlike" }} />
                <ActionBtn mew={mew} action={{ type: "remew", display: "remew" }} />
            </div>
        </div>
    );
}
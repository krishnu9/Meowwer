import React, { useEffect, useState } from 'react';
import {loadMews} from '../lookup'

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
    const className = props.className ? props.className : "btn btn-primary btn-sm";
    return action.type === "like" ? <button className={className}>{mew.likes} Like</button> : null;
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
                <ActionBtn mew={mew} action={{ type: "like" }} />
                <ActionBtn mew={mew} action={{ type: "unlike" }} />
            </div>
        </div>
    );
}
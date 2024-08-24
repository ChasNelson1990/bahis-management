import React, {useEffect, useState} from 'react';
import {FormControl, InputLabel, MenuItem, Select, SelectChangeEvent} from "@mui/material";
import {useGetUsersQuery} from "./userApiSlice.ts";
import {useDispatch} from "react-redux";
import {setUsers, UserType} from "./userSlice.ts";


function User() {
    const [selectedUserId, setSelectedUserId] = useState('')
    const dispatch = useDispatch()


    const {data: userList} = useGetUsersQuery(null)


    useEffect(() => {
        // console.log("dispatch user");
        dispatch(setUsers(userList))
    }, [userList])


    const handleChange = (evt: SelectChangeEvent) => {
        setSelectedUserId(evt.target.value);
    }

    return (
        <div className={'my-3'}>
            <FormControl fullWidth>
                <InputLabel id="user-list-label">User List</InputLabel>
                <Select
                    labelId="user-list-label"
                    label="User List"
                    value={selectedUserId}
                    onChange={handleChange}
                >
                    {userList?.map((user) => (
                        <MenuItem key={user.id} value={user.id}>{user.username}</MenuItem>
                    ))}
                </Select>
            </FormControl>
        </div>
    );
}

export default User;
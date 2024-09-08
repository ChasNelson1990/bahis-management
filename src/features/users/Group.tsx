import React, {useEffect, useState} from 'react';
import {FormControl, InputLabel, MenuItem, Select, SelectChangeEvent} from "@mui/material";
import {useGetGroupsQuery} from "./userApiSlice.ts";
import {useDispatch} from "react-redux";
import {GroupType} from "./User.model.ts";

// import {setGroups, GroupType} from "./userSlice.ts";


function Group() {
    const [selectedGroupId, setSelectedGroupId] = useState('')
    const dispatch = useDispatch()


    const {data: groupList} = useGetGroupsQuery()


    // useEffect(() => {
    //     // console.log("dispatch group");
    //     dispatch(setGroups(groupList))
    // }, [groupList])


    const handleChange = (evt: SelectChangeEvent) => {
        setSelectedGroupId(evt.target.value);
    }

    return (
        <div className={'my-3'}>
            <FormControl fullWidth>
                <InputLabel id="group-list-label">Group List</InputLabel>
                <Select
                    labelId="group-list-label"
                    label="Group List"
                    value={selectedGroupId}
                    onChange={handleChange}
                >
                    {groupList?.map((group) => (
                        <MenuItem key={group.id} value={group.id}>{group.name}</MenuItem>
                    ))}
                </Select>
            </FormControl>
        </div>
    );
}

export default Group;
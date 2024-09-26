import {createSlice} from "@reduxjs/toolkit";
import {UserType} from "./User.model.ts";


export interface UserInitialState {
    users: UserType[],
}

const initialState: UserInitialState = {
    users: [],
}

export const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        setUsers(state, action) {
            state.users = action.payload
        }
    },
    selectors: {
        selectUsers: state => state.users,
    }
})

export const {selectUsers} = userSlice.selectors
export const {setUsers} = userSlice.actions
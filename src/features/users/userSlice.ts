import {createSlice} from "@reduxjs/toolkit";

export interface UserType {
    id: number,
    username: string,
    is_superuser: boolean,
    date_joined: string,
    last_login: string,
    is_active: boolean,
    email: string,
    asset_count: number,
    metadata: object
}

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
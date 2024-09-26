import {createSlice} from "@reduxjs/toolkit";
import {FormInitialState} from "./form.model.ts";


const initialState: FormInitialState = {
    forms: [],
    permissions: []
}

export const formSlice = createSlice({
    name: 'form',
    initialState,
    reducers: {
        setForms(state, action) {
            state.forms = action.payload
        },
        setPermissions(state, action) {
            state.permissions = action.payload
        }
    },
    selectors: {
        selectForms: state => state.forms,
        selectPermissions: state => state.permissions
    }
})

export const getPermissionsByFormId = (state: FormInitialState, formId: string) => {
    return state.forms?.find(form => form.uid === formId)?.permissions
}
export const {selectForms, selectPermissions} = formSlice.selectors
export const {setForms, setPermissions} = formSlice.actions
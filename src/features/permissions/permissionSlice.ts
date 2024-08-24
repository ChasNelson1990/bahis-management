import {createSlice} from "@reduxjs/toolkit";
import {LocalPermissionType, PermissionTreeType} from "./Permission.model.ts";

export const PARTIAL_PERMIT = "partial_permissions"
export const PARTIAL_SUBMIT = "partial_submissions"
export const PERMISSIONS = [
    {
        "permission": "view_asset",
        "label": "View form",
        muiIcon: '',
    },
    {
        "permission": "add_submissions",
        "label": "Add submissions",
        muiIcon: '',
    },
    {
        "permission": "view_submissions",
        "label": "View submissions only from specific users",
        type: PARTIAL_PERMIT,
        muiIcon: '',
    },
    {
        "permission": "change_submissions",
        "label": "Edit submissions only from specific users",
        type: PARTIAL_PERMIT,
        muiIcon: '',
    },
    {
        "permission": "delete_submissions",
        "label": "Delete submissions only from specific users",
        type: PARTIAL_PERMIT,
        muiIcon: '',
    },
    {
        "permission": "validate_submissions",
        "label": "Validate submissions only from specific users",
        type: PARTIAL_PERMIT,
        muiIcon: '',
    },
]

interface PermissionInitialState {
    selectedPermissionsIds: []
    localPermissions: LocalPermissionType[],
    permissionTreeData: PermissionTreeType
}

const initialState: PermissionInitialState = {
    selectedPermissionsIds: [],
    localPermissions: PERMISSIONS,
    permissionTreeData: {}
}

export const permissionSlice = createSlice({
    name: 'permission',
    initialState,
    reducers: {
        setSelectedPermissionsIds(state, action) {
            state.selectedPermissionsIds = action.payload
        },
        setPermissionTreeData(state, action) {
            state.permissionTreeData = action.payload
        },
    },
    selectors: {
        selectedPermissionsIds: state => state.selectedPermissionsIds,
        selectLocalPermissions: state => state.localPermissions,
        selectPermissionTreeData: state => state.permissionTreeData,
    }
})

export const {
    selectedPermissionsIds,
    selectLocalPermissions,
    selectPermissionTreeData,
} = permissionSlice.selectors
export const {
    setSelectedPermissionsIds,
    setPermissionTreeData,
} = permissionSlice.actions

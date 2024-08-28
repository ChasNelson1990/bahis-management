import {useDispatch, useSelector} from "react-redux";
import {selectForms} from "../forms/formSlice.ts";
import {
    convertTreeToPermissions,
    getBlankPermission,
    getLocalPermissionsPerUser
} from "../../utils/UserPermissionUtils.ts";
import {Permission} from "./Permission.tsx";
import {FormType} from "../forms/form.model.ts";
import {LocalPermissionType, PermissionTreeType} from "./Permission.model.ts";
import {
    Box,
    Button,
    FormControl,
    FormControlLabel,
    InputLabel,
    MenuItem,
    Select,
    SelectChangeEvent,
    Typography
} from "@mui/material";
import {SimpleTreeView, TreeItem2} from "@mui/x-tree-view";
import React, {SyntheticEvent, useEffect, useRef, useState} from "react";
import {
    selectLocalPermissions,
    selectedPermissionsIds,
    selectPermissionTreeData,
    setPermissionTreeData,
    setSelectedPermissionsIds
} from "./permissionSlice.ts";
import Checkbox from "@mui/material/Checkbox";
import {useGetUsersQuery} from "../users/userApiSlice.ts";
import {Add} from "@mui/icons-material";
import {useSubmitBulkPermissionMutation} from "./permissionApiSlice.ts";

interface PermissionProps {
    formId: string
}


export const Permissions = (props: PermissionProps) => {
    const forms: FormType[] = useSelector(selectForms);
    const selectedPermit: [] = useSelector(selectedPermissionsIds);
    const localPermission: LocalPermissionType[] = useSelector(selectLocalPermissions);
    const permissionTreeData: PermissionTreeType = useSelector(selectPermissionTreeData);
    const {data: userList} = useGetUsersQuery(null)
    const [submitBulkPermission, {isLoading, isSuccess}] = useSubmitBulkPermissionMutation()

    const [selectedPermissions, setSelectedPermissions] = useState<Set<string>>(new Set())
    const [owner, setOwner] = useState<string>()
    const [selectedUser, setSelectedUser] = useState('')

    const dispatch = useDispatch()

    const rnd = useRef(0)

    useEffect(() => {
        rnd.current = rnd.current + 1
    });


    useEffect(() => {
        const {
            permissionTree,
            currentPermissions,
            owner
        } = getLocalPermissionsPerUser(forms, localPermission, props.formId);
        dispatch(setPermissionTreeData(permissionTree))
        setSelectedPermissions(currentPermissions)
        setOwner(owner)
    }, [dispatch, forms, localPermission, props.formId])


    useEffect(() => {
        dispatch(setSelectedPermissionsIds(Array.from(selectedPermissions)))
    }, [dispatch, selectedPermissions]);

    const handleChangePermission = (event: SyntheticEvent, itemId: string, isSelected: boolean) => {
        if (isSelected) {
            // if item is user
            if (Object.keys(permissionTreeData).includes(itemId)) {
                setSelectedPermissions(prev => {
                    return new Set<string>([...prev, ...Object.values(permissionTreeData[itemId]).map(permit => permit.id), itemId])
                })
            } else {
                setSelectedPermissions(prev => {
                    return new Set<string>([...prev, itemId])
                })
            }

        } else {
            // if item is user
            if (Object.keys(permissionTreeData).includes(itemId)) {
                const itemsToRemove = [...Object.values(permissionTreeData[itemId]).map(permit => permit.id), itemId]
                setSelectedPermissions(prev => new Set([...prev].filter(permit => !itemsToRemove.includes(permit))))
            } else {
                setSelectedPermissions(prev => new Set([...prev].filter(permit => permit != itemId)))
            }
        }
    }
    const handleChangeUser = (evt: SelectChangeEvent) => {
        setSelectedUser(evt.target.value);
    }
    const handleAddUser = () => {
        if (selectedUser) {
            const blankPermission = getBlankPermission(selectedUser, localPermission)
            setSelectedUser('')
            dispatch(setPermissionTreeData({...blankPermission, ...permissionTreeData}))
        }
    }
    const savePermission = () => {
        const bulkPermission = convertTreeToPermissions(permissionTreeData, selectedPermissions)
        submitBulkPermission({bulkPermission, formId: props.formId})
    }


    return (
        <div>
            <Typography variant="h3" gutterBottom>
                Permissions {rnd.current}
            </Typography>
            <div className={"flex flex-col"}>
                <div className={"mb-5 self-end"}>
                    <Button onClick={savePermission} variant="contained">Save</Button>
                </div>
                <div>
                    <FormControlLabel control={<Checkbox/>} label="Select All"/>
                    <FormControlLabel control={<Checkbox/>} label="Unselect All"/>
                    <FormControlLabel control={<Checkbox/>} label="Expand All"/>
                    <FormControlLabel control={<Checkbox/>} label="Collapse All"/>
                </div>

                {
                    isLoading ? 'Loading...' :
                    <Box display="flex" alignItems="center"
                         className={'my-5'}
                         gap={2}>
                        <FormControl fullWidth size='small'>
                            <InputLabel id="user-list-label">User List</InputLabel>
                            <Select
                                labelId="user-list-label"
                                label="User List"
                                value={selectedUser}
                                onChange={handleChangeUser}>
                                {userList?.map((user) => (
                                    (user.id !== -1 && !Object.keys(permissionTreeData).includes(user.username)) &&
                                    <MenuItem key={user.id} value={user.username}>{user.username}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                        <Button variant='contained'
                                onClick={handleAddUser}
                                startIcon={<Add/>}
                                sx={{'minWidth': '10rem'}}>Add User</Button>
                    </Box>
                }
                <SimpleTreeView
                    defaultExpandedItems={['sharful', 'bamna']}
                    selectedItems={selectedPermit}
                    onItemSelectionToggle={handleChangePermission}
                    checkboxSelection
                    multiSelect>
                    {Object.keys(permissionTreeData)?.map(user => (
                        <TreeItem2 key={user}
                                   label={user === owner ? (user + ' (Owner)') : user}
                                   itemId={user}
                                   disabled={user === owner}>
                            <Permission userPermission={permissionTreeData[user]} user={user}/>
                        </TreeItem2>
                    ))}
                </SimpleTreeView>
                <div className={"mt-5 self-end"}>
                    <Button onClick={savePermission} variant="contained">Save</Button>
                </div>
            </div>
        </div>
    )
}

import * as React from 'react';
import {styled} from '@mui/material/styles';
import {
    unstable_useTreeItem2 as useTreeItem2,
    UseTreeItem2Parameters,
} from '@mui/x-tree-view/useTreeItem2';
import {
    TreeItem2Content,
    TreeItem2IconContainer,
    TreeItem2GroupTransition,
    TreeItem2Label,
    TreeItem2Root,
    TreeItem2Checkbox,
} from '@mui/x-tree-view/TreeItem2';
import {TreeItem2Icon} from '@mui/x-tree-view/TreeItem2Icon';
import {TreeItem2Provider} from '@mui/x-tree-view/TreeItem2Provider';
import {FilterMultiUser, FilterType, UserPermissionTreeType, UserPermissionType} from "./Permission.model.ts";
import {Autocomplete, Stack} from "@mui/material";
import {PARTIAL_PERMIT, selectPermissionTreeData, setPermissionTreeData} from "./permissionSlice.ts";
import TextField from "@mui/material/TextField";
import {useGetUsersQuery} from "../users/userApiSlice.ts";
import {UserType} from "../users/User.model.ts";
import {useEffect, useState} from "react";
import {useDispatch, useSelector} from "react-redux";
import user from "../users/User.tsx";

const PermissionTreeItemContent = styled(TreeItem2Content)(({theme}) => ({
    padding: theme.spacing(1, 1),
    backgroundColor: 'transparent',
    '&:hover': {
        backgroundColor: 'transparent',
    },
}));

interface PermissionTreeItemProps
    extends Omit<UseTreeItem2Parameters, 'rootRef'>,
        Omit<React.HTMLAttributes<HTMLLIElement>, 'onFocus'> {
    permitData: UserPermissionType,
    user: string,
    formOwner?: string
}

export const PermissionTreeItem = React.forwardRef(function PermissionTreeItem(
    props: PermissionTreeItemProps,
    ref: React.Ref<HTMLLIElement>,
) {

    const {id, itemId, label, disabled, children, permitData, user: currentUser, formOwner, ...other} = props;
    const {
        getRootProps,
        getContentProps,
        getIconContainerProps,
        getCheckboxProps,
        getLabelProps,
        getGroupTransitionProps,
        status,
    } = useTreeItem2({id, itemId, children, label, disabled, rootRef: ref});

    const {data: userList} = useGetUsersQuery(null)

    const [userValues, setUserValues] = useState<string[]>([])
    const [owner, setOwner] = useState<UserType>({} as UserType)
    const [otherUsers, setOtherUsers] = useState<string[]>([])
    const permissionTreeData: UserPermissionTreeType = useSelector(selectPermissionTreeData);

    const dispatch = useDispatch()

    useEffect(() => {
        const submittedBy: string | FilterMultiUser = permitData.filters?.filter(fltr => fltr._submitted_by)[0]._submitted_by

        let defaultUserValue: Set<string> = new Set<string>([]);
        if (typeof submittedBy === 'string') {
            defaultUserValue = new Set<string>([submittedBy])
        } else {
            if (submittedBy && Object.prototype.hasOwnProperty.call(submittedBy, '$in')) {
                defaultUserValue = new Set<string>(submittedBy.$in)
            }
        }

        const own = userList?.find(user => user.username === currentUser) as UserType;
        if (own) {
            defaultUserValue.add(own.username)
        }
        setOwner(own)
        setUserValues([...defaultUserValue])
        setOtherUsers(getUsers())

    }, [permitData.filters, props.user, userList]);


    const getUsers = () => {
        return userList?.filter(user => user?.username !== formOwner && user.id > 0).map(user => user.username) || []
    }
    const changeUserValue = (event, newValue) => {
        const newUsers = [
            owner.username,
            ...newValue.filter(option => option !== owner.username),
        ]
        setUserValues(newUsers);

        if (!getCheckboxProps().checked) return;

        const permissionData: UserPermissionType = permissionTreeData[currentUser][permitData.permission];
        let filters: FilterType[]
        if (newUsers.length > 1) {
            filters = [{_submitted_by: {$in: newUsers}}]
        } else {
            filters = [{_submitted_by: newUsers[0]}]

        }

        dispatch(setPermissionTreeData({
            ...permissionTreeData,
            [currentUser]: {
                ...permissionTreeData[currentUser],
                [permitData.permission]: {
                    ...permissionData,
                    filters,
                },
            },
        }))

    }

    return (
        <TreeItem2Provider itemId={itemId}>
            <TreeItem2Root {...getRootProps(other)}>
                <PermissionTreeItemContent {...getContentProps()}>
                    <TreeItem2IconContainer {...getIconContainerProps()}>
                        <TreeItem2Icon status={status}/>
                    </TreeItem2IconContainer>
                    <TreeItem2Checkbox sx={{alignSelf: 'start'}} {...getCheckboxProps()} />
                    <Stack sx={{display: 'flex', width: '50%'}} spacing={1}>
                        <TreeItem2Label {...getLabelProps()} />
                        {(permitData.type === PARTIAL_PERMIT) &&
                            <Autocomplete
                                multiple
                                size={'small'}
                                value={userValues}
                                options={otherUsers}
                                disabled={!getCheckboxProps().checked}
                                onChange={changeUserValue}
                                renderInput={(params) => (
                                    <TextField
                                        {...params}
                                        variant="standard"
                                        label="User name"
                                        placeholder="User name"
                                        onClick={evt => {
                                            evt.preventDefault()
                                            evt.stopPropagation()
                                        }}
                                    />
                                )}
                            />
                        }

                    </Stack>
                </PermissionTreeItemContent>
                {children && <TreeItem2GroupTransition {...getGroupTransitionProps()} />}
            </TreeItem2Root>
        </TreeItem2Provider>
    );
});


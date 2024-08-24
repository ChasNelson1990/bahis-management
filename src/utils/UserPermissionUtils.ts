import {
    BulkPermissionType,
    KoboPermissionType,
    LocalPermissionType, PartialPermissionType,
    PermissionTreeType,
    PermissionType,
    TreeNode
} from "../features/permissions/Permission.model.ts";
import {PARTIAL_PERMIT, PARTIAL_SUBMIT} from "../features/permissions/permissionSlice.ts";
import {FormType} from "../features/forms/form.model.ts";


function findWordAfter(url: string, firstWord: string) {
    // Construct a regular expression to capture the word following the firstWord
    const regex = new RegExp(`${firstWord}/([^/]+)`, 'i');

    // Execute the regex against the URL
    const match = url.match(regex);

    // If a match is found, return the captured word; otherwise, return null
    return match ? match[1] : '';
}

function getPermissionName(url: string): string {
    return findWordAfter(url, 'permissions')
}

function makeUrl(word: string, prefix: string = '', sufix: string = ''): string {
    const kfApiUrl = import.meta.env.VITE_KF_API_URL;
    return kfApiUrl + prefix + word + sufix;
}

function getPermissionTreePerUser(permissions, owner) {
    const permissionTree: PermissionTreeType = {};
    const selectedPermissions: Set<string> = new Set()
    permissions?.forEach((permission: PermissionType, index) => {
        const userName = findWordAfter(permission.user, 'users')
        const permissionName = getPermissionName(permission.permission)
        if (!Object.prototype.hasOwnProperty.call(permissionTree, userName)) {
            permissionTree[userName] = {}
        }
        const id = userName.concat('.', permissionName);
        const label = (typeof permission.label === 'string') ? permission.label : permissionName
        const {partial_permissions} = permission

        permissionTree[userName][permissionName] = {
            id,
            permission: permissionName,
            label: label,
            isExist: true,
            partial_permissions,
            isOwner: userName === owner
        }

        selectedPermissions.add(id)
    })
    return {permissionTree, selectedPermissions};
}

export function getBlankPermission(user: string, localPermissions) {
    const permissionTreeItem: PermissionTreeType = {[user]: {}};

    localPermissions?.map(({permission, label, type}) => {
        permissionTreeItem[user][permission] = {
            id: user.concat('.', permission),
            permission: permission,
            label: label,
            isExist: false,
            type: type,
            filters: [{_submitted_by: user}]
        }
    })
    return permissionTreeItem;
}

export function getPermissionsExceptOwner(forms: FormType[], formId: string): PermissionType[] {
    const form = forms?.find(form => form.uid === formId)
    const owner_url = form?.owner;
    return form?.permissions.filter(permission => permission.user != owner_url) as PermissionType[]
}

export function getPermissionPerUser(permissions: PermissionType[], allPermissions?: KoboPermissionType[]): {
    permissionTree: PermissionTreeType,
    currentPermissions: Set<string>
} {

    const {permissionTree, selectedPermissions} = getPermissionTreePerUser(permissions, '')

    Object.keys(permissionTree)?.map(user => {
        allPermissions?.map(permission => {

            if (!Object.prototype.hasOwnProperty.call(permissionTree[user][permission.codename], 'id')) {
                permissionTree[user][permission.codename] = {
                    id: user.concat('.', permission.codename),
                    permission: permission.codename,
                    label: permission.name,
                    isExist: false,
                    type: '',
                }
            }

        })
    })

    return {permissionTree, currentPermissions: selectedPermissions};
}

export function getLocalPermissionsPerUser(forms: FormType[], localPermissions: LocalPermissionType[], formId: string) {
    const form = forms?.find(form => form.uid === formId)
    const owner = form?.owner__username
    const permissions: PermissionType[] = form?.permissions as PermissionType[]
    const {permissionTree, selectedPermissions} = getPermissionTreePerUser(permissions, owner)

    Object.keys(permissionTree)?.map(user => {

        permissionTree[user]?.partial_submissions?.partial_permissions?.map(permit => {
            const permissionName = getPermissionName(permit.url)
            const id = user.concat('.', permissionName)

            permissionTree[user][permissionName] = {
                id,
                permission: permissionName,
                label: '',
                isExist: true,
                type: PARTIAL_PERMIT,
                filters: permit.filters,
                isOwner: user === owner
            }
            selectedPermissions.add(id)
        })

        //update the label and add new that not selected
        localPermissions?.map(({permission, label, type}) => {

            if (!permissionTree[user][permission]) {
                permissionTree[user][permission] = {
                    id: user.concat('.', permission),
                    permission: permission,
                    label: label,
                    isExist: false,
                    type: PARTIAL_PERMIT,
                    isOwner: user === owner
                }
            } else {
                permissionTree[user][permission].label = label
            }

        })
    })

    return {permissionTree, currentPermissions: selectedPermissions, owner};
}

export function convertPermissionsToTreeData(userPermission): TreeNode[] {
    return [{
        id: 'abc',
        label: 'ABC'
    }]
}

export function convertTreeToPermissions(treeData: PermissionTreeType, selectedPermissions): BulkPermissionType[] {
    const bulkPermission: BulkPermissionType[] = []
    console.log(treeData);
    Object.keys(treeData).map(user => {
        const partialPermit: PartialPermissionType[] = []
        Object.keys(treeData[user]).map(permission => {
            const permitObj = treeData[user][permission]
            if (!permitObj.isOwner && permission !== PARTIAL_SUBMIT && selectedPermissions.has(permitObj.id)) {
                if (permitObj.type === PARTIAL_PERMIT) {
                    partialPermit.push({
                        url: makeUrl(permission, 'permissions/'),
                        filters: permitObj.filters
                    })
                } else {
                    bulkPermission.push({
                        user: makeUrl(user, 'users/'),
                        permission: makeUrl(permission, 'permissions/')
                    })
                }
            }
        })
        if (partialPermit.length) {
            bulkPermission.push({
                user: makeUrl(user, 'users/'),
                permission: makeUrl(PARTIAL_SUBMIT, 'permissions/'),
                [PARTIAL_PERMIT]: partialPermit
            })
        }

    })
    return bulkPermission;
}

import {PARTIAL_PERMIT} from "./permissionSlice.ts";

export interface KoboPermissionType {
    url: string
    codename: string
    implied: []
    contradictory: []
    name: string
}

export interface PartialPermissionType {
    url: string,
    filters: FilterType[]
}

export interface PermissionType {
    url: string,
    user: string,
    permission: string,
    label: string
    [PARTIAL_PERMIT]: PartialPermissionType[]
}

export interface FilterType {
    _submitted_by: string
}

export interface UserPermission {
    id: string
    permission: string,
    label: string,
    isExist: boolean,
    partial_permissions?: PartialPermissionType[],
    type?: string
    filters?: FilterType[],
    isOwner?: boolean,
}

export interface PermissionTreeType {
    [key: string]: { [key: string]: UserPermission }
}

export interface TreeNode {
    id: string,
    label: string,
    children?: TreeNode[]
}

export interface LocalPermissionType {
    permission: string
    label: string
    type?: string
}

export interface BulkPermissionType {
    user: string,
    permission: string
    [PARTIAL_PERMIT]?: PartialPermissionType[]
}
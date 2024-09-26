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

export interface GroupType {
    id: number,
    name: string,
}

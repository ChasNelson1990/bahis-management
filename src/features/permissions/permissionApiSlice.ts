import {baseApi} from "../../app/baseApi.ts";


export const permissionApiSlice = baseApi.injectEndpoints({
    endpoints: build => ({
        getPermissions: build.query({
            query: () => {
                return 'permissions/?format=json'
            },
        }),
    })
})

export const {useGetPermissionsQuery} = permissionApiSlice
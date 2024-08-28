import {baseApi} from "../../app/baseApi.ts";
import {KoboPermissionType} from "./Permission.model.ts";


export const permissionApiSlice = baseApi.injectEndpoints({
    endpoints: build => ({
        getPermissions: build.query({
            query: () => {
                return 'permissions/?format=json'
            },
            transformResponse: (response: { results: KoboPermissionType[] }) => response.results
        }),
        submitBulkPermission: build.mutation({
            query: ({bulkPermission, formId}) => ({
                url: `assets/${formId}/permission-assignments/bulk/`,
                method: 'POST',
                body: bulkPermission,
            })
        })
    })
})

export const {useGetPermissionsQuery, useSubmitBulkPermissionMutation} = permissionApiSlice
import {baseApi} from "../../app/baseApi.ts";

export const formApiSlice = baseApi.injectEndpoints({
    endpoints: build => ({
        getForms: build.query({
            query: () => {
                return `assets/?format=json`
            }
        }),
        getFormPermissions: build.query({
            query: (fromId) => {
                return `assets/${fromId}/`
            }
        })
    })
})

export const {useGetFormPermissionsQuery, useGetFormsQuery} = formApiSlice;

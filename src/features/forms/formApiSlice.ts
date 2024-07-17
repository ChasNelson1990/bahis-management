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
                console.log(fromId);
                return `assets/${fromId}/?format=json`
            }
        })
    })
})

export const {useGetFormPermissionsQuery, useGetFormsQuery} = formApiSlice;

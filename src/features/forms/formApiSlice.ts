import {baseApi} from "../../app/baseApi.ts";

export const formApiSlice = baseApi.injectEndpoints({
    endpoints: build => ({
        getForms: build.query({
            query: () => {
                // console.log("querying forms");

                return `assets/?format=json`
            }
        }),
        getFormPermissions: build.query({
            query: (fromId) => {
                // console.log(fromId);
                return `assets/${fromId}/`
            }
        })
    })
})

export const {useGetFormPermissionsQuery, useGetFormsQuery} = formApiSlice;

import {baseApi} from "../../app/baseApi.ts";
import {UserType} from "./userSlice.ts";


export const userApiSlice = baseApi.injectEndpoints({
    endpoints: build => ({
        getUsers: build.query({
            query: () => `users/`,
            transformResponse: (response: { results: UserType[] }) => response.results
        })
    })
})

export const {useGetUsersQuery} = userApiSlice
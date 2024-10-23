import {baseApi} from "../../app/baseApi.ts";
import {GroupType, UserType} from "./User.model.ts";


export const userApiSlice = baseApi.injectEndpoints({
    endpoints: build => ({
        getUsers: build.query<UserType[], void>({
            query: () => `users/?limit=10000&offset=0`,
            transformResponse: (response: { results: UserType[] }) => response.results
        }),
        getUsersByGroup: build.query<UserType[], string>({
            query: (groupName) => `utils/groups/${groupName}/users/`,
            transformResponse: (response: { results: UserType[] }) => response.results
        }),
        getGroups: build.query<GroupType[], void>({
            query: () => `utils/groups/`,
            transformResponse: (response: { results: GroupType[] }) => response.results
        })
    })
})

export const {useGetUsersQuery, useGetGroupsQuery, useGetUsersByGroupQuery} = userApiSlice
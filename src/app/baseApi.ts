import {createApi, fetchBaseQuery} from "@reduxjs/toolkit/query/react";

export const baseApi = createApi({
    baseQuery: fetchBaseQuery({
            baseUrl: "/api/v2/",
            credentials: "include",
            prepareHeaders: (headers) => {
                const token = localStorage.getItem('token');
                headers.set("authorization", `TOKEN ${token}`);
                headers.set("Content-Type", "application/json");
                headers.set('Accept', 'application/json');
                return headers;
            },
        },
    ),
    reducerPath: "api",
    // tagTypes: ["Permissions"],
    endpoints: () => ({}),
})
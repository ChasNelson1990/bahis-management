import {createApi, fetchBaseQuery} from "@reduxjs/toolkit/query/react";

export const baseApi = createApi({
    baseQuery: fetchBaseQuery({
            // baseUrl: "http://kf.sharful.com/api/v2/",
            baseUrl: "/api/v2/",
            credentials: "include",
            // mode: 'no-cors',
            prepareHeaders: (headers) => {
                headers.set("authorization", `TOKEN d7316cbff63921083545676fc9a3a9980d4355d6`);
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
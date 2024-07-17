import {useState} from "react";
import {useGetPermissionsQuery} from "./permissionApiSlice.ts";

interface PremissionProps {
    formId: string
}

export const Permission = (props: PremissionProps) => {

    const {data} = useGetPermissionsQuery(props.formId)
    return (<div>
            Permissions
            <div>
                {JSON.stringify(data)}
            </div>
        </div>
    )
}
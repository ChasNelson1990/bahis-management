import {UserPermission} from "./Permission.model.ts";
import {PermissionTreeItem} from "./PermissionTreeItem.tsx";
import {PARTIAL_SUBMIT} from "./permissionSlice.ts";


// type PermissionProps = TreeItem2Props & {
type PermissionProps = {
    userPermission: { [key: string]: UserPermission, }
    user: string
}


export const Permission = ({userPermission, user}: PermissionProps) => {
    return (
        <>
            {Object.keys(userPermission)?.map(permission => (
                (permission != PARTIAL_SUBMIT) &&
                <PermissionTreeItem
                    permitData={userPermission[permission]}
                    user={user}
                    itemId={userPermission[permission].id}
                    label={userPermission[permission].label}
                    key={userPermission[permission].permission}/>
            ))}
        </>
    );
};

import {UserPermissionType} from "./Permission.model.ts";
import {PermissionTreeItem} from "./PermissionTreeItem.tsx";
import {PARTIAL_SUBMIT} from "./permissionSlice.ts";


// type PermissionProps = TreeItem2Props & {
type PermissionProps = {
    userPermission: { [key: string]: UserPermissionType, }
    user: string,
    formOwner?: string
}


export const Permission = ({userPermission, user, formOwner}: PermissionProps) => {
    return (
        <>
            {Object.keys(userPermission)?.map(permission => (
                (permission != PARTIAL_SUBMIT) &&
                <PermissionTreeItem
                    formOwner={formOwner}
                    permitData={userPermission[permission]}
                    user={user}
                    itemId={userPermission[permission].id}
                    label={userPermission[permission].label}
                    key={userPermission[permission].id}/>
            ))}
        </>
    );
};

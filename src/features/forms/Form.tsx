import React, {useEffect, useMemo, useState} from 'react';
import {FormControl, InputLabel, MenuItem, Select, SelectChangeEvent} from "@mui/material";
import {useGetFormsQuery} from "./formApiSlice.ts";
import {Permissions} from "../permissions/Permissions.tsx";
import {setForms} from "./formSlice.ts";
import {useDispatch} from "react-redux";
import User from "../users/User.tsx";
import {FormType} from "./form.model.ts";


function Form() {
    const [selectedFormId, setSelectedFormId] = useState('')
    const dispatch = useDispatch()


    // const formList: FormType[] = [] as FormType[]


    const {data: formsData} = useGetFormsQuery(null)
    const formList: FormType[] = formsData?.results
    // const formList: FormType[] = useMemo(() => formsData?.results, [formsData?.results])

    useEffect(() => {
        dispatch(setForms(formList))
        formList && setSelectedFormId(formList[0]?.uid)
    }, [formList])

    const handleChange = (evt: SelectChangeEvent) => {
        setSelectedFormId(evt.target.value);
    }

    return (
        <div>
            <FormControl fullWidth>
                <InputLabel id="form-list-label">Form List</InputLabel>
                <Select
                    labelId="form-list-label"
                    label="Form List"
                    value={selectedFormId}
                    onChange={handleChange}
                >
                    {formList?.map((form, index) => (
                        <MenuItem key={form.uid}
                                  value={form.uid}>{form.name}</MenuItem>
                    ))}
                </Select>
            </FormControl>
            <Permissions formId={selectedFormId}/>
        </div>
    );
}

export default Form;